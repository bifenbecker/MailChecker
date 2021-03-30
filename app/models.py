from pony import orm
from database import db


class Account(db.Entity):
    login = orm.Required(str, unique=True)
    password = orm.Required(str)
    valid = orm.Required(bool)
    messages = orm.Set("Message")


class Message(db.Entity):
    date = orm.Required(str)
    sender = orm.Required(str)
    subject = orm.Required(str)
    content = orm.Required(str)
    content_extension = orm.Required(str)
    owner = orm.Required(Account)

    class Meta:
        unique_together = ('subject', 'content')


def config(provider: str, filename: str, create_db: bool = False) -> None:
    db.bind(provider, filename, create_db)
    db.generate_mapping(create_tables=True)


config(provider='sqlite', filename='database.sqlite', create_db=True)
