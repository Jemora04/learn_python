Temperatura = float(input("ingrese la temperatura a convertir:"))
escala = input("Es Farenhait(F) o Celsius (C):").lower()

if escala == "f":
    Celsius = (Temperatura - 32) * 5/9
    print(Celsius)

elif escala == "C":
    farenhait = Temperatura * 1,8 + 32 
    print(farenhait)
else:print("escala incorrecta")

86