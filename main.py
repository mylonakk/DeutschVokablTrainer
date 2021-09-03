import pandas as pd

df = pd.read_excel("wortschatz.xlsx")

for index, row in df.sample(frac=1).iterrows():
    input('----------------------------')
    print(row['Übersetzung'])
    input('')
    print(row['Wort'])
    input('----------------------------')
    
    
    