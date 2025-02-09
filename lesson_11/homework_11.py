# Вивести всі числа від 1 до 100, що діляться на 5

print("Числа від 1 до 100, що діляться на 5:")
for num in range(1, 101):
    if num % 5 == 0:
        print(num, end=" ")

print()
# Вивести всі парні числа від 1 до 20 за допомогою циклу for

print("Парні числа від 1 до 20:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num, end=" ")

print()
# Вивести всі парні числа від 20 до 40 у списку за допомогою comprehension

print("Парні числа від 20 до 40 за допомогою comprehension:")
even_numbers = [num for num in range(20, 41) if num % 2 == 0]
print(even_numbers)

print()
# Вивести суму чисел від 1 до 20

sum_numbers = sum(range(1, 21))
print("Сума чисел від 1 до 20:", sum_numbers)

print()
# Створити список чисел від 20 до 40 і за допомогою циклу for вивести всі числа, які діляться на 5 без остачі

numbers_list = list(range(20, 41))
print("Числа від 20 до 40, що діляться на 5:")
for num in numbers_list:
    if num % 5 == 0:
        print(num, end=" ")

print()
# Те саме, але за допомогою comprehension

numbers_multiple_of_5 = [num for num in range(20, 41) if num % 5 == 0]
print("Числа від 20 до 40, що діляться на 5 за допомогою comprehension:", numbers_multiple_of_5)

print()
# Створіть список трьох своїх улюблених фруктів і назвіть його favorite_fruits.
# Напишіть перевірку на те, чи входить фрукт у список. Якщо фрукт входить у список,
# виводиться повідомлення, на зразок You really like peaches!,
# у протилежному випадку - повідомлення про відсутність фрукту у списку.

favorite_fruits = ["apple", "banana", "strawberry"]
fruit = input("Enter a fruit: ").lower()

# Перевіряємо, чи є фрукт у списку
if fruit in favorite_fruits:
    print(f"You really like {fruit}s!")
else:
    print(f"{fruit.capitalize()} is not in your favorite fruits list.")

print()
# Створіть список years_list, що містить рік, в який ви народилися, і кожен наступний рік
# аж до вашого десятого дня народження. Наприклад, якщо ви народилися в 1995 році,
# список буде виглядати так: years_list = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005].
# Виведіть на екран, у якому із років, що міститься у списку years_list, вам виповнилося 6 років? Пам’ятайте,
# у перший рік вам було 0 років.

years_list = [1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
sixth_year = years_list[6]

print("Список років:", years_list)
print(f"Вам виповнилося 6 років у {sixth_year} році.")

print()
# Дано список з такими елементами: cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong'].
# Сформуйте з елементів списку повідомлення, у якому перед останнім елементом буде вставлено слово and.
# Наприклад, у нашому випадку, повідомлення буде таким: Budapest, Rome, Istanbul, Sydney, Kyiv and Hong Kong.
# Програма має працювати з будь-якими списками.

cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']

if len(cities) > 1:
    message = ", ".join(cities[:-1]) + " and " + cities[-1]
else:
    message = cities[0]  # Якщо список містить лише один елемент

print(message)

print()
# Дано два списки чисел: [1 6 3 5 6] та [10 12 6 5 1 4]. Порахуйте, скільки унікальних цифр міститься в обох з них.

list1 = [1, 6, 3, 5, 6]
list2 = [10, 12, 6, 5, 1, 4]

unique_numbers = set(list1 + list2)
print("Кількість унікальних чисел:", len(unique_numbers))

print()
# Запитати у користувача число і вивести повідомлення, чи є воно парним або непарним.

num = int(input("Введіть число: "))
if num % 2 == 0:
    print(f"Число {num} є парним.")
else:
    print(f"Число {num} є непарним.")

print()
# Напишіть скрипт, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем
# для цього користувача, то виводиться повідомлення Password accepted. У іншому випадку повідомлення буде
# Sorry, that is the wrong password і скрипт буде знову запитувати пароль.

correct_password = "qwerty123456"

while True:
    entered_password = input("Enter your password: ")

    if entered_password == correct_password:
        print("Password accepted")
        break
    else:
        print("Sorry, that is the wrong password. Please try again.")

print()
# Напишіть скрипт, в якій користувач вводить пароль. Додайте перевірку, що пароль містить НЕ ЛИШЕ цифри.
# У випадку успішності вивести 'Registered!', у випадку помилки вивести 'Password issue. Try again...'
# і скрипт буде знову запитувати пароль.

while True:
    password = input("Enter your password: ")

    if any(c.isalpha() for c in password):
        print("Registered!")
        break
    else:
        print("Password issue. Try again...")

print()
# Напишіть скрипт, де треба ввести 2 числа і поділити одне на інше.
# Додайте exception handler який буде перевіряти ділення на 0 або що введені дані дійсно є числами. Додати умови,
# Додати умови, якщо у результаті ділення отримуємо відємне число, пишемо 'The result is negative:' і додаємо до виводу
# результуючи величину. В іншому випадку пишемо 'The result is positive:' і також додаємо результуючи величину.

num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

try:
    result = float(num1) / float(num2)

    if result < 0:
        print(f"The result is negative: {result}")
    else:
        print(f"The result is positive: {result}")

except ValueError:
    print("Вводьте лише числа")
except ZeroDivisionError:
    print("На нуль ділити не можна")

print()
# Cкористайтеся третім аргументом функції range() для створення списку непарних чисел від 1 до 25
# і зведіть усі числа до 3 степені.

odd_numbers = [num ** 3 for num in range(1, 26, 2)]
print(odd_numbers)

print()
# У вас на рахунку Х (значення для всіх змінних оберіть самі). Ваша ціль - Y. Щомісяця ви додаєте на рахунок Z.
# Напишіть алгоритм, що виводитиме на кожній ітерації наступні показники (наприклад для значень  Х = 0;  Y = 100; Z = 10):
# 1 місяць. Зібрано 10$. Треба зібрати ще 90$
# 2 місяць. Зібрано 20$. Треба зібрати ще 80$
# 3 місяць. Зібрано 30$. Треба зібрати ще 70$
# і т.д.

X = 0
Y = 180
Z = 25

months = 0
while X < Y:
    months += 1
    X += Z
    accumulate = max(Y - X, 0)
    print(f"{months} місяць. Зібрано {X}$. Треба зібрати ще {accumulate}$")

print()
# Перетворити рядок "     nIce, CLEan TTTText!,,,, " на "Nice, clean text!" :)

input_str = "     nIce, CLEan TTTText!,,,, "
output_str = input_str.strip().lower().replace(",", "").replace("!", "").replace("ttt", "")

print(output_str.capitalize())
