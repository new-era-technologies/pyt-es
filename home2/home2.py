# Завдання 1
# Створіть клас Editor, який містить методи view_document та edit_document.
# Нехай метод edit_document виводить на екран інформацію про те,
# що редагування документів недоступне для безкоштовної версії.
# Створіть підклас ProEditor, у якому цей метод буде перевизначено.
# Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor.
# Викликайте методи перегляду та редагування документів.


# class Editor:

#     def view_document():
#         pass

#     def edit_document():
#         print("Редагування документів недоступне для безкоштовної версії")


# class Proeditor:

#     def edit_document():
#         print("Редагування документів доступне")


# proper_key = "asd"

# key = input("Введіть ліцензійний ключ: ")

# if key == proper_key:
#     current_editor = Proeditor
# else:
#     current_editor = Editor

# current_editor.edit_document()


# Завдання 2
# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші.
# Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на кнопку.


# Завдання 5
# Використовуючи код example_10,
# створіть статичний метод класу  ( для створення використовуйте декоратор @staticmethod ),
# метод має приймати вік людини та перевіряти чи досягла вона повноліття,
# метод має повертати True або False


class MyClass1:

    total = []

    @staticmethod
    def isAdult(age):
        if age > 18:
            return True

    @classmethod
    def quantityAdult(cls, quantity):
        for _ in range(quantity):
            quantity -= cls.isAdult(cls.age)
            return quantity


m_per1 = MyClass1.isAdult(19)
m_per2 = MyClass1.isAdult(9)
m_per3 = MyClass1.isAdult(1)
m_per4 = MyClass1.isAdult(39)
m_per5 = MyClass1.isAdult(79)


# Завдання 6
# Використовуючи код example_10,
# створіть класовий метод ( для створення використовуйте декоратор @classmethod ).
# Метод має підраховувати кількість об'єктів цього класу які досягли повноліття,
# для вирішення задачі використовуйте статичний метод створенний в завданні 5
