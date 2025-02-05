# Завдання 1
# Реалізувати наступні арифметичні операції і вивести результати:
print(2 * 3) # 6
print((3 * 3 + 8) / 3) # 5.666666666666667
print(8 // 3) # 2 - ціле число
print(8 % 3) # 2 - остача
print(5 ** 2) # 25
# print("Hello ' + 'world') # Error через різні види лапок
print('Python'*5) # PythonPythonPythonPythonPython
print(5 < 9) # True

# Завдання 2
# Створити дві змінні текстового типу, використовуючи одинарні і подвійні лапки.

# 2.1. Створення змінних
name = 'Natalia'
surname = "Pylypenko"

# 2.2. Поєднання змінних
full_name = name + ' ' + surname
print(full_name)

# 2.3. Перетворення до верхнього та нижнього регістрів
print(full_name.upper())
print(full_name.lower())

# 2.4. Індекси останніх трьох літер імені
index1 = full_name.index(name) + len(name) - 3
index2 = index1 + 1
index3 = index1 + 2
print("Indexes last three letters:", index1, index2, index3)

# 2.5. Індекси перших двох літер прізвища
index4 = full_name.index(surname)
index5 = index4 + 1
print("Indexes first two letters:", index4, index5)

# 6. Замінюємо перше слово на інше логічне слово
new_full_name = full_name.replace(name, "Ms")
print("new full name:", new_full_name)

# Завдання 3
# Cлайси (як змінну використайте Python Zen).
# import this
python_zen = "Beautiful is better than ugly."
print("First 10 characters:", python_zen[:10]) # 'Beautiful '
print("10 characters from 3:", python_zen[2:12]) # 'autiful is'
print("Last 10 characters:", python_zen[-10:]) # 'than ugly.'
print("String in reverse order:", python_zen[::-1]) # '.ylgu naht retteb si lufituaeB'
print("Symbols with even indices:", python_zen[::2]) # 'Batfli etrta gy'
print("Symbols with odd indices:", python_zen[1::2]) # 'euiu sbte hnul.'

# Завдання 4
# Створіть дві змінні з будь-якими числовими значеннями
# з 5 знаками до коми та 5 знаками після коми.
num1 = 12345.67890
num2 = 67890.12345

# операцій порівняння
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 >= num2:", num1 >= num2)
print("num1 <= num2:", num1 <= num2)
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)

# логічні операції
print(num1 > num2 and num1 > 0)
print(num2 < 100 or num2 == 50)

# форматування числа
print(f'{num1:.2f}')
print(f'{num1:.2%}')
print(f'{num1:,.5f}')

# Завдання 5
# Створіть словник. Наповніть словник 10 парами
# ключ - значення на будь-яку тему

actors = {
    "Меттью Мак-Конагей": "Інтерстеллар",
    "Кіану Рівз": "Матриця",
    "Джонні Депп": "Пірати Карибського моря",
    "Роберт Дауні мл.": "Залізна людина",
    "Том Круз": "Місія нездійсненна",
    "Х'ю Джекман": "Логан",
    "Морган Фрімен": "Втеча з Шоушенка",
    "Бред Пітт": "Бійцівський клуб",
    "Метт Деймон": "Марсіянин",
    "Скарлетт Йоганссон": "Чорна вдова"
}

actors_copy = actors.copy()
actors_copy["Зендея"] = "Дюна"

print("Actors:", list(actors_copy.keys()))
print("Movies:", list(actors_copy.values()))

another_actors = {
    "Дензел Вашингтон": "Тренувальний день",
    "Аль Пачіно": "Хрещений батько",
    "Рассел Кроу": "Гладіатор",
    "Том Хенкс": "Форрест Гамп"
}

actors_copy.update(another_actors)
print("combined dictionary:", actors_copy)

actors_copy.clear()
print("cleared dictionary:", actors_copy)

# Завдання 6
# Створіть список з 10 значеннями числового типу.
# Порядок повинен бути хаотичним.

numbers = [42, 7, 19, 85, 3, 56, 23, 91, 11, 34]
print("numbers:", numbers)

numbers.sort()
print("sorted numbers:", numbers)

numbers.pop(-3)
print("without a third element:", numbers)

print("6th element:", numbers[5])

numbers.insert(1, 77)
print("added new element:", numbers)

another_numbers = [101, 202, 303, 404, 505]

numbers.extend(another_numbers)
print("combined numbers:", numbers)
