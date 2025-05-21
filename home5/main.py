# Завдання 1
# Вивчити роботу інструментів, які розглядалися на занятті.


# Завдання 2
# Створити клас Contact з полями surname, name, age, mob_phone, email.
# Додати методи get_contact, sent_message.
# Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, job.
# Додати методи get_message.
# Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів: __dict__, __base__, __bases__.
# Роздрукувати інформацію на екрані.


class Contact:

    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        pass

    def send_message(self):
        pass


class UpdateContact(Contact):

    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        pass


contact1 = Contact("Bot", "Botov", 999, 12345, "bot@email")
updateContact1 = UpdateContact("Dot", "Dotov", 111, 9876, "dot@email", "president")

print(Contact.__dict__)
print(Contact.__base__)
print(Contact.__bases__)

print(UpdateContact.__dict__)
print(UpdateContact.__base__)
print(UpdateContact.__bases__)


# Завдання 3
# Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr().
# Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.


print(hasattr(updateContact1, "name"))
print(hasattr(contact1, "job"))

print(getattr(contact1, "surname"))
print(getattr(updateContact1, "surname"))

setattr(updateContact1, "weekdays", "sunday")
print(hasattr(updateContact1, "weekdays"))
print(hasattr(contact1, "weekdays"))

delattr(contact1, "mob_phone")
print(hasattr(contact1, "mob_phone"))
print(hasattr(updateContact1, "mob_phone"))
print(getattr(contact1, "mob_phone"))
print(getattr(updateContact1, "mob_phone"))


# Завдання 4

# Використовуючи код з завдання 2, створити 2 екземпляри обох класів. Використати функції isinstance() – для перевірки екземплярів класу (за яким класом створені) та issubclass() – для перевірки і визначення класу-нащадка.

# Завдання 5

# Використовуючи код завдання 2 надрукуйте у терміналі інформацію, яка міститься у класах Contact та UpdateContact та їх екземплярах. Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів. Порівняйте їх. Зробіть відповідні висновки.

# Завдання 6

# Використовуючи код завдання 2 надрукуйте у терміналі всі методи, які містяться у класі Contact та UpdateContact.
