"""
Un profesor tiene un salario inicial de $1500, y recibe un
incremento de 10 % anual durante 6 años. ¿Cuál es su
salario al cabo de 6 años? ¿Qué salario ha recibido en
cada uno de los 6 años? Realice el algoritmo
"""
# Salario inicial y datos del problema
salario = 1500.0
incremento = 0.10  # 10%
años = 6

print("Evolución del salario del profesor")
print("=" * 45)
print(f"Año | Salario anual ($)")
print("-" * 45)

# Mostrar salario de cada año
for anio in range(1, años + 1):
    print(f"{anio:4} | ${salario:12.2f}")
    # Aplicar incremento para el siguiente año
    salario = salario * (1 + incremento)

print("-" * 45)
print(f"Salario al cabo de {años} años: ${salario:.2f}")
