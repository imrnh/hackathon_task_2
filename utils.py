import json
from db import get_db_connection

def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Parse each JSON object 
        json_objects = []
        for line in lines:
            if line.strip(): 
                try:
                    json_object = json.loads(line.strip())  # Parse the JSON
                    json_objects.append(json_object)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
        
        return json_objects
    
    
def list_ingredients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ingredient")
    ingredients = cursor.fetchall()
    conn.close()
    
    ingradients_str = ""
    for row in ingredients:
        ig = {'name': row['name'], 'amount': row['amount'] }
        ingradients_str += str(ig)
    
    return ingradients_str