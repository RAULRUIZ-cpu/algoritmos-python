contador_exceso = 0
LIMITE = 23  

print("Control de peso de maletas (Límite: 23 kg)")
print("-" * 45)


for i in range(1, 11):
    peso = float(input(f"Ingresa el peso de la maleta {i} (kg): "))
    
    if peso > LIMITE:
        print(f"  ⚠️  Maleta {i}: EXCEDE el límite ({peso} kg)")
        contador_exceso += 1
    else:
        print(f"  ✅ Maleta {i}: Correcto ({peso} kg)")

print("-" * 45)
print(f"Total de maletas que superan el límite: {contador_exceso}")
