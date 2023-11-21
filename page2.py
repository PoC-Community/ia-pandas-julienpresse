import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


file_path = 'video_games.csv'
data = pd.read_csv(file_path)
data_head = data.head()
print(data_head)