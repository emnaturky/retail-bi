

import pandas as pd

df = pd.read_excel("Online Retail.xlsx")

print("Les 5 premières lignes :")
print(df.head())

print("Nombre de lignes et colonnes :")
print(df.shape)

print("Noms des colonnes :")
print(df.columns.tolist())

print("Valeurs manquantes :")
print(df.isnull().sum())

print("Nombre de lignes dupliquées :")
print(df.duplicated().sum())

print("Quantités négatives ou nulles :")
print((df["Quantity"] <= 0).sum())

print("Prix négatifs ou nuls :")
print((df["UnitPrice"] <= 0).sum())

# Créer une copie avec les ventes valides
df_ventes = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
].copy()

print("Nombre de ventes après filtrage :")
print(len(df_ventes))

# Calculer le montant de chaque vente
df_ventes["TotalPrice"] = df_ventes["Quantity"] * df_ventes["UnitPrice"]

# Calculer le chiffre d'affaires total
chiffre_affaires = df_ventes["TotalPrice"].sum()

print("Chiffre d'affaires total :")
print(chiffre_affaires)

import matplotlib.pyplot as plt

ventes_par_pays = df_ventes.groupby("Country")["TotalPrice"].sum()

top5 = ventes_par_pays.nlargest(5)

top5.plot(kind="bar")

plt.title("Top 5 des pays par chiffre d'affaires")
plt.xlabel("Pays")
plt.ylabel("Chiffre d'affaires")

plt.tight_layout()
plt.savefig("ventes_par_pays.png")
plt.close()
# Top 5 des pays sans le Royaume-Uni
sans_uk = ventes_par_pays.drop("United Kingdom")

top5_sans_uk = sans_uk.nlargest(5)

top5_sans_uk.plot(kind="bar")

plt.title("Top 5 des pays hors Royaume-Uni")
plt.xlabel("Pays")
plt.ylabel("Chiffre d'affaires")

plt.tight_layout()
plt.close()
# Top 5 des pays sans le Royaume-Uni
sans_uk = ventes_par_pays.drop("United Kingdom")

top5_sans_uk = sans_uk.nlargest(5)

top5_sans_uk.plot(kind="bar")

plt.title("Top 5 des pays hors Royaume-Uni")
plt.xlabel("Pays")
plt.ylabel("Chiffre d'affaires")

plt.tight_layout()
plt.close()
# Top 5 des pays sans le Royaume-Uni
sans_uk = ventes_par_pays.drop("United Kingdom")

top5_sans_uk = sans_uk.nlargest(5)

top5_sans_uk.plot(kind="bar")

plt.title("Top 5 des pays hors Royaume-Uni")
plt.xlabel("Pays")
plt.ylabel("Chiffre d'affaires")

plt.tight_layout()
plt.savefig("top5_sans_uk.png")