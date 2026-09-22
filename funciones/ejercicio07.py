"""
Determina cuánto pagará finalmente una persona por un artículo equis, considerando que tiene un descuento de 20% y debe pagar 15% de IVA. Debe mostrar el precio con descuento y el precio final.

Crea un menú para que el usuario elija entre 2 productos y el que elija despliegue el nombre del producto, precio, precio con descuento y precio final.

print("----- MENÚ -----")
print("1. Producto A - $500")
print("2. Producto B - $800")

opcion = int(input("Elige un producto: "))

if opcion == 1:
    nombre = "Producto A"
    precio = 500
elif opcion == 2:
    nombre = "Producto B"
    precio = 800
else:
    print("Opción no válida")
    exit()

descuento = precio * 0.20
precio_descuento = precio - descuento

iva = precio_descuento * 0.15
precio_final = precio_descuento + iva

print("Producto:", nombre)
print("Precio original: $", precio)
print("Precio con descuento: $", precio_descuento)
print("Precio final: $", precio_final)
"""
