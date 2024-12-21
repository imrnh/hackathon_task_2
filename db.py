import sqlite3


# Database connection
DB_NAME = "database.db"
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Enable dictionary-style row access
    return conn

# Initialize the database and create the Ingredient table
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Ingredient (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                amount INTEGER NOT NULL,
                last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """
    )
    conn.commit()
    conn.close()

init_db()