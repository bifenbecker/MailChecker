import poplib

mail = poplib.POP3_SSL('pop.poortenaar.com')
mail.user('info@poortenaar.com')
mail.pass_('78jeroen')
print(mail.list())

# # Выводит список папок в почтовом ящике.
# mail.select("inbox")  # Подключаемся к папке "входящие".
# result, data = mail.search(None, "ALL")
# print(data)
#
# ids = data[0]  # Получаем сроку номеров писем
# id_list = ids.split()  # Разделяем ID писем
# latest_email_id = id_list[-1]  # Берем последний ID
#
# result, data = mail.fetch(latest_email_id, "(RFC822)")  # Получаем тело письма (RFC822) для данного ID
#
# raw_email = data[0][1]  # Тело письма в необработанном виде
# print(raw_email)
# # включает в себя заголовки и альтернативные полезные нагрузки
