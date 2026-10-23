#Diseñe una aplicación que permita ingresar n números y muestre y sume los números pares.
contador = 0
print("Números pares del 1 al 20:")
for num in range(2, 21, 2):  # Empieza en 2, avanza de 2 en 2
    print(num)
    contador += 1
    suma += num
print(f"Total: {contador}")
