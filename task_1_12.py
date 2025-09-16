Hour = input("Gib eine ganze Anzahl Stunden an: ")
Minute = input("Gib eine ganze Anzahl Minuten an: ")
Second = input("Gib eine ganze Anzahl Sekunden an: ")

print(f"Die Zeit in Stunden im metrischen System beträgt: {round(int(Hour) + (int(Minute) / 60) + (int(Second) / 3600), 2)} h")