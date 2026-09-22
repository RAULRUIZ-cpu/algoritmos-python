"""
Almacenes “El Harapiento Distinguido” tiene una promoción: a todos los trajes que tienen un precio superior a $2500.00 se les aplicará un descuento de 15%; a todos los demás se les aplicará sólo 8%.

Realice un algoritmo para determinar el precio final que debe pagar una persona por comprar un traje y de cuánto es el descuento que obtendrá.

precio = float(input("Ingresa el precio del traje: "))

if precio > 2500:
    porcentaje = 0.15
else:
    porcentaje = 0.08

descuento = precio * porcentaje
precio_final = precio - descuento

print("Descuento obtenido: $", descuento)
print("Precio final: $", precio_final)
"""
