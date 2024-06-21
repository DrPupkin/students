import pandas as pd
df = pd.read_csv('c:\_py_projects\students\students.csv')

#12 позиция, столбец Рост
print(df.iloc[[12]]['Growth'])

#ищем 18 с конца запись
print(df.iloc[len(df)-18,1])

#2 lesson
print(df.info())
#средний вес
print(df['Rock paper scissors'].value_counts())
print(df['Rock paper scissors'].value_counts().loc['Ножницы'])
#выбор столбца по индексу
print(df.iloc[:,26].value_counts())
#10 по списку
print(df[['Weight', 'Sex']].iloc[9])