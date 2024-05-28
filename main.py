import pandas as pd

df = pd.read_csv('train.csv')

print("\n---CERINTA 1---\n")

col = df.shape[1]
print(f"Numarul de coloane: {col}\n")

print("Tipurile datelor din fiecare coloana sunt:\n")
print(df.dtypes)
print("\n")

valori_lipsa = df.isna().sum()
print("Numar de valori lipsa pentru fiecare coloana:\n")
print(valori_lipsa)

lin = df.shape[0]
print(f"\nNumarul de linii: {lin}\n")

df1 = df.duplicated(keep='last')

ok = True
for val in df1:
    if val == True:
        ok = False

if ok == True:
    print("Nu exista linii duplicate")
else:
    print("Exista linii duplicate\n")

# print("\n---CERINTA 2---\n")



