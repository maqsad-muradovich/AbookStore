import sqlite3



class Database:
    def __init__(self, path_to_db = "main.db"):
        self.path_to_db = path_to_db


    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)
    
    def exe(self, sql: str, parametrs: tuple = None, fetchone = False, fetchall = False, commit = False):
        if not parametrs:
            parametrs = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parametrs)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data


    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id int NOT NULL,
        name varchar(250) NOT NULL,
        language varchar(250),
        PRIMARY KEY (id)
        );
        """
        self.exe(sql, commit=True)


    @staticmethod
    def format_argc(sql, parametrs: dict):
        sql += "AND".join([
            f"{item} = ?" for item in parametrs
        ])
        return sql, tuple(parametrs.values())
    

    def add_user(self, id: int, name: str, language: str = None):
        sql = "INSERT INTO Users(id, name, language) VALUES(?,?,?)"
        self.exe(sql, parametrs=(id, name, language), commit=True)

    def select_add_users(self):
        sql = "SELECT * FROM Users"
        return self.exe(sql, fetchall=True)


    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE"
        sql, parametrs = self.format_argc(sql, kwargs)

        return self.exe(sql, parametrs=parametrs, fetchone=True)

    def count_user(self):
        return self.exe("SELECT COUNT(*) FROM Users;",fetchone=True)
#
#
    def update_user_language(self, language, id):
        sql = f"""
        UPDATE Users SET language=? WHERE id=?
"""
        return self.exe(sql, parametrs=(language, id), commit=True)
#
#
    def delete_users(self):
        self.exe("DELETE FROM Users WHERE TRUE", commit=True)
#
#
    def user_language(self, id_key):
        return self.exe(f"SELECT language FROM Users WHERE id={id_key}", fetchone=True)[0]

    
def logger(statement):
    print(f"""
    ------------------------------------
    Executing:
    {statement}
    ------------------------------------
""")


# m = Database()
# m.create_table_users()
# # m.add_user(id=112233, name= "Salom")
# m.update_user_language(id=112233, language='en')
# print(m.user_language(id_key=112233))
