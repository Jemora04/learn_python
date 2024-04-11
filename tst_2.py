import random 

def adivina_el_numero():
    numero_aleatorio = random.randint(1, 10)
    intentos = 0
 
    print("¡Bienvenido al juego!")
    print("piensa en un numero del 1 al 10")

    while True:
        intento = int(input("Ingresa un numero aleatorio "))
        intentos += 1
   
        if intento < numero_aleatorio:
           print("El numero que estoy pensando es mayor")
     
        elif intento > numero_aleatorio:
          print("El numero que estoy pensando es menor")
 
        else:
          print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
          break  
    
if __name__== "__main__":
   adivina_el_numero() 

    