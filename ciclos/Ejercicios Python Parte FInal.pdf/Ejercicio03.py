"""
3. Inversión con interés compuesto anual: Un inversionista inicia con un capital inicial
de $2,000 y recibe un rendimiento del 8% anual acumulado durante 𝑁 años. Genera
un reporte que muestre el capital ganado en cada uno de los años y el saldo final
acumulado al terminar el periodo.
"""
# Datos iniciales
capital = 2000.0
tasa = 0.08
anios = int(input("¿Número de años de inversión? "))

# Acumular intereses año por año
for anio in range(1, anios + 1):
    interes = capital * tasa
    nuevo_capital = capital + interes
    print(f"{anio:4} | ${capital:13.2f} | ${interés:14.2f} | ${nuevo_capital:12.2f}")
    capital = nuevo_capital

print(f"Saldo final acumulado: ${capital:.2f}")
