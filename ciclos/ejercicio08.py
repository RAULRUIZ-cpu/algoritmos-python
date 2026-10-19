# Revisa la entrada de peso de 10 maletas en un ciclo y cuenta cuántas superan el límite de 23 kg.
# Inicializamos el contador
contador_exceso = 0
LIMITE = 23  # Límite de peso en kg

print("Control de peso de maletas (Límite: 23 kg)")
print("-" * 45)

# Revisamos las 10 maletas
for i in range(1, 11):
    peso = float(input(f"Ingresa el peso de la maleta {i} (kg): "))
    
    if peso > LIMITE:
        print(f"  ⚠️  Maleta {i}: EXCEDE el límite ({peso} kg)")
        contador_exceso += 1
    else:
        print(f"  ✅ Maleta {i}: Correcto ({peso} kg)")

print("-" * 45)
print(f"Total de maletas que superan el límite: {contador_exceso}")
