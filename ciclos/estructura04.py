"""
Plan de ahorro mensual con meta variable: Una persona desea ahorrar dinero mes a
mes durante un año. Al final de cada mes ingresa el monto depositado. El programa
debe mostrar el acumulado mes tras mes y, al finalizar los 12 meses, indicar si logró
superar una meta fija de $12,000 y por cuánto la superó o cuánto le faltó.
"""
meta = 12000
    ahorro_acumulado = 0

    # Se solicitan los depósitos de los 12 meses.
    for mes in range(1, 13):
        deposito = float(input(f"Deposito del mes {mes}: $"))
        ahorro_acumulado += deposito
        print(f"Ahorro acumulado: ${ahorro_acumulado:.2f}")

    # Se compara el ahorro total con la meta.
    if ahorro_acumulado > meta:
        print(f"Superaste la meta por ${ahorro_acumulado - meta:.2f}.")
    elif ahorro_acumulado == meta:
        print("Llegaste exactamente a la meta de $12,000.")
    else:
        print(f"Te faltaron ${meta - ahorro_acumulado:.2f} para llegar a la meta.")
