from database.models import db

from pony import orm


# TODO: Add docs for class and its functions
class SQLiteDB:
    db_count = 0
    table_count = 0

    def __init__(self, filename: str, create_db: bool, create_tables: bool) -> None:
        db.bind('sqlite', filename, create_db)
        db.generate_mapping(create_tables=create_tables)

        # if not session_name:
        #     session_name = f"db_{SQLiteDB.db_count}"
        #
        # if not os.path.exists(path):
        #     os.makedirs(path)
        #
        # SQLiteDB.db_count += 1

    @orm.db_session
    def get_entry(self, table: db.Entity, unique_fields: dict) -> bool:
        if table.get(**unique_fields):
            return True
        else:
            return False

    @orm.db_session
    def add_in_table(self, table: db.Entity, data: dict, unique_fields: dict) -> tuple:
        entry = self.get_entry(table, unique_fields)

        if not entry:
            entry = table(**data)
            return True, entry
        else:
            return False, entry

    @orm.db_session
    def show_table(self, table: db.Entity, end: str = '') -> None:
        table.select().show()
        print(end=end)
