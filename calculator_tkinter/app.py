from tkinter import * #libreria de donde se va a ejecutar el cod, se instala en la terminal 

root = Tk() #Modulo que iniciara la ventana
root.title("calculadora gay de Jorge") #titulo de la app

display = Entry(root)#para poner numeros, display es solo una variable
display.grid(row=1, columnspan=6, sticky=W+E)#para saber donde se pondra la variable, en que fila/columna (row, column)
#stycky sirve para decirle que ancho y largo ocupara, en este caso ocupara todo


#Entonces, display.insert(i, n) inserta el número n en la posición i de la pantalla. Como i se inicia en 0, al principio se insertará el número en la primera posición de la pantalla.
i = 0 # es el espacio de donde comenzara a escribir, desde el espacio 0 que viene siendo desde el incio, i es la variable en la que se escribira


def get_numbers(n):
    display.insert(i, n)
i+=1 #Finalmente, i += 1 aumenta i en 1 después de cada inserción, lo que significa que la próxima vez que ingreses un número, se insertará en la siguiente posición en la pantalla.

def get_operation(operation):
    global i

#command: Es un parámetro que se puede pasar al crear un widget de botón en tkinter. Define la acción que se realizará cuando se haga clic en el botón. 
#lambda: lambda es una función anónima en Python que se utiliza para definir funciones simples en una sola línea. En este contexto, se utiliza para crear una función lambda que luego se asociará con el botón.
#get_numbers(1): Esto es lo que se ejecutará cuando se haga clic en el botón. get_numbers es el nombre de la función que se va a llamar, y (1) son los argumentos que se pasan a esta función. En este caso, se pasa 1 como argumento a la función get_numbers

Button(root, text="1", command=lambda:get_numbers(1)).grid(row=2, column=0)#botones
Button(root, text="2", command=lambda:get_numbers(2)).grid(row=2, column=1)#botones
Button(root, text="3", command=lambda:get_numbers(3)).grid(row=2, column=2)#botones

Button(root, text="4",command=lambda:get_numbers(4)).grid(row=3, column=0)#botones
Button(root, text="5", command=lambda:get_numbers(5)).grid(row=3, column=1)#botones
Button(root, text="6", command=lambda:get_numbers(6)).grid(row=3, column=2)#botones

Button(root, text="7", command=lambda:get_numbers(7)).grid(row=4, column=0)#botones
Button(root, text="8", command=lambda:get_numbers(8)).grid(row=4, column=1)#botones
Button(root, text="9", command=lambda:get_numbers(9)).grid(row=4, column=2)#botones

#Botones part2
Button(root, text="AC").grid(row=5, column=0)#AC es la funcion para limpiar la pantalla
Button(root, text="0", command=lambda:get_numbers(0)).grid(row=5, column=1)#numero 0
Button(root, text="%").grid(row=5, column=2)#porcentaje

#botones part3
Button(root, text="+").grid(row=2, column=3, sticky=W+E)#porcentaje
Button(root, text="-").grid(row=3, column=3, sticky=W+E)
Button(root, text="*").grid(row=4, column=3, sticky=W+E)
Button(root, text="/").grid(row=5, column=3, sticky=W+E)

#botones part3
Button(root, text="🠄").grid(row=2, column=4, sticky=W+E)
Button(root, text="exp").grid(row=3, column=4, sticky=W+E)
Button(root, text="^2").grid(row=3, column=5, sticky=W+E)
Button(root, text="(").grid(row=4, column=4, sticky=W+E)
Button(root, text=")").grid(row=4, column=5, sticky=W+E)
Button(root, text="=").grid(row=5, column=4, sticky=W+E, columnspan= 2)#columnspan hice que el = utilizara dos espacios
Button(root, text="-").grid(row=2, column=5, sticky=W+E)







root.mainloop()#indispensable para que aparezca la ventana