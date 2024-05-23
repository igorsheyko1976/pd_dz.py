import pandas as pd

data = {
    'Имя': ['Игорь', 'Борис', 'Владимир', 'Дмитрий', 'Елена', 'Фёдор', 'Галина', 'Ирина', 'Ольга', 'Павел'],
    'Математика': [5, 4, 3, 5, 4, 3, 5, 4, 4, 5],
    'Физика': [5, 5, 4, 5, 4, 3, 5, 4, 4, 5],
    'Русский язык': [5, 4, 3, 4, 5, 4, 5, 5, 4, 4],
    'История': [5, 4, 5, 3, 5, 4, 5, 4, 4, 5],
    'Литература': [5, 3, 4, 5, 5, 4, 5, 4, 3, 5]
}

df = pd.DataFrame(data)

print("Таблица данных:")
print(df)

mean_scores = df.mean(numeric_only=True)
median_scores = df.median(numeric_only=True)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)

IQR_math = Q3_math - Q1_math

std_deviation = df.std(numeric_only=True)

print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

print("\nМедианная оценка по каждому предмету:")
print(median_scores)

print("\nQ1 и Q3 для оценок по математике:")
print(f"Q1: {Q1_math}")
print(f"Q3: {Q3_math}")

print("\nIQR для оценок по математике:")
print(IQR_math)

print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)
