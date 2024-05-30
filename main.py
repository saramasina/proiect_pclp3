import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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

print("\n---CERINTA 2---\n")

alive = sum(df['Survived'])
dead = lin - alive
alive = alive / lin * 100
alive = "%.2f" % alive
print(f"Procent supravietuitori: {alive}%\n")

dead = dead / lin * 100
dead = "%.2f" % dead
print(f"Procent nesupravietuitori: {dead}%\n")

clasa3 = df[df['Pclass'] == 3]
alive3 = sum(clasa3['Survived'])
dead3 = lin - alive3
alive3 = alive3 / lin * 100
alive3 = "%.2f" % alive3
dead3 = dead3 / lin * 100
dead3 = "%.2f" %dead3
print("Clasa a treia:\n") 
print(f"Procent supravietuitori: {alive3}%\n")
print(f"Procent nesupravietuitori: {dead3}%\n")

clasa2 = df[df['Pclass'] == 2]
alive2 = sum(clasa2['Survived'])
dead2 = lin - alive2
alive2 = alive2 / lin * 100
alive2 = "%.2f" % alive2
dead2 = dead2 / lin * 100
dead2 = "%.2f" %dead2
print("Clasa a doua:\n") 
print(f"Procent supravietuitori: {alive2}%\n")
print(f"Procent nesupravietuitori: {dead2}%\n")

clasa1 = df[df['Pclass'] == 1]
alive1 = sum(clasa1['Survived'])
dead1 = lin - alive1
alive1 = alive1 / lin * 100
alive1 = "%.2f" % alive1
dead1 = dead1 / lin * 100
dead1 = "%.2f" %dead1
print("Clasa intai:\n") 
print(f"Procent supravietuitori: {alive1}%\n")
print(f"Procent nesupravietuitori: {dead1}%\n")

femei = df[df['Sex'] == 'female']
alivef = sum(femei['Survived'])
deadf = lin - alivef
alivef = alivef / lin * 100
alivef = "%.2f" % alivef
deadf = deadf / lin * 100
deadf = "%.2f" %deadf
print("Femei:\n") 
print(f"Procent supravietuitori: {alivef}%\n")
print(f"Procent nesupravietuitori: {deadf}%\n")

barbati = df[df['Sex'] == 'male']
aliveb = sum(barbati['Survived'])
deadb = lin - aliveb
aliveb = aliveb / lin * 100
aliveb = "%.2f" % aliveb
deadb = deadb / lin * 100
deadb = "%.2f" %deadb
print("Barbati:\n") 
print(f"Procent supravietuitori: {aliveb}%\n")
print(f"Procent nesupravietuitori: {deadb}%\n")

labels = ['C3a', 'C3n', 'C2a', 'C2n', 'C1a', 'C1n', 'Fa', 'Fn', 'Ba', 'Bn']
sizes = [13.36, 86.64, 9.76, 90.24, 15.26, 84.74, 26.15, 73.85, 12.23, 87.77]

plt.figure()
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, sizes, color='skyblue')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval}', ha='center', va='bottom')

plt.xlabel('Categorii')
plt.ylabel('Valori')
plt.title('Histograma cu valori si categorii')
plt.savefig('cerinta2.png')

print("---CERINTA 3---\n")

print("Histogramele in README\n")

plt.figure()
labels = ['Nesupravietuitori', 'Supravietuitori']
ax = df["Survived"].plot(kind = 'hist', bins = [-0.5, 0.5, 1.5], rwidth=0.2)
plt.xlim(-0.5, 1.5)
plt.xticks(ticks=[0, 1], labels=labels)
for patch in ax.patches:
    height = patch.get_height()
    ax.text(patch.get_x() + patch.get_width() / 2, height + 0.1, f'{int(height)}', ha='center', va='bottom')
plt.ylabel('Numar persoane')
plt.title('Distribuția supraviețuitorilor')
plt.savefig('Survived.png')

plt.figure()
labels = ['Clasa I', 'Clasa II', 'Clasa III']
df1 = df[df['Survived'] == 1]['Pclass']
bx = df1.plot(kind = 'hist', bins = [0.5, 1.5, 2.5, 3.5], rwidth=0.2)
plt.ylabel('Numar persoane')
plt.xlim(0.5, 3.5)
plt.title('Distribuția supraviețuitorilor dupa clasa')
for patch in bx.patches:
    height = patch.get_height()
    bx.text(patch.get_x() + patch.get_width() / 2, height + 0.1, f'{int(height)}', ha='center', va='bottom')
plt.xticks(ticks=[1, 2, 3], labels=labels, rotation=45)
plt.savefig('Pclass.png')

plt.figure()
df1 = df[df['Survived'] == 1]['Age']
cx = df1.plot(kind = 'hist')
plt.xlabel('Varsta')
plt.ylabel('Numar persoane')
plt.title('Distribuția supraviețuitorilor dupa varsta')
plt.xlim(0, 80)
plt.savefig('Age.png')

plt.figure()
df1 = df[df['Survived'] == 1]['Fare']
cx = df1.plot(kind = 'hist')
plt.xlabel('Pretul biletului')
plt.ylabel('Numar persoane')
plt.title('Distribuția supraviețuitorilor dupa pretul biletului')
plt.xlim(0, 300)
plt.savefig('Fare.png')

print("---CERINTA 4---\n")

print("Coloanele pentru care exista valori lipsa:\n")

# valori_lipsa retine coloanele si numarul de valori lipsa pentru fiecare
for sir, value in valori_lipsa.items():
    if value != 0:
        print(sir)

print("\nNumarul si proportia valorilor lipsa:\n")

for sir, value in valori_lipsa.items():
    if value != 0:
        procent = (value / lin) * 100
        print("%s: %d, %.2f%%" % (sir, value, procent))

print("\nProcentul pentru fiecare clasa:\n")

for sir, value in valori_lipsa.items():
    if value != 0:
        print(f"Coloana {sir}:")
        for survived_class in [0, 1]:
            class_count = df[df['Survived'] == survived_class][sir].isnull().sum()
            procent = class_count / value
            print(f" - Status supravietuire {survived_class}: {procent:.2%} ({class_count} valori lipsă)")

print("\n---CERINTA 5---\n")

categ1 = categ2 = categ3 = categ4 = 0

df1 = df["Age"]

for value in df1:
    if value >= 0 and value <= 20:
        categ1 += 1
    if value >= 21 and value <= 40:
        categ2 += 1
    if value >= 41 and value <= 60:
        categ3 += 1
    if value >= 61:
        categ4 += 1
print("Numarul de pasageri din fiecare categorie:\n")
print(f"Categoria 1: {categ1}, Categoria 2: {categ2}, Categoria 3: {categ3}, Categoria 4: {categ4}")

def cat_age(age):
    if age >= 0 and age <= 20:
        return 1
    elif age >= 21 and age <= 40:
        return 2
    elif age >= 41 and age <= 60:
        return 3
    elif age >= 61:
        return 4

df['Categorie varsta'] = df['Age'].apply(cat_age)

plt.figure()
labels = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4']
df1 = df['Categorie varsta']
bx = df1.plot(kind = 'hist', bins = [0.5, 1.5, 2.5, 3.5, 4.5], rwidth=0.2)
plt.ylabel('Numar persoane')
plt.xlim(0.5, 4.5)
plt.title('Categorie varsta')
for patch in bx.patches:
    height = patch.get_height()
    bx.text(patch.get_x() + patch.get_width() / 2, height + 0.1, f'{int(height)}', ha='center', va='bottom')
plt.xticks(ticks=[1, 2, 3, 4], labels=labels)
plt.savefig('Categorii_varsta.png')

print("\n---CERINTA 6---")

b_survivors = df[(df['Sex'] == 'male') & (df['Survived'] == 1)]
b_survivors = b_survivors['Categorie varsta']
categ1 = categ2 = categ3 = categ4 = 0

for value in b_survivors:
    if value == 1:
        categ1 += 1
    if value == 2:
        categ2 += 1
    if value == 3:
        categ3 += 1
    if value == 4:
        categ4 += 1

print("\nNumarul de barbati supravietuitori din fiecare categorie:\n")
print(f"Categoria 1: {categ1}, Categoria 2: {categ2}, Categoria 3: {categ3}, Categoria 4: {categ4}")

plt.figure()
labels = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4']
bx = b_survivors.plot(kind = 'hist', bins = [0.5, 1.5, 2.5, 3.5, 4.5], rwidth=0.2)
plt.ylabel('Numar persoane')
plt.xlim(0.5, 4.5)
plt.title('Categorie varsta')
for patch in bx.patches:
    height = patch.get_height()
    bx.text(patch.get_x() + patch.get_width() / 2, height + 0.1, f'{int(height)}', ha='center', va='bottom')
plt.xticks(ticks=[1, 2, 3, 4], labels=labels)
plt.savefig('Categorii_varsta_barbati.png')

print("\n---CERINTA 7---")

copii = 0

df1 = df['Age']

for value in df1:
    if value < 18:
        copii += 1

procent = copii / lin
print(f"\nProcentul de copii la bord este : {procent:.2%}")

procent_adulti = 100 - procent

plt.figure()
labels = ['Copii', 'Adulti']
bx = b_survivors.plot(kind = 'hist', bins = [0.5, 1.5, 2.5], rwidth=0.2)
plt.ylabel('Procente')
plt.xlim(0.5, 2.5)
plt.title('Supravietuire adulti vs. copii')
for patch in bx.patches:
    height = patch.get_height()
    bx.text(patch.get_x() + patch.get_width() / 2, height + 0.1, f'{int(height)}', ha='center', va='bottom')
plt.xticks(ticks=[1, 2], labels=labels)
plt.savefig('Supravietuire adulti vs. copii.png')

# ---CERINTA 8---

# numarul de vii
alive = sum(df['Survived'])
# numarul de morti
dead = lin - alive

dfsur = df[df['Survived'] == 1]['Age']
dfnot = df[df['Survived'] == 0]['Age']

# media de varsta a persoanelor supravietuitoare
sum1 = dfsur.sum()
sum1 = int(sum1 / alive)

# media de varsta a persoanelor nesupravietuitoare
sum2 = dfnot.sum()
sum2 = int(sum2 / dead)

for i in range(1, lin):
    if pd.isnull(df.loc[i, 'Age']) == 1:
        if df.at[i, 'Survived'] == 1:
            df.at[i, 'Age'] = sum1
        if df.at[i, 'Survived'] == 0:
            df.at[i, 'Age'] = sum2

dfsur = df[df['Survived'] == 1]['Embarked']
dfnot = df[df['Survived'] == 0]['Embarked']

sur_frecv = dfsur.value_counts()

cea_mai_frecv_litera_sur = sur_frecv.idxmax()

not_frecv = dfnot.value_counts()

cea_mai_frecv_litera_not = not_frecv.idxmax()

for i in range(1, lin):
    if pd.isnull(df.loc[i, 'Embarked']) == 1:
        if df.at[i, 'Survived'] == 1:
            df.at[i, 'Embarked'] = cea_mai_frecv_litera_sur
        if df.at[i, 'Survived'] == 0:
            df.at[i, 'Embarked'] = cea_mai_frecv_litera_not

df.to_csv('cerinta8.csv', index=False)

# ---CERINTA 9---

relatie_titlu_sex = {
    'Mr.': 'male',
    'Mrs.': 'female',
    'Miss': 'female',
    'Ms.': 'female',
    'Don.': 'male',
    'Rev.': 'male',
    'Master.': 'male',
    'Jonkheer.': 'male'
}

titluri = ['Mr.', 'Mrs.', 'Miss', 'Ms.', 'Rev.', 'Master.', 'Jonkheer.', 'Don.']

vect_titluri = [0] * 8

for i in range(1, lin):
    sir = df.at[i, 'Name']
    for titlu in titluri:
        if sir.find(titlu) != -1:
            break
    sex_pretins = relatie_titlu_sex.get(titlu)
    index = titluri.index(titlu)
    if sex_pretins == df.at[i, 'Sex']:
        vect_titluri[index] += 1

plt.figure()
plt.figure(figsize=(9, 9))
bars = plt.bar(titluri, vect_titluri)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{yval}', ha='center', va='bottom')

plt.ylabel('Număr de persoane')
plt.title('Numar persoane ce corespund titlurilor lor.png')
plt.savefig('Numar persoane ce corespund titlurilor lor.png')

# -------Cerinta 10--------

k_singuri = 0

for i in range(1, lin):
    nr1 = df.at[i, 'SibSp']
    nr2 = df.at[i, 'Parch']
    nr = nr1 + nr2
    if nr == 0 and df.at[i, 'Survived'] == 1:
        k_singuri += 1

alive = sum(df['Survived'])

k_nu_singuri = alive - k_singuri

vect = [k_singuri, k_nu_singuri]

labels = ['Singuri', 'Nu singuri']

plt.figure()
plt.figure(figsize=(9, 9))
bars = plt.bar(labels, vect, color=['blue', 'red'])

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{yval}', ha='center', va='bottom')

plt.ylabel('Număr de persoane')
plt.title('Supraviețuitori în funcție de starea de a fi singur pe vas')
plt.savefig('Supravietuitori in functie de rude pe vas')

df = df.head(100)

plt.figure()
plt.figure(figsize=(15, 10))
sns.catplot(data=df, x="Survived", y="Fare", hue="Pclass")
plt.xlabel('Class')
plt.ylabel('Fare')
plt.savefig('Relatia dintre clasa, tarif si starea de supravietuire')





