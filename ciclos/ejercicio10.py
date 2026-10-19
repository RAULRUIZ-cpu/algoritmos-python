contador_exceso = 0
LIMITE_KG = 23

print("Verificación de peso - 10 maletas")
print(f"Límite permitido: {LIMITE_KG} kg")
print("-" * 40)

for i in range(1, 11):
    peso = float(input(f"Peso maleta {i} (kg): "))
    if peso > LIMITE_KG:
        contador_exceso += 1

print("-" * 40)
print(f"Maletas que superan el límite: {contador_exceso}")
