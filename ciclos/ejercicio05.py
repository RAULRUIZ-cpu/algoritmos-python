#Crea un programa que recorra los números del 1 al 20 e imprima únicamente aquellos que sean pares, indicando al final cuántos números pares se encontraron en total.
# Inicializamos contador de pares
contador_pares = 0

print("Números pares del 1 al 20:")
print("-" * 30)

# Recorremos del 1 al 20
for numero in range(1, 21):
    # Verificamos si es par (resto de dividir entre 2 es 0)
    if numero % 2 == 0:
        print(numero)
        contador_pares += 1  # Aumentamos el contador

print("-" * 30)
print(f"Total de números pares encontrados: {contador_pares}")
