tage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
preise = [32.5, 30.1, 35.8, 29.4, 33.0, 26.7, 24.9]

print("------Strompreise der Woche------")
for tag, preis in zip(tage, preise):
    print(f"{tag}: {preis}")

def durchschnitt(liste):
    gesamtsum = sum(liste)
    laenge = len(liste)
    return round(gesamtsum / laenge, 2)

def ueberschnitt(tagListe, preisListe):
    limit = durchschnitt(preisListe)
    print(f"------Preise über den Durchschnitt von {limit} €------")
    for tag, preis in zip(tagListe, preisListe):
        if preis > limit:
            print(f"{tag}: {preis}")

print(durchschnitt(preise))
ueberschnitt(tage, preise)

    