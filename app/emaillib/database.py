import sqlite3


class SQLiteDB:
    db_count = 0
    table_count = 0

    def __init__(self, db_name: str = ""):

        if not db_name:
            db_name = f"db_{SQLiteDB.db_count}"

        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        SQLiteDB.db_count += 1

    def exists(self, table: str, field_name: str, field: str) -> bool:
        self.cursor.execute(f"""SELECT {field_name} FROM {table} WHERE {field_name}=?""", (field,))

        return True if self.cursor.fetchall() else False

    def update_table(self, fields: tuple, table_name: str = ""):

        if not table_name:
            table_name = f"table_{SQLiteDB.table_count}"

        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}
                                (folder text, subject text, content text, content_extension text)""")

        print(fields[-1])
        if not self.exists(table_name, "content", fields[-1]):
            marks = ','.join(['?' for _ in range(len(fields))])
            self.cursor.execute(f"INSERT INTO {table_name} VALUES ({marks})", fields)
            self.connection.commit()

    def get_table(self, table_name: str):
        return self.cursor.execute(f"SELECT * FROM {table_name}")
