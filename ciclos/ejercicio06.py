n = int(input("¿Cuántos números deseas ingresar? "))

suma_pares = 0
print("\nNúmeros pares encontrados:")
print("-" * 30)

for i in range(1, n + 1):
    numero = int(input(f"Ingresa el número {i}: "))
    
    if numero % 2 == 0:
        print(f"- {numero}")
        suma_pares += numero

print("-" * 30)
print(f"Suma total de los números pares: {suma_pares}")
