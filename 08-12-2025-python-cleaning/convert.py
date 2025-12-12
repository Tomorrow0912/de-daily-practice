import pandas as pd
data = pd.read_csv('./lotr_characters.csv')

df=pd.DataFrame(data)
try:
    df['age'] = df['age'].astype(int)
except:
    print("Error: Text in age column")