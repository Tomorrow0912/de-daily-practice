import pandas as pd
import sys
try:
    data = pd.read_csv('./lotr_characters.csv')
    print("file loaded successfully")
except:
    print(f"File not found")
    sys.exit(1)

df=pd.DataFrame(data)
df["race"] = df["race"].str.lower()
df["race"] = df["race"].str.strip()
df["race"] = df["race"].fillna("unknown")
#print(data)
print("this is the raw csv")
print(data)

try:
    df.to_csv('cleaned_lotr_characters.csv', index=False)
    print("cleaned data written to file")
except:
    print(f"cleaned data could not be written to file")
    sys.exit(1)

cleaned_data=pd.read_csv('./cleaned_lotr_characters.csv')

print("this is the cleaned data")
print(cleaned_data)