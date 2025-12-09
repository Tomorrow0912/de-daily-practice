import pandas as pd
data = pd.read_csv('./lotr_characters.csv')

df=pd.DataFrame(data)
df["race"] = df["race"].str.lower()
df["race"] = df["race"].str.strip()
df["race"] = df["race"].fillna("unknown")
#print(data)
print("this is the raw csv")
print(data)

df.to_csv('cleaned_lotr_characters.csv', index=False)

cleaned_data=pd.read_csv('./cleaned_lotr_characters.csv')

print("this is the cleaned data")
print(cleaned_data)