CREATE_TABLE_ITEM = """
    CREATE TABLE IF NOT EXISTS purchases(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         product TEXT NOT NULL,
         is_bought INTEGER DEFAULT 0
    )
"""

INSERT_ITEM = "INSERT INTO purchases(product) VALUES (?)"

SELECT_ITEM = "SELECT id, product, is_bought FROM purchases"

UPDATE_ITEM = "UPDATE purchases SET product = ? WHERE id = ?"

DELETE_ITEM = "DELETE FROM purchases WHERE id = ?"

