import os
from pony import orm


class SQLiteDB:
    db_count = 0
    table_count = 0

    # TODO: solve problem with __init__ and database location
    def __init__(self, path: str = "", session_name: str = ""):
        pass

        # if not session_name:
        #     session_name = f"db_{SQLiteDB.db_count}"
        #
        # if not os.path.exists(path):
        #     os.makedirs(path)
        #
        # SQLiteDB.db_count += 1

    @orm.db_session
    def get_entry(self, table: orm.core.EntityMeta, unique_fields: dict) -> bool:
        if table.get(**unique_fields):
            return True
        else:
            return False

    @orm.db_session
    def add_in_table(self, table: orm.core.EntityMeta, data: dict, unique_fields: dict) -> tuple:
        entry = self.get_entry(table, unique_fields)

        if not entry:
            entry = table(**data)
            return (True, entry)
        else:
            return (False, entry)

    @orm.db_session
    def show_table(self, table: orm.core.Entity) -> None:
        table.select().show()
