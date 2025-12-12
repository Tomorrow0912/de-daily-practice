import pandas as pd
data = pd.read_csv('./cleaned_lotr_characters.csv')

df=pd.DataFrame(data)

df['is_elf'] = df["race"] =="elf"
print(df)