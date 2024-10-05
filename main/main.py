import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from static import ListingData

# Установим фиксированное значение для воспроизводимости
np.random.seed(42)
# Параметры генерации
num_tours = 1000  # Общее количество туров
seasons = ['лето', 'осень', 'зима', 'весна']
regions = ['Крым', 'Сочи', 'Алтай', 'Санкт-Петербург', 'Москва']

# Генерация данных
data = {
    'Название тура': [f"Тур {i}" for i in range(1, num_tours + 1)],
    'Регион': np.random.choice(regions, num_tours),
    'Сезон': np.random.choice(seasons, num_tours),
    'Кол-во туристов': np.random.randint(1, 100, num_tours),  # Количество туристов от 1 до 100
    'Длительность': np.random.randint(1, 15, num_tours),  # Длительность от 1 до 14 дней
    'Цена': np.random.randint(1000, 10000, num_tours),  # Цена от 1000 до 10000
    'Оценка': np.round(np.random.uniform(1, 10, num_tours), 1)  # Оценка от 1 до 10
}

listing_data = ListingData()
mse = listing_data.get_mso()
# Создание DataFrame
df = pd.DataFrame(data)

# Вычисление прибыли (можно добавить, если нужно)
df['Прибыль'] = df['Цена'] * df['Кол-во туристов']  # Пример вычисления прибыли

# Просмотр первых 10 строк датасета


# Сохранение датасета в CSV файл (опционально)
df.to_csv('tour_data.csv', index=False)

"""----------------------------------"""

df = pd.read_csv(r'C:\Users\py\Kursach\iad_sistem_liza\data\tour_data_1.csv')

# Предобработка данных
# Преобразование категориальных переменных в числовые с помощью One-Hot Encoding
encoder = OneHotEncoder(sparse_output=False)  # sparse_output=False для возвращения массива NumPy
encoded_features = encoder.fit_transform(df[['Сезон', 'Регион']])

# Создание нового DataFrame с закодированными значениями
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['Сезон', 'Регион']))

# Объединение закодированных данных с исходным DataFrame
df_processed = pd.concat([df, encoded_df], axis=1)
df_processed.drop(['Сезон', 'Регион', 'Название тура'], axis=1, inplace=True)

# Определение признаков (X) и целевой переменной (y)
X = df_processed.drop('Цена', axis=1)
y = df_processed['Цена']

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Оценка модели
y_pred = model.predict(X_test)
mso = mean_squared_error(y_test, y_pred)
print(f'Среднеквадратичная ошибка: {mse}')

# Предсказание трех самых прибыльных туров для каждого сезона
df['Цена'] = model.predict(df_processed.drop('Цена', axis=1))
top_tours = df.groupby('Сезон').apply(lambda x: x.nlargest(3, 'Цена')).reset_index(drop=True)

# Результаты
print(top_tours[['Название тура', 'Регион', 'Сезон', 'Цена']])
print(f"{top_tours['Название тура']} | {top_tours['Регион']} | {top_tours['Сезон']} | {top_tours['Цена']}")



















# # Загрузка данных (замените на свой источник данных)
# data = pd.read_csv(r'C:\Users\py\Kursach\iad_sistem_liza\data\tour_data.csv')
#
# # Преобразуем категориальные переменные
# data['Прибыль'] = data['Цена'] * data['Кол-во туристов']
#
# # Функция для выбора самых популярных туров
# def select_top_popular_tours(data, n=2):
#     # Сначала группируем данные по названиям туров и суммируем количество покупок и оценки
#     popular_tours = data.groupby('Название тура').agg({
#         'Кол-во туристов': 'sum',  # Суммируем количество семплов
#         'Оценка': 'mean'           # Берем среднюю оценку
#     }).reset_index()
#
#     # Сортируем по количеству туристов (покупок) и затем по оценке
#     top_popular_tours = popular_tours.nlargest(n, 'Кол-во туристов')
#     return top_popular_tours
#
# # Функция для выбора самых прибыльных туров
# def select_top_profitable_tours(data, n=2):
#     # Группируем данные по названиям туров и суммируем прибыль
#     profitable_tours = data.groupby('Название тура').agg({
#         'Прибыль': 'sum',          # Суммируем прибыль
#     }).reset_index()
#
#     # Сортируем по прибыли
#     top_profitable_tours = profitable_tours.nlargest(n, 'Прибыль')
#     return top_profitable_tours
#
# # Выбираем топ-2 популярных и топ-2 прибыльных туров
# top_popular_tours = select_top_popular_tours(data)
# top_profitable_tours = select_top_profitable_tours(data)
#
# # Выводим результаты
# print('Топ-2 популярных тура:')
# print(top_popular_tours[['Название тура', 'Кол-во туристов', 'Оценка']])
#
# print('\nТоп-2 прибыльных тура:')
# print(top_profitable_tours[['Название тура', 'Прибыль']])
