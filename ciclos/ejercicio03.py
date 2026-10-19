#Pide al usuario que ingrese 5 números enteros uno por uno. Al finalizar la lectura, muestra la suma total de todos los números ingresados.
# Inicializamos la suma en 0
suma_total = 0

# Pedimos 5 números uno por uno
for i in range(1, 6):
    numero = int(input(f"Ingresa el número {i}: "))
    suma_total += numero  # Agregamos el número a la suma

# Mostramos el resultado final
print(f"\nLa suma total de los 5 números es: {suma_total}")
