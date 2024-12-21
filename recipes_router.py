import os, json, shutil
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from models import RecipeModel
from utils import read_json_from_file
from llm import chatbot
from utils import list_ingredients

rcp_router = APIRouter(prefix="/recipes")

TMP_FILE = "lib/tmp/tmp.txt"
ROOT_FILE = "lib/recipes/my_fav_recipes.txt"

@rcp_router.post("/new")
def save_recipe(recp: RecipeModel):
    # Write to my_fav_recipes.txt
    # to maintain acid property, writing to a dummy file first.
    os.makedirs("lib", exist_ok=True)
    os.makedirs("lib/recipes", exist_ok=True)
    os.makedirs("lib/tmp", exist_ok=True)
    
    try:
        rd = recp.model_dump()
        
        # Temporary storage.
        with open(TMP_FILE, 'w') as tmp_file:
            json.dump(rd, tmp_file)
            tmp_file.close()
            
        # validate if already not written
        existing_items = read_json_from_file(ROOT_FILE)
        
        if existing_items.__contains__(rd):
            return HTTPException(status_code=400, detail="Recipe Already exists")     
    
        # Writing to original file if not already written.
        with open(ROOT_FILE, "a") as fav_file:
            json.dump(rd, fav_file)
            fav_file.write("\n")
            fav_file.close()
            
        os.remove("lib/tmp/tmp.txt")
        
        return JSONResponse(content="Successfully added a new recipe", status_code=status.HTTP_201_CREATED)
    
    except:
        return HTTPException(status_code=400, detail="Unable to create. Try again please")
    
    
    

@rcp_router.get("/all")
def get_recipes():
    try:
        existing_items = read_json_from_file(ROOT_FILE)
        return JSONResponse(content=existing_items, status_code=status.HTTP_200_OK)
    except Exception as e:
        return HTTPException(status_code=400, detail=e)


@rcp_router.get("/name")
def get_recipes(name: str):
    try:
        existing_items = read_json_from_file(ROOT_FILE)
        
        for item in existing_items:
            if item['name'] == name:
                return JSONResponse(content=item, status_code=status.HTTP_200_OK)
            
        return JSONResponse(content="No recipe found", status_code=status.HTTP_204_NO_CONTENT)
    
    except Exception as e:
        return HTTPException(status_code=400, detail=e)
    
    
    
    
@rcp_router.get("/recommendation")
def recipe_recommendation(recipe_type: str):
    # Get recipe information
    existing_items = read_json_from_file(ROOT_FILE)
    truncated_list = ""
    
    for itm in existing_items:
        itm.pop("description", "prep_time")
        truncated_list += str(itm)
        
        
    # Instruction prompt
    with open("lib\instruct.prompt.txt", "r") as fr:
        additional_instruction = fr.read()
        
    ingradients = list_ingredients()
    additional_instruction += f"\n {ingradients}"
    additional_instruction += f"\n\n This is the list of all favorite foods: {truncated_list}"
    
    recomm = chatbot(recipe_type, additional_instruction)
    
    return recomm