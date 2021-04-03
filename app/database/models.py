from pony import orm

db = orm.Database()


class Account(db.Entity):
    login = orm.Required(str, unique=True)
    password = orm.Required(str)
    is_valid = orm.Required(bool)
    messages = orm.Set("Message")


class Message(db.Entity):
    date = orm.Required(int)
    sender = orm.Required(str)
    subject = orm.Required(str)
    content = orm.Required(str)
    content_extension = orm.Required(str)
    owner = orm.Required(Account)

    orm.composite_key(subject, content)
