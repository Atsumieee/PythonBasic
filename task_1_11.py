Weight = input("Gib dein Gewicht in kg an: ")
Height = input("Gib deine Grösse in m an: ")

print(f"Dein BMI beträgt:{round(int(Weight) / (float(Height) * float(Height)), 2)}")