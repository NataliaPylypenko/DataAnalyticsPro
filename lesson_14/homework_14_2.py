import pandas as pd

# print(df_copy.columns.tolist())
# ['DATETIME_ORIGINAL', 'USAGE_KWH', 'LAGGING_CURRENT_REACTIVE.POWER_KVARH', 'LEADING_CURRENT_REACTIVE_POWER_KVARH',
# 'CO2(TCO2)', 'LAGGING_CURRENT_POWER_FACTOR', 'LEADING_CURRENT_POWER_FACTOR', 'NSM', 'WEEKSTATUS', 'DAY_OF_WEEK',
# 'LOAD_TYPE', 'DATETIME_UPDATED']

# 1. Вивантаження файлу у pandas DataFrame та копіювання DataFrame у нову змінну
df = pd.read_csv('Lesson_14_task_2.csv')
df_copy = df.copy()

# 2. Конвертація атрибуту Date_Time
df_copy['Datetime_Updated'] = pd.to_datetime(df_copy['Date_Time'], dayfirst=True)

# 3. Перейменування атрибуту Date_Time в Datetime_Original
df_copy.rename(columns={'Date_Time': 'Datetime_Original'}, inplace=True)

# 4. Перетворення назв атрибутів у uppercase
df_copy.columns = df_copy.columns.str.upper()


# 5. Підрахунок кількості 0
zeros_count = (df_copy['LEADING_CURRENT_REACTIVE_POWER_KVARH'] == 0).sum()
print(f"Кількість нулів: {zeros_count}")

# 6. Фільтрація та підрахунок кількості рядків
filtered_df = df_copy[df_copy['LEADING_CURRENT_REACTIVE_POWER_KVARH'] != 0]
print(f"Кількість рядків після фільтрації: {len(filtered_df)}")

# 7. Фільтрація та перезапис DataFrame
df_copy = filtered_df.copy()

# 8. Мінімум, середнє та максимум Usage_kWh та NSM
usage_min = df_copy['USAGE_KWH'].min()
usage_mean = df_copy['USAGE_KWH'].mean()
usage_max = df_copy['USAGE_KWH'].max()

nsm_min = df_copy['NSM'].min()
nsm_mean = df_copy['NSM'].mean()
nsm_max = df_copy['NSM'].max()

print(f"USAGE_KWH: min={usage_min}, mean={usage_mean}, max={usage_max}")
print(f"NSM: min={nsm_min}, mean={nsm_mean}, max={nsm_max}")

# 9. Мінімум, середнє та максимум у довільному слайсі
slice_df = df_copy.iloc[100:200]  # Довільний слайс
usage_min_slice = slice_df['USAGE_KWH'].min()
usage_mean_slice = slice_df['USAGE_KWH'].mean()
usage_max_slice = slice_df['USAGE_KWH'].max()

nsm_min_slice = slice_df['NSM'].min()
nsm_mean_slice = slice_df['NSM'].mean()
nsm_max_slice = slice_df['NSM'].max()

print(f"USAGE_KWH_2: min={usage_min_slice}, mean={usage_mean_slice}, max={usage_max_slice}")
print(f"NSM_2: min={nsm_min_slice}, mean={nsm_mean_slice}, max={nsm_max_slice}")

# 10. Видалення DataFrame
del df
del df_copy