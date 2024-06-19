import pandas as pd
df = pd.read_csv('c:\_py_projects\students.csv')

#12 позиция, столбец Рост
print(df.iloc[[12]]['Growth'])

#ищем 18 с конца запись
print(df.iloc[len(df)-18,1])