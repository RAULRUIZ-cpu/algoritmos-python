"""
Registro de temperaturas extremas y promedios: Registra las temperaturas máximas
de cada día del mes (30 días). Determina cuál fue la temperatura más alta
registrada, la más baja y calcula el promedio mensual de temperatura.
"""
suma = 0
    temperatura_mayor = None
    temperatura_menor = None

    for dia in range(1, 31):
        temperatura = float(input(f"Temperatura maxima del dia {dia}: "))
        suma += temperatura

        # La primera temperatura sirve para inicializar extremos.
        if temperatura_mayor is None or temperatura > temperatura_mayor:
            temperatura_mayor = temperatura
        if temperatura_menor is None or temperatura < temperatura_menor:
            temperatura_menor = temperatura

    promedio = suma / 30

    print(f"\nTemperatura mas alta: {temperatura_mayor:.2f}")
    print(f"Temperatura mas baja: {temperatura_menor:.2f}")
    print(f"Promedio mensual: {promedio:.2f}")
