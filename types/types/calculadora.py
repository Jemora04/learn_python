n1 = input("ingresa primer numero:")
n2 = input("ingresa el segundo numero:")
n1 = int(n1)
n2 = int (n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n1

mensaje = f"""
para los numeros {n1} y {n2}
el resultado de la suma es: {suma}
el resultado de la resta es: {resta}
el resultado de la multiplicacion es: {multiplicacion}
el resultado de la divisivion es: {division}
"""
print(mensaje)