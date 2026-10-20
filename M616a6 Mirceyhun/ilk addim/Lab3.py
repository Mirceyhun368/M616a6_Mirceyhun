import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Создание примерного набора данных
data = {
    'Дисциплина': ['Математика', 'История', 'Программирование', 'Физика', 'Философия', 'Английский', 'Химия', 'Физкультура', 'Экономика'],
    'Средний_балл': [65, 85, 70, 60, 90, 88, 62, 95, 75],
    'Процент_сдачи': [50, 95, 60, 45, 98, 90, 55, 100, 75]
}
df = pd.DataFrame(data)

# 2. Выбор показателей успеваемости
X = df[['Средний_балл', 'Процент_сдачи']]

# 3. Масштабирование данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Применение алгоритма K-means (делим на 3 группы: сложные, средние, легкие)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Кластер'] = kmeans.fit_predict(X_scaled)

print("Результаты кластеризации дисциплин:")
print(df)

# 5. Визуализация результатов
plt.figure(figsize=(10, 6))
plt.scatter(df['Средний_балл'], df['Процент_сдачи'], c=df['Кластер'], cmap='plasma', s=100)

# Добавление названий дисциплин на график
for i, txt in enumerate(df['Дисциплина']):
    plt.annotate(txt, (df['Средний_балл'][i] + 0.5, df['Процент_сдачи'][i] + 0.5))

plt.xlabel('Средний балл')
plt.ylabel('Процент сдачи (%)')
plt.title('Кластеризация дисциплин по успеваемости')
plt.grid(True)
plt.show()