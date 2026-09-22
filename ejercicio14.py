"""
La política de la compañía telefónica “Chimefón” es: “Chismea + x -”.

Cuando se realiza una llamada, el cobro es por el tiempo que ésta dura:

Los primeros 5 minutos cuestan $1.00 cada uno.
Los siguientes 3 minutos cuestan $0.80 cada uno.
Los siguientes 2 minutos cuestan $0.70 cada uno.
A partir del décimo minuto, cuestan $0.50 cada uno.

Determinar cuánto debe pagar por cada concepto una persona que realiza una llamada en moneda nacional mexicana (MXN).

minutos = int(input("Ingresa la duración de la llamada: "))

costo1 = 0
costo2 = 0
costo3 = 0
costo4 = 0

if minutos <= 5:
    costo1 = minutos * 1

elif minutos <= 8:
    costo1 = 5 * 1
    costo2 = (minutos - 5) * 0.80

elif minutos <= 10:
    costo1 = 5 * 1
    costo2 = 3 * 0.80
    costo3 = (minutos - 8) * 0.70

else:
    costo1 = 5 * 1
    costo2 = 3 * 0.80
    costo3 = 2 * 0.70
    costo4 = (minutos - 10) * 0.50

total = costo1 + costo2 + costo3 + costo4

print("Primeros 5 minutos: $", costo1)
print("Siguientes 3 minutos: $", costo2)
print("Siguientes 2 minutos: $", costo3)
print("Minutos después del décimo: $", costo4)
print("Total a pagar: $", total)
"""
