import sqlite3
connetion = sqlite3.connect("data\AbS_database.db", uri= True)
kursor = connetion.cursor()


def create_table():
    kursor.execute("""CREATE TABLE IF NOT EXISTS super_users
                   (num NUMERIC , name TEXT, id INTEGER, phone_number TEXT, lan TEXT, status TEXT)""")
    connetion.commit()

def insert_info(num, name, id, phone_number, lan):
    kursor.execute("INSERT INTO users (?,?,?,?,?)", (num, name, id, phone_number, lan))
    connetion.commit()

create_table()
