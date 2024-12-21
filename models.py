from pydantic import BaseModel
from datetime import datetime


# Pydantic model for Ingredient
class Ingredient(BaseModel):
    name: str
    amount: int
    last_updated: str = datetime.now().isoformat()


class IngredientAmountUpdateModel(BaseModel):
    amount: int
    
    
class RecipeModel(BaseModel):
    name: str
    taste: str # eg. sweet, sour or combination. therefore left as taste. If kept empty, LLM filled that.
    reviews: float # User input.
    prep_time: int # Min
    cuisine_type: str
    description: str