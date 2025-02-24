import pandas as pd

# Завантаження даних
file_path = "adult_data.csv"
df = pd.read_csv(file_path, skipinitialspace=True)
df_copy = df.copy()

# print(df_copy.columns.tolist())
# ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
# 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
# 'hours-per-week', 'native-country', 'salary']


print(df_copy.head())
