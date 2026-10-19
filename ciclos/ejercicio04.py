n = int(input("¿Cuántos números deseas ingresar? "))

suma_total = 0


for i in range(1, n + 1):
    numero = int(input(f"Ingresa el número {i}: "))
    suma_total += numero


print(f"\nLa suma total de los {n} números es: {suma_total}")
