import csv
import os

def process_csv_file(input_file):
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as csvfile: # відкриває вхідний файл для читання
            reader = csv.reader(csvfile)
            header = next(reader)

            output_file = 'Lesson_14_task_1_processed.csv'

            with open(output_file, 'w', newline='', encoding='utf-8') as outfile: # створює новий файл для запису
                writer = csv.writer(outfile)
                writer.writerow(header)

                for row_num, row in enumerate(reader, start=2):
                    processed_row = []

                    for col_num, cell in enumerate(row, start=1):
                        if cell == '':
                            print(f"У рядку {row_num} пропущене значення {col_num}.")
                            processed_row.append("-")
                        elif cell.lower() == 'yes':
                            processed_row.append("YES")
                        elif cell.lower() == 'no':
                            processed_row.append("NO")
                        else:
                            try:
                                processed_row.append(str(round(float(cell))))
                            except ValueError:
                                processed_row.append(cell)

                    writer.writerow(processed_row)

            return os.path.abspath(output_file)

    except FileNotFoundError:
        return f"Помилка: Файл '{input_file}' не знайдено."
    except Exception as e:
        return f"Помилка під час обробки файлу: {e}"

input_file_path = 'Lesson_14_task_1.csv'
output_file_path = process_csv_file(input_file_path)

if "Помилка" not in output_file_path:
    print(f"Новий файл створено за шляхом: {output_file_path}")
else:
    print(output_file_path)