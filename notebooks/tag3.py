import pandas as pd

tage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
preise = [32.5, 30.1, 35.8, 29.4, 33.0, 26.7, 24.9]

df = pd.DataFrame({"tag": tage, "preis": preise})

print(df)

print(df["preis"].mean())
print(df["preis"].max())
print(df["preis"].min()) 

schnitt = df["preis"].mean()
teuer = df[df["preis"] > schnitt]
print(teuer)
laenge = len(teuer)
print(f"{laenge} sind teurer als der Durchschnitt")

schnitt = df["preis"].mean()
guenstig = df[df["preis"] < schnitt]
print(guenstig)

unter30 = df[df["preis"] < 30.0]
print(unter30)

