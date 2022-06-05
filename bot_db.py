import sqlite3
from config import bot

def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()
    if db:
        print("База данных подключена")
    db.execute("CREATE TABLE IF NOT EXISTS food ("
               "id INTEGER PRIMARY KEY, name_food TEXT, "
               "load_photo  TEXT, discription TEXT, Price INTERSECT)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa VALUES (?, ?, ?, ?)"), tuple(data.value())
        db.commit()

async def sql_command_random(massege):
    result = cursor.execute("SELECT * FROM food").fetchall()
    random_user = random.randint(0, len(result)-1)
    await bot.send_message(message. from_user.id,
                           f"Name_food:{result[random_user][0]}\n"
                           f"load_photo:{result[random_user][1]}\n"
                           f"discription:{result[random_user][2]}\n"
                           f"price:{result[random_user][3]}\n)

async def sql_command_all():
        return cursor.execute("SELECT * FROM food").fetchall()

async def sql_command_delete (id):
cursor.execute("DELETE FROM food WHERE id == ?", (id,))