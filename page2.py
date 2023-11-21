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