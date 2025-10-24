import sqlite3
from db import queries
from config import path_db

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_ITEM)
    print("Data base is pluged")
    conn.commit()
    conn.close()

def add_item(item):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_ITEM,(item, ))
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return item_id

def get_items():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_ITEM)
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def delete_items(item_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_ITEM,(item_id, ))
    conn.commit()
    conn.close()

def update_items(item_id,new_item=None, is_bought=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if new_item is not None:
        cursor.execute(queries.UPDATE_ITEM, (new_item,item_id))

    if is_bought is not None:
        cursor.execute("UPDATE purchases SET is_bought=? WHERE id=?",(is_bought,item_id))
        
    conn.commit()
    conn.close()