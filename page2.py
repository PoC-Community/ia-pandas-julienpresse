import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


file_path = 'video_games.csv'
data = pd.read_csv(file_path)
data_head = data.head()
print(data_head)

data_info = data.info()
print(data_info)

column_names = data.columns
print(column_names)

missing_percentage = (data.isnull().mean() * 100)
print(missing_percentage)

missing_count = data.isnull().sum()
print(missing_count)

numerical_data = data.select_dtypes(include='number')
column_names = numerical_data.columns
print(column_names)

columns_to_remove = ['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating']
data = data.drop(columns=columns_to_remove)
numerical_data = data.select_dtypes(include='number')
column_names = numerical_data.columns

correlation_matrix = numerical_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap of Numerical Values')
plt.show()
