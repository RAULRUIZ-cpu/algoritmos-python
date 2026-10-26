"""
Inversión con interés compuesto anual: Un inversionista inicia con un capital inicial
de $2,000 y recibe un rendimiento del 8% anual acumulado durante 𝑁 años. Genera
un reporte que muestre el capital ganado en cada uno de los años y el saldo final
acumulado al terminar el periodo.
"""
# Definir el capital inicial
capital = 2000

# Pedir la cantidad de años
n = int(input("Cantidad de años: "))

# Calcular el rendimiento de cada año
for anio in range(1, n + 1):
    interes = capital * 0.08
    capital += interes

    # Mostrar el interés ganado y el saldo
    print("Año:", anio)
    print("Capital ganado: $", round(interes, 2))
    print("Saldo acumulado: $", round(capital, 2))

# Mostrar el saldo final
print("Saldo final: $", round(capital, 2))
