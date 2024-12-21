```
Route:
    /ingredients/
    Method: GET
    Sample Response:
        [
        {
            "id": 1,
            "name": "Ginger",
            "amount": 77,
            "last_updated": "2024-12-21 13:58:41"
        }
        ]


Route:
    /ingredients/
    Method: POST
    Sample Payload:
        {
            "name": "Ginger",
            "amount": 4,
            "last_updated": "2024-12-21T21:56:57.354437"
        }

    

Route:
    /recipes/new
    Method: POST
    Sample Payload:
        {
            "name": "string",
            "taste": "string",
            "reviews": 0,
            "prep_time": 0,
            "cuisine_type": "string",
            "description": "string"
        }


Route:
    /recipes/all
    Method: GET
    Sample Response:
       [
            {
                "name": "Sweet Chorizo and Pepper Pasta",
                "taste": "sweet",
                "reviews": 4.5,
                "prep_time": 40,
                "cuisine_type": "Italian",
                "description": "Spicy chorizo and sweet bell peppers tossed with pasta in a light tomato sauce."
            },
            {
                "name": "Sweet Basil Pesto Pasta",
                "taste": "sweet",
                "reviews": 4.8,
                "prep_time": 35,
                "cuisine_type": "Italian",
                "description": "Classic Italian pesto made with sweet basil, garlic, pine nuts, and Parmesan, tossed with fresh pasta."
            },
            ....
       ]

Route:
    /recipes/recommendation
    Method: GET
    Sample Response:
      recipe_type: "Sweet but little Sour"

    Sample Response:
    {
        "User Message": "sweet",
        "AI Message": "You can cook Sweet Chorizo and Pepper Pasta"
    }
```