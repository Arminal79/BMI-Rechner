Gewicht = float(input("Geben Sie Ihr Gewicht in kg ein: "))
Grosse = float(input("Geben Sie Ihre Größe in Metern ein: "))

Ergebnisse = Gewicht / (Grosse ** 2)

print(f"Ihr BMI beträgt: {Ergebnisse:.2f}")

if Ergebnisse < 18.5:
    print("Sie sind untergewichtig.")
elif 18.5 <= Ergebnisse <= 24.9:
    print("Sie haben Normalgewicht.")
elif 25 <= Ergebnisse <= 29.9:
    print("Sie sind übergewichtig.")
else:
    print("Sie haben Adipositas.")
