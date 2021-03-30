import os

import sqlite3
from pony import orm
# from models import Account, Message


db = orm.Database()


# TODO: Solve problem with class or delete it and use functions
class SQLiteDB:
    db_count = 0
    table_count = 0

    def __init__(self, provider: str = "sqlite", path: str = "", session_name: str = "", create_db: bool = False):

        if not session_name:
            session_name = f"db_{SQLiteDB.db_count}"

        if not os.path.exists(path):
            os.makedirs(path)

        db_name = os.path.join(path, f'{session_name}.db')

        db.bind(provider, db_name, create_db)
        db.generate_mapping(create_tables=True)

        SQLiteDB.db_count += 1

    def exists(self, table: str, field_name: str, field: str) -> bool:
        self.cursor.execute(f"""SELECT {field_name} FROM {table} WHERE {field_name}=?""", (field,))

        return True if self.cursor.fetchall() else False

    def update_table(self, fields: tuple, table_name: str = ""):

        if not table_name:
            table_name = f"table_{SQLiteDB.table_count}"

        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}
                                (date_ text, subject text, content text, content_extension text)""")

        print(fields[-1])
        if not self.exists(table_name, "content", fields[-1]):
            marks = ','.join(['?' for _ in range(len(fields))])
            self.cursor.execute(f"INSERT INTO {table_name} VALUES ({marks})", fields)
            self.connection.commit()

    def get_table(self, table_name: str):
        return self.cursor.execute(f"SELECT * FROM {table_name}")
