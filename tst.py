import random  # Importa el módulo random para generar números aleatorios
from hola import cabeza_de_monda

def adivina_el_numero():  # Define una función llamada adivina_el_numero()
    numero_secreto = random.randint(1, 10)  # Genera un número aleatorio entre 1 y 10 y lo asigna a la variable numero_secreto
    intentos = 0  # Inicializa una variable intentos con el valor 0. Esta variable se utilizará para contar los intentos del usuario

    print("¡Bienvenido al juego!")  # Imprime un mensaje de bienvenida
    print("Piensa en un número del 1 al 10")  # Imprime instrucciones para el usuario

    while True:  # Inicia un bucle infinito
        intento = int(input("Intenta adivinar el número: "))  # Solicita al usuario que ingrese un número y lo convierte a entero
        intentos += 1  # Incrementa el contador de intentos en cada iteración del bucle

        if intento < numero_secreto:  # Comprueba si el número ingresado es menor que el número secreto
            print("El número que estoy pensando es mayor.")  # Imprime un mensaje indicando que el número secreto es mayor

        elif intento > numero_secreto:  # Comprueba si el número ingresado es mayor que el número secreto
            print("El número que estoy pensando es menor.")  # Imprime un mensaje indicando que el número secreto es menor

        else:  # Si el número ingresado coincide con el número secreto
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")  # Imprime un mensaje de felicitaciones que incluye el número de intentos
            break  # Sale del bucle infinito

if __name__ == "__main__":  # Comprueba si el script se está ejecutando directamente como el programa principal
    cabeza_de_monda()
    adivina_el_numero()  # Llama a la función adivina_el_numero() para iniciar el juego


