# Se leen tres números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
numero4 = int(input("Ingresa el cuarto número: "))
#  Asumir temporalmente que numero1 es el mayor
tamano_numero = numero1

if numero2 > tamano_numero:
    tamano_numero = numero2

if numero3 > tamano_numero:
    tamano_numero = numero3

if numero4 > tamano_numero:
    tamano_numero = numero4

print("El número más grande es:", tamano_numero)

