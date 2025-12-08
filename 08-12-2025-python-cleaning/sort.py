import pandas as pd
data = pd.read_csv('./lotr_characters.csv')

df=pd.DataFrame(data)
df["race"] = df["race"].str.lower()
print(df[['race']])