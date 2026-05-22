import pandas as pd

data = {'Name': ['Anjali', 'Benny', 'Vishnu'],
        'Age': [25, 30, 35],
        'Marks':[80,70,90]}
df = pd.DataFrame(data)

print(df[df['Marks']>85])