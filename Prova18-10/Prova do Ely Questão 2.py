import pandas as pd
df = pd.read_csv('train.csv')
dfield = df[df['Survived'] == 1]
print(dfield)
array_sobreviventes = df['PassengerId'].unique()
all_number = array_sobreviventes[-1]
survived_number = dfield.sum()['Survived']
percent = (survived_number / all_number) * 100

print('Porcetagem de sobreviventes: ' + str(percent))
df = df[pd.notnull(df['Embarked'])]
print(df)

pd.get_dummies(data=df, columns=df['Embarked'])