n = int(input("¿Cuántos números deseas ingresar? "))


mayores_cero = 0
menores_cero = 0
iguales_cero = 0

print("\nIngresa los números:")
print("-" * 35)


for i in range(1, n + 1):
    numero = float(input(f"Número {i}: "))
    
    if numero > 0:
        mayores_cero += 1
    elif numero < 0:
        menores_cero += 1
    else:
        iguales_cero += 1


print("-" * 35)
print(f"Cantidad de números mayores que 0: {mayores_cero}")
print(f"Cantidad de números menores que 0: {menores_cero}")
print(f"Cantidad de números iguales a 0: {iguales_cero}")
