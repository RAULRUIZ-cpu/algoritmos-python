#Pide al usuario que ingrese N númerosenteros enteros uno por uno. Al finalizar la lectura, muestra la suma total de todos los números ingresados.
# Primero pedimos cuántos números se van a ingresar
n = int(input("¿Cuántos números deseas ingresar? "))

suma_total = 0

# Pedimos los N números uno por uno
for i in range(1, n + 1):
    numero = int(input(f"Ingresa el número {i}: "))
    suma_total += numero

# Mostramos el resultado
print(f"\nLa suma total de los {n} números es: {suma_total}")
