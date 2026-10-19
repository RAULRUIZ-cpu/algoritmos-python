# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.
# Inicializamos el ahorro acumulado
ahorro_total = 0

print("Plan de Ahorro Anual")
print("=" * 40)

# Recorremos los 12 meses del año
for mes in range(1, 13):
    deposito = float(input(f"Depósito final del mes {mes} ($): "))
    ahorro_total += deposito  # Sumamos el depósito al acumulado
    print(f"  → Ahorro acumulado al mes {mes}: ${ahorro_total:.2f}\n")

print("=" * 40)
print(f"Ahorro total al final del año: ${ahorro_total:.2f}")
