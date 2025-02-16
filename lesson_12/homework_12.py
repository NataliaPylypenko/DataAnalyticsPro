# 1
def get_odd_numbers(n = 1):
    if n > 63:
        return
    if n % 2 != 0:
        print(n)

    get_odd_numbers(n + 1)

get_odd_numbers()


# 2
def convert_to_weeks(days, hours, minutes):
    total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60)
    weeks = total_seconds / 7 * 24 * 60 * 60

    return weeks

print("Count weeks", round(convert_to_weeks(16, 2, 25), 2))


# 3
def filter_numbers(numbers):

    if len(numbers) < 20:
        return "Список повинен містити не менше 20 елементів."

    filtered_numbers = [num for num in numbers if 50 <= num <= 75 and num % 4 == 0]

    return filtered_numbers

list_1 = [48, 52, 56, 60, 64, 68, 72, 76, 80, 50, 54, 59]
list_2 = [48, 52, 56, 60, 64, 68, 72, 76, 80, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 55, 59]

print("List 1", filter_numbers(list_1))
print("List 2", filter_numbers(list_2))


4
def get_total_cost(goods):

    if len(goods) < 10:
        return "Кількість товарів повинна бути не менше 10."

    total_price = sum(goods.values())

    return total_price

products = {
    "Молоко": 50,
    "Хліб": 35,
    "Яйця": 70,
    "Цукор": 40,
    "Сіль": 15,
    "Масло": 100,
    "Сир": 80,
    "Кава": 500,
    "Чай": 90,
    "Шоколад": 60
}

print("Total cost:", get_total_cost(products))


# 5
def get_total_cost_v2(**goods):

    if len(goods) < 10:
        return "Кількість товарів повинна бути не менше 10."

    total_price = sum(goods.values())

    return total_price

print("Total cost v2:", get_total_cost_v2(**products))


# 6
def del_numbers(string):

    new_string = ""

    for i in string:
        if not i.isdigit():
            new_string += i

    return new_string

string_v1 = "Hello123 world456"

print(del_numbers(string_v1))


# 7
def convert_temperature(temperature, scale):
    if scale.upper() == "C":
        return (temperature * 1.8) + 32
    elif scale.upper() == "F":
        return (temperature - 32) / 1.8
    else:
        return "Error: Unknown temperature scale. Use 'C' or 'F'."

print("25°C =", convert_temperature(25, "C"), "°F")
print("77°C =", convert_temperature(77, "F"), "°C")

# 8
def convert_shoe_size(size, scale):
    EU_size = ["36 2/3", "37 1/3", "38", "39", "39 2/3", "40 1/3", "41", "42", "42 2/3", "43 1/3", "44", "45", "45 2/3", "46 1/3", "47", "48", "48 2/3", "49 1/3", "50"]
    UA_size = ["35", "36", "36.5", "37", "38", "38/39", "40.5", "41", "41.5", "42", "42/43", "43", "44", "45", "46", "47", "47.5", "48", "48.5"]

    if scale.upper() == "UA":
        if size in UA_size:
            i = UA_size.index(size)
            return EU_size[i]
        else:
            return "Error: Incorrect UA size."
    elif scale.upper() == "EU":
        if size in EU_size:
            i = EU_size.index(size)
            return UA_size[i]
        else:
            return "Error: Incorrect EU size."
    else:
        return "Error: Unknown size scale. Please use 'UA' or 'EU'."

print("36 (UA) =", convert_shoe_size("36", "UA"), "(EU)")
print("41 (EU) =", convert_shoe_size("41", "EU"), "(UA)")


# 9
def convert_to_upper(string_list):
    return (lambda strings: [s.upper() for s in strings])(string_list)

list = ["apple", "banana", "cherry"]
print(convert_to_upper(list))


# 10
def get_season(month):

    if 3 <= month <= 5:
        return "spring"
    elif 6 <= month <= 8:
        return "summer"
    elif 9 <= month <= 11:
        return "autumn"
    elif month == 1 or month == 2 or month == 12:
        return "winter"
    else:
        return None

print(get_season(1))
print(get_season(13))
