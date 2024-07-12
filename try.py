import pandas as pd

file_path = 'data/weibo_data.xlsx' 
df = pd.read_excel(file_path)

column_name = '主持人'

value_counts = df[column_name].value_counts()

print(value_counts)