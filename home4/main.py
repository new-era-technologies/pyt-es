# Завдання 1
# Вивчіть основні стандартні винятки, які перераховані в цьому уроці.

print(dir(locals()["__builtins__"]))

# Завдання 2
# Напишіть програму-калькулятор, яка підтримує такі операції: додавання, віднімання, множення,
# ділення та піднесення до ступеня.
# Програма має видавати повідомлення про помилку та продовжувати роботу під час введення некоректних даних,
# діленні на нуль та зведенні нуля в негативний степінь.


def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def pow(a, b):
    return a**b


def get_res(a, b, x):
    match x:
        case "+":
            print(sum(a, b))
        case "-":
            print(sub(a, b))
        case "*":
            print(mult(a, b))
        case "/":
            try:
                print(div(a, b))
            except ZeroDivisionError:
                print("На нуль не ділимо")
        case "**":
            try:
                print(pow(a, b))
            except ZeroDivisionError:
                print("Введіть правильне число для степені")
        case _:
            print("Введіть правильну дію")


while True:
    num1 = int(input("Введіть 1 число: "))
    num2 = int(input("Введіть 2 число: "))
    oper = input("Введіть дію: ")

    try:
        get_res(num1, num2, oper)
    except Exception as e:
        print(e)


# Завдання 3
# Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
# Конструктор має генерувати виняток, якщо вказано неправильні дані.
# Введіть список працівників із клавіатури. Виведіть усіх співробітників, які були прийняті після цього року.


# Завдання 4
# Опишіть свій клас винятку.
# Напишіть функцію, яка викидатиме цей виняток, якщо користувач введе певне значення,
# і перехопіть цей виняток під час виклику функції.


# Завдання 5
# Створіть програму спортивного комплексу,
# у якій передбачене меню: 1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань, 4 - вартість тренування.
# Дані зберігати у словниках.
# Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури у відповідному пункті меню.
# Якщо ключ не буде знайдений, створити відповідний клас-Exception, який буде викликатися в обробнику виключень.

sports = {
    "first": "sport1",
    "second": "sport2",
    "third": "sport3",
    "forth": "sport4",
    "fifth": "sport5",
}

trainers = {
    "trainer1": "trainer1",
    "trainer2": "trainer2",
    "trainer3": "trainer3",
    "trainer4": "trainer4",
    "trainer5": "trainer5",
}

trainings = {"training1", "training2", "training3", "training4", "training5"}

prices = {"price1", "price2", "price3", "price4", "price5"}


menu = int(
    input(
        "1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань, 4 - вартість тренування "
    )
)


def show_values(x):

    for key, value in enumerate(x):
        print(value)


def get_menu(x):
    match (x):
        case 1:
            show_values(sports)
        case 2:
            show_values(trainers)
        case 3:
            show_values(trainings)
        case 4:
            show_values(prices)


def find_trainer(t, ts):

    try:
        value = ts[t]
        print(value)
    except KeyError:
        print("Такого тренера немає")


try:
    get_menu(menu)
except Exception as e:
    print(e)

trainer = input("Пошук по прізвищу тренера ")
find_trainer(trainer, trainers)
