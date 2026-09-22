"""
“La Langosta Ahumada” es una empresa dedicada a ofrecer banquetes. Sus tarifas son las siguientes:

El costo del platillo por persona es de $95.00.
Si el número de personas es mayor a 200 pero menor o igual a 300, el costo es de $85.00.
Para más de 300 personas, el costo por platillo es de $75.00.

Se requiere un algoritmo que ayude a determinar el presupuesto que se debe presentar a los clientes que deseen realizar un evento.

personas = int(input("Ingresa el número de personas: "))

if personas > 300:
    precio_platillo = 75
elif personas > 200:
    precio_platillo = 85
else:
    precio_platillo = 95

total = personas * precio_platillo

print("Costo por persona: $", precio_platillo)
print("Presupuesto total: $", total)
"""
