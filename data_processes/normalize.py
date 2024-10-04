import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Read the dataset
df = pd.read_csv(r'C:\Users\py\Kursach\iad_sistem_liza\data\tour_data_1.csv')

# Separate numerical columns
numerical_columns = ['Кол-во туристов', 'Длительность', 'Цена', 'Оценка']
original_values = df[numerical_columns].values

# Normalize data using MinMaxScaler
scaler = MinMaxScaler()
normalized_values = scaler.fit_transform(df[numerical_columns])

# Plotting prices before and after normalization
plt.figure(figsize=(8, 5))

# Plot original prices
plt.scatter(range(len(original_values[:, 2])), original_values[:, 2], color='blue', label='Before Normalization (Цена)')
# Plot normalized prices
plt.scatter(range(len(normalized_values[:, 2])), normalized_values[:, 2], color='green', label='After Normalization (Цена)')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Цена')
plt.title('Цена до и после нормализации')
plt.legend()

plt.show()

# Save normalized data to a new CSV
normalized_df = df.copy()
normalized_df[numerical_columns] = normalized_values

normalized_df.to_csv('normalized_dataset.csv', index=False)