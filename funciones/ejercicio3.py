"""
Un estacionamiento requiere determinar el cobro que debe aplicar a las personas que lo utilizan. Considere que el cobro es con base en las horas que lo disponen y que las fracciones de hora se toman como completas.

import math

horas = float(input("Ingresa las horas utilizadas: "))
precio_hora = float(input("Ingresa el precio por hora: "))

horas_cobradas = math.ceil(horas)
total = horas_cobradas * precio_hora

print("Horas cobradas:", horas_cobradas)
print("Total a pagar: $", total)
"""
