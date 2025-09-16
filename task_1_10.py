Distance = input("Gib dein geplante Reisedistanz in km an: ")
Speed = input("Gib deine durchschnittliche Reisegeschwindigkeit in km/h an: ")
Fuel = input("Gib deinen durchschnittlichen Benzinverbrauch in l/100km an: ")

print(f"Die geplante Reisedauer beträgt {round((int(Distance) / int(Speed))*60, 2)} Minuten")
print(f"Der geschätzte Benzinverbrauch beträgt {round((int(Distance) * int(Fuel)) / 100, 2)} Liter")