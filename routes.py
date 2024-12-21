from fastapi import APIRouter, HTTPException
from models import Ingredient, IngredientAmountUpdateModel
import sqlite3
from db import get_db_connection

router = APIRouter()



@router.post("/ingredients/")
def create_ingredient(ingredient: Ingredient):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if ingredient.amount < 0:
            raise HTTPException(status_code=400, detail="Cannot be negative amount")
        
        cursor.execute(
            "INSERT INTO Ingredient (name, amount) VALUES (?, ?)",
            (ingredient.name, ingredient.amount),
        )
        conn.commit()
        return {"id": cursor.lastrowid, "name": ingredient.name, "amount": ingredient.amount}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        conn.close()


@router.get("/ingredients/")
def list_ingredients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ingredient")
    ingredients = cursor.fetchall()
    conn.close()
    return [dict(row) for row in ingredients]


@router.get("/ingredients/{ingredient_id}")
def get_ingredient(ingredient_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ingredient WHERE id = ?", (ingredient_id,))
    ingredient = cursor.fetchone()
    conn.close()
    if ingredient:
        return dict(ingredient)
    else:
        raise HTTPException(status_code=404, detail="Ingredient not found")


@router.put("/ingredients/{ingredient_id}")
def update_ingredient(ingredient_id: int, ingredient: IngredientAmountUpdateModel):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if ingredient.amount <0:
            raise HTTPException(status_code=400, detail="Cannot be negative amount")
        
        cursor.execute(
            """
            UPDATE Ingredient
            SET amount = ?, last_updated = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (ingredient.amount, ingredient_id),
        )
        conn.commit()
        if cursor.rowcount:
            return {"message": "Ingredient updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Ingredient not found")
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        conn.close()

