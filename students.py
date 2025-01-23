import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('c:\_py_projects\students\students.csv')
#test
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

#army = df[df['Army']=='могут призвать']
#free = df[df['Army']!='могут призвать']

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

'''
print(df['Fastfood'].value_counts())
KFC_persons = df[df['Fastfood']=='KFC']['Weight'].mean()

Burger_persons = df[df['Fastfood']=='Бургер кинг']['Weight'].mean()

Mac_persons = df[df['Fastfood']=='Макдональдс (или как он там сейчас называется?)']['Weight'].mean()
print(KFC_persons - Mac_persons)
'''


'''
d_new = pd.DataFrame([{'price': 3, 'count':8}, {'price': 4, 'count': 11}])
d_new['sum'] = d_new['price'] + d_new['count']
print(d_new.head())
'''

#df_cut = df[['Year of birth','Growth','Weight','Hair length','Shoe size']]
#print(df_cut.sort_values(['Shoe size', 'Growth'], ascending=[False, True]).iloc[1,])
#df_cut['Full length'] = df_cut['Growth'] + df_cut['Hair length']
#print(df_cut['Full length'].max())
#корелляция
#print(df_cut.corr())
#print(df[['Russian rating','Maths rating','Rock paper scissors']].groupby('Rock paper scissors').mean())
#print(df.describe())

#sns.displot(data=df, x='Growth')
#вывод через бибоиотеку matplotlib
#plt.show()

#df1=df.dropna()
#df1=df.fillna(0)
#df=df.fillna(df.mean())
#только для количественных

#df['Weight']=df['Weight'].fillna(df['Weight'].mean()) #только для количественных
#df['Glasses'] = df['Glasses'].fillna('да')
#print(df['Glasses'].value_counts())
#print(df['Children number'].isnull().value_counts()[1])

"""
print(df['Sex'].value_counts())
males = df[df['Sex']=="мужской"]
females = df[df['Sex']=="женский"]
females['Weight'] = females['Weight'].fillna(females['Weight'].mean())
males['Weight'] = males['Weight'].fillna(males['Weight'].mean())
df_new=pd.concat([males, females])
print(df_new['Weight'].mean())
"""

"""
singles=df[df['Brother-sister']=='нет ни брата ни сестры']
sublings=df[df['Brother-sister']!='нет ни брата ни сестры']
print(singles['Children number'].median())
print(sublings['Children number'].median())
singles['Children number'] = singles['Children number'].fillna(singles['Children number'].median())
sublings['Children number'] = sublings['Children number'].fillna(sublings['Children number'].median())
df_new=pd.concat([singles, sublings])
print(df_new['Children number'].median())
"""
#выбросы и аномальные значения
sns.boxplot(df['Age'])
#вывод через бибоиотеку matplotlib
plt.show()