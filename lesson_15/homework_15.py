import pandas as pd

# Завантаження даних
file_path = "adult_data.csv"
df = pd.read_csv(file_path, skipinitialspace=True)
df_copy = df.copy()

# print(df_copy.columns.tolist())
# ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
# 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
# 'hours-per-week', 'native-country', 'salary']

# Підрахунок кількості чоловіків і жінок
gender_counts = df_copy["sex"].value_counts()
print(gender_counts)


# Обчислення середнього віку жінок
average_age_women = df_copy[df_copy["sex"] == "Female"]["age"].mean()
print('Середній вік жінок:', average_age_women)


# Частка громадян Німеччини
germany_count = df_copy[df_copy["native-country"] == "Germany"].shape[0]
total_count = df_copy.shape[0]
germany_share = germany_count / total_count
print('Частка громадян Німеччини:', germany_share)


# Які средні значення та средньоквадратичні відхилення віку тих, хто отримує більше 50K на рік i тих, хто отримує менше 50K на рік?
income_groups = df.groupby("salary")["age"].agg(["mean", "std"])
print(income_groups)


# Чи правда, що люди, які отримують більше 50k, мають як мінімум вищу освіту?
higher_education = ["Bachelors", "Masters", "Doctorate"]
high_income_edu = df[df["salary"] == ">50K"]["education"].isin(higher_education).all()
result = "Yes" if high_income_edu else "No"
print("Чи правда, що люди, які отримують більше 50k, мають як мінімум вищу освіту?", result)


# Порахуйте статистику віку для кожної раси і кожної статі. Знайдіть таким чином максимальний вік чоловіків раси Amer-Indian-Eskimo.
age_stats = df.groupby(["race", "sex"])["age"].describe()
print("Статистика віку для кожної раси і кожної статі:")
print(age_stats)
max_age = df[(df["race"] == "Amer-Indian-Eskimo") & (df["sex"] == "Male")]["age"].max()
print("Максимальний вік чоловіків раси Amer-Indian-Eskimo:", max_age)


# Серед кого більша доля багатіших (>50K): серед одружених чи не одружених чоловіків? За одружених вважаємо тих, у кого marital-status
# починається із Married (Married-civ-spouse, Married-spouse-absent или Married-AF-spouse), всі інші - не одружені.
df_men = df[df["sex"] == "Male"].copy()
df_men.loc[:, "married"] = df_men["marital-status"].str.startswith("Married")

married_rich = df_men[df_men["married"] & (df_men["salary"] == ">50K")].shape[0] / df_men[df_men["married"]].shape[0]
single_rich = df_men[~df_men["married"] & (df_men["salary"] == ">50K")].shape[0] / df_men[~df_men["married"]].shape[0]

print(f"Частка чоловіків із доходом >50K:")
print(f"- Одружені: {married_rich:.2%}")
print(f"- Неодружені: {single_rich:.2%}")
print("Більша доля багатіших серед одружених чоловіків" if married_rich > single_rich else "Більша доля багатіших серед не одружених чоловіків")


# Яку максимальну кількість годин в тиждень працює людина? Скільки людей працюють таку кількість годин і який відсоток серед них багатих?
max_hours = df["hours-per-week"].max()
num_people_max_hours = df[df["hours-per-week"] == max_hours].shape[0]
rich_percent = df[(df["hours-per-week"] == max_hours) & (df["salary"] == ">50K")].shape[0] / num_people_max_hours * 100

print(f"Максимальна кількість годин роботи на тиждень: {max_hours}")
print(f"Кількість людей, які працюють {max_hours} годин: {num_people_max_hours}")
print(f"Відсоток багатих серед них: {rich_percent:.2f}%")


# Проведіть описовий аналіз тривалості роботи на тиждень серед багатих і бідних, які висновки можна зробити, базуючись на описових статистиках?
work_hours_stats = df.groupby("salary")["hours-per-week"].describe()
print(work_hours_stats)

# Висновки:
# Багаті в середньому працюють більше годин на тиждень (45.47), ніж бідні (38.84).
# Медіана для обох груп однакова (40 годин), але 75% багатих працюють 50 годин, тоді як 75% бідних працюють 40 годин.
# Стандартне відхилення для бідних трохи вище, що вказує на більшу мінливість тривалості роботи в цій групі.
# Максимальна і мінімальна тривалість роботи однакова для обох груп (99 годин і 1 година відповідно).


# Покажіть через візуалізацію:
import matplotlib.pyplot as plt
import seaborn as sns

# Чи залежить кількість годин роботи від віку респондента?
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["age"], y=df["hours-per-week"], alpha=0.5)
plt.xlabel("Вік")
plt.ylabel("Години роботи на тиждень")
plt.title("Залежність кількості годин роботи від віку")
plt.show()

# Чи однаковий розподіл marital-status у різних статей?
plt.figure(figsize=(12, 6))
sns.countplot(x="marital-status", hue="sex", data=df, order=df["marital-status"].value_counts().index)
plt.xlabel("Сімейний стан")
plt.ylabel("Кількість людей")
plt.title("Розподіл сімейного стану за статтю")
plt.xticks(rotation=45)
plt.legend(title="Стать")
plt.show()

# Як кількість годин роботи змінюється для різних occupation?
plt.figure(figsize=(12, 6))
sns.boxplot(x="hours-per-week", y="occupation", data=df, orient="h", order=df["occupation"].value_counts().index)
plt.xlabel("Години роботи на тиждень")
plt.ylabel("Професія")
plt.title("Розподіл годин роботи серед різних професій")
plt.show()
