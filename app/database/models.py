from pony import orm

db = orm.Database()


class Account(db.Entity):
    login = orm.Required(str, unique=True)
    password = orm.Required(str)
    is_valid = orm.Required(bool)
    messages = orm.Set("Message")


class Message(db.Entity):
    date = orm.Optional(int)
    sender = orm.Optional(str)
    subject = orm.Optional(str)
    content = orm.Required(str)
    content_extension = orm.Required(str)
    owner = orm.Required(Account)

    orm.composite_key(sender, content)
