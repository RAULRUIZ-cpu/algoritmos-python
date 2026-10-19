contador_pares = 0

print("Números pares del 1 al 20:")
print("-" * 30)

for numero in range(1, 21):
    
    if numero % 2 == 0:
        print(numero)
        contador_pares += 1  

print("-" * 30)
print(f"Total de números pares encontrados: {contador_pares}")
