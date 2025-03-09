# Завдання:
# провести описовий та корреляційний аналіз запропонованого датасету.

# Використайте відомі вам методи візуалізації та опису, щоб розказати історію про дані.
# Об'єднайте дані в 2 групи та використайте відомі вам методи пошуку кореляцій:
# Числові: continuos, binary
# Категоріальні: categorical, binary
# Врахуйте, що викиди в числових даних можуть сильно впливати на кореляції.
# Якщо необхідна фільтрація "неадекватних" даних, вказуйте це. +


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Завантаження даних
data = pd.read_csv("health_data.csv", sep=";")

# Перевірка на наявність пропущених значень
# print(data.isnull().sum())

# пропущених значень немає

# Перетворення віку з днів у роки
data['age'] = data['age'] / 365
data['age'] = data['age'].astype(int)

# Опис даних
# print(data.describe())

# оскільки мінімальний вік 29 років тому мінімальна вага 10 кг є неприпустимою
# також присутні аномалії в даних для зросту, систолічного та діастолічного тиску

# фільтрація аномальних значень
data_clean = data[
    (data["height"].between(140, 210)) &
    (data["weight"].between(40, 180)) &
    (data["ap_hi"].between(90, 200)) &
    (data["ap_lo"].between(60, 120))
]

print(f"Розмір даних до фільтрації: {data.shape[0]}, після: {data_clean.shape[0]}")

# Опис даних
print(data_clean.describe())


# Описовий аналіз

# Розподіл віку
plt.figure(figsize=(10, 6))
sns.histplot(data_clean['age'], bins=30, kde=True)
plt.title('Розподіл віку')
plt.show()

# Розподіл зросту та ваги
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(data_clean['height'], bins=30, kde=True)
plt.title('Розподіл зросту')
plt.subplot(1, 2, 2)
sns.histplot(data_clean['weight'], bins=30, kde=True)
plt.title('Розподіл ваги')
plt.show()

# Розподіл артеріального тиску
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(data_clean['ap_hi'], bins=30, kde=True)
plt.title('Розподіл систолічного тиску')
plt.subplot(1, 2, 2)
sns.histplot(data_clean['ap_lo'], bins=30, kde=True)
plt.title('Розподіл діастолічного тиску')
plt.show()

# Розподіл холестерину та глюкози
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.countplot(x='cholesterol', data=data_clean)
plt.title('Розподіл холестерину')
plt.subplot(1, 2, 2)
sns.countplot(x='gluc', data=data_clean)
plt.title('Розподіл глюкози')
plt.show()

# Розподіл бінарних змінних
binary_vars = ['smoke', 'alco', 'active']
plt.figure(figsize=(15, 8))
for i, var in enumerate(binary_vars):
    plt.subplot(2, 3, i+1)
    sns.countplot(x=var, data=data)
    plt.title(f'Розподіл {var}')
plt.tight_layout()
plt.show()


# Кореляційний аналіз

# Обчислення кореляційної матриці
corr_matrix = data_clean.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Кореляційна матриця")
plt.show()

# Кореляція факторів із хворобами серця
corr_with_cardio = data_clean.corr()["cardio"].sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(
    x=corr_with_cardio.index,
    y=corr_with_cardio.values,
    hue=corr_with_cardio.index,
    palette="coolwarm",
    legend=False,
)
plt.xticks(rotation=45)
plt.title("Кореляція факторів із хворобами серця")
plt.show()


# Висновки

# Вік: Більшість учасників дослідження знаходяться у віці від 50 до 65 років.
# Зріст та вага: Розподіл зросту та ваги є нормальним, з деякими відхиленнями.
# Артеріальний тиск: Розподіл артеріального тиску показує, що більшість людей має нормальний тиск.
# Холестерин та глюкоза: Більшість учасників мають нормальний рівень холестерину та глюкози.
# Бінарні змінні: Більшість учасників не курять та не вживають алкоголь і є активними.

# Фізична активність, систолічний артеріальний тиск та діастолічний артеріальний тиск, вік, холестерин, вага та глюкоза
# мають позитивну кореляцію з cardio, що свідчить про їхній важливий вплив на серцево-судинні захворювання.
# Вживання алкоголю, зріст, куріння та фізична активність мають слабку негативну кореляцію з cardio.
