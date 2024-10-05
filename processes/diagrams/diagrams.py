''' 1 '''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Предположим, что ваш датасет загружен в df
df = pd.read_csv(r'C:\Users\py\Kursach\iad_sistem_liza\data\tour_data.csv')
#
# # Группировка по сезонам и подсчет общего количества туристов
# tourists_by_season = df.groupby('Сезон')['Кол-во туристов'].sum().reset_index()
#
# # Построение столбчатой диаграммы
# plt.figure(figsize=(10, 6))
# plt.bar(tourists_by_season['Сезон'], tourists_by_season['Кол-во туристов'], color='skyblue')
# plt.title('Количество туристов по сезонам')
# plt.xlabel('Сезон')
# plt.ylabel('Количество туристов')
# plt.xticks(rotation=45)
# plt.show()
''' 2 '''

# avg_price_by_region = df.groupby('Регион')['Цена'].mean().reset_index()
#
# # Построение столбчатой диаграммы
# plt.figure(figsize=(12, 6))
# plt.bar(avg_price_by_region['Регион'], avg_price_by_region['Цена'], color='salmon')
# plt.title('Средняя цена туров по регионам')
# plt.xlabel('Регион')
# plt.ylabel('Средняя цена')
# plt.xticks(rotation=45)
# plt.show()

''' 3 '''

# region_counts = df['Регион'].value_counts()
#
# # Построение круговой диаграммы
# plt.figure(figsize=(8, 8))
# plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', startangle=140)
# plt.title('Распределение туров по регионам')
# plt.axis('equal')  # Для равного круга
# plt.show()

''' 4 '''

# Плохо

#
# # Выбор интересующих колонок
# corr_data = df[['Кол-во туристов', 'Цена', 'Оценка']]
#
# # Расчет корреляционной матрицы
# corr_matrix = corr_data.corr()
#
# # Построение тепловой карты
# plt.figure(figsize=(8, 6))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
# plt.title('Тепловая карта корреляций')
# plt.show()


''' 5 '''

# # Определяем порог для популярных и непопулярных туров
# threshold = df['Кол-во туристов'].mean()
# df['Популярность'] = df['Кол-во туристов'].apply(lambda x: 'Популярный' if x > threshold else 'Непопулярный')
#
# # Группировка и подсчет средней цены
# avg_price_by_popularity = df.groupby('Популярность')['Цена'].mean().reset_index()
#
# # Построение столбчатой диаграммы
# plt.figure(figsize=(8, 6))
# plt.bar(avg_price_by_popularity['Популярность'], avg_price_by_popularity['Цена'], color='lightgreen')
# plt.title('Средняя цена туров для популярных и непопулярных туров')
# plt.xlabel('Тип тура')
# plt.ylabel('Средняя цена')
# plt.show()


''' 6 '''


# Подсчет числа туров в каждом регионе
# tours_count_by_region = df['Регион'].value_counts()
#
# # Построение столбчатой диаграммы
# plt.figure(figsize=(12, 6))
# plt.bar(tours_count_by_region.index, tours_count_by_region.values, color='orange')
# plt.title('Количество туров в каждом регионе')
# plt.xlabel('Регион')
# plt.ylabel('Количество туров')
# plt.xticks(rotation=45)
# plt.show()


''' 7 '''


# Определение топ-5 популярных туров
top_popular_tours = df.groupby('Название тура')['Кол-во туристов'].sum().nlargest(5).reset_index()

# Определение топ-5 прибыльных туров
top_profitable_tours = df.groupby('Название тура')['Цена'].sum().nlargest(5).reset_index()

# Определение топ-5 туров с высокими оценками
top_rated_tours = df.groupby('Название тура')['Оценка'].mean().nlargest(5).reset_index()

# Топ-5 популярных туров
plt.figure(figsize=(10, 6))
plt.bar(top_popular_tours['Название тура'], top_popular_tours['Кол-во туристов'], color='blue', alpha=0.7)
plt.title('Топ-5 популярных туров', fontsize=16)
plt.xlabel('Название тура', fontsize=14)
plt.ylabel('Количество туристов', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()  # Отображение первой диаграммы

# Топ-5 прибыльных туров
plt.figure(figsize=(10, 6))
plt.bar(top_profitable_tours['Название тура'], top_profitable_tours['Цена'], color='green', alpha=0.7)
plt.title('Топ-5 прибыльных туров', fontsize=16)
plt.xlabel('Название тура', fontsize=14)
plt.ylabel('Прибыль', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()  # Отображение второй диаграммы

# Топ-5 туров с высокими оценками
plt.figure(figsize=(10, 6))
plt.bar(top_rated_tours['Название тура'], top_rated_tours['Оценка'], color='orange', alpha=0.7)
plt.title('Топ-5 туров с высокими оценками', fontsize=16)
plt.xlabel('Название тура', fontsize=14)
plt.ylabel('Оценка', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()  # Отображение третьей диаграммы
