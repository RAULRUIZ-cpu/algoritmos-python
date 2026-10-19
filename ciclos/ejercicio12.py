ahorro_total = 0

print("Plan de Ahorro Anual")
print("=" * 40)

for mes in range(1, 13):
    deposito = float(input(f"Depósito final del mes {mes} ($): "))
    ahorro_total += deposito  
    print(f"  → Ahorro acumulado al mes {mes}: ${ahorro_total:.2f}\n")

print("=" * 40)
print(f" Ahorro total al final del año: ${ahorro_total:.2f}")
