# Definición de la función para saludar
def saludar(nombre):
    print("Hola,", nombre)

# Definición de la función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Definición de la función para imprimir un mensaje de despedida
def despedirse():
    print("¡Hasta luego!")

# Llamando a la función para saludar
saludar("Juan")

# Llamando a la función para calcular el área de un rectángulo
base_rectangulo = 5
altura_rectangulo = 3
area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
print("El área del rectángulo es:", area_rectangulo)

# Llamando a la función para despedirse
despedirse()
