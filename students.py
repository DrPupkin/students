import pandas as pd
df = pd.read_csv('c:\_py_projects\students\students.csv')

#12 позиция, столбец Рост
#print(df.iloc[[12]]['Growth'])

#ищем 18 с конца запись
#print(df.iloc[len(df)-18,1])

#2 lesson
print(df.info())
#средний вес
#print(df['Rock paper scissors'].value_counts())
#print(df['Rock paper scissors'].value_counts().loc['Ножницы'])
#выбор столбца по индексу
#print(df.iloc[:,26].value_counts())
#10 по списку
#print(df[['Weight', 'Sex']].iloc[9])
#print(df[df['Weight']==df['Weight'].max()]['Growth'])
#print(df['Army'].value_counts())

army = df[df['Army']=='могут призвать']
free = df[df['Army']!='могут призвать']

#print(army['Hair length'].head())
#print(free['Hair length'].info())

#print(army['Hair length'].mean())
#print(free['Hair length'].mean())

#print(df[df.iloc[:,5]==0]['Sex'].value_counts())

#print(df['Animal'].value_counts())
#dog_lov = df[df['Animal']=='Собак']
#print(dog_lov[dog_lov['Floor number']==1]['Animal'].value_counts())

#print(df['Brother-sister'].value_counts())
#print(df[df['Brother-sister']=='нет ни брата ни сестры']['Social network duration min'].median())
#print(df[df['Brother-sister']!='нет ни брата ни сестры']['Social network duration min'].median())


print(df['Fastfood'].value_counts())
KFC_persons = df[df['Fastfood']=='KFC']['Weight'].mean()

Burger_persons = df[df['Fastfood']=='Бургер кинг']['Weight'].mean()

Mac_persons = df[df['Fastfood']=='Макдональдс (или как он там сейчас называется?)']['Weight'].mean()
print(KFC_persons - Mac_persons)

'''
d_new = pd.DataFrame([{'price': 3, 'count':8}, {'price': 4, 'count': 11}])
d_new['sum'] = d_new['price'] + d_new['count']
print(d_new.head())
'''