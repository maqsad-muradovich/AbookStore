import sqlite3
connetion = sqlite3.connect(r"AbookStore_2/data/AbS_database.db")
kursor = connetion.cursor()


def create_table():
    kursor.execute("""CREATE TABLE IF NOT EXISTS users
                   (id INTEGER, lan TEXT)""")
    connetion.commit()

def insert_user(id, lan):
    kursor.execute("""INSERT INTO users VALUES (?,?)""", (id,lan))
    connetion.commit()
    # pass

def update_user(id, lan):
    kursor.execute("""UPDATE users SET lan=? WHERE id=?""",(lan,id))
    connetion.commit()

def delete_user():
    pass

def info_user():
    pass

# create_table()
