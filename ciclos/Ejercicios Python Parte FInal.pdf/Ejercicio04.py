"""
4. Plan de ahorro mensual con meta variable: Una persona desea ahorrar dinero mes a
mes durante un año. Al final de cada mes ingresa el monto depositado. El programa
debe mostrar el acumulado mes tras mes y, al finalizar los 12 meses, indicar si logró
superar una meta fija de $12,000 y por cuánto la superó o cuánto le faltó.
"""
meta = 12000.0
acumulado = 0.0

# Se hace un ciclo de los 12 meses
for mes in range(1, 13):
    deposito = float(input(f"Mes {mes} - Monto a depositar: $"))
    acumulado += deposito
    print(f"  Acumulado al mes {mes}: ${acumulado:.2f}")

# Evaluar meta
diferencia = acumulado - meta
if diferencia >= 0:
    print(f"¡Meta alcanzada! Acumulaste ${acumulado:.2f} (Superaste por ${diferencia:.2f})")
else:
    print(f"No se alcanzó la meta. Acumulaste ${acumulado:.2f} (Te faltaron ${-diferencia:.2f})")
