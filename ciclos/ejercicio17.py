"""
Una compañía fabrica focos de colores (verdes, blancos y
rojos). Se desea contabilizar, de un lote de N focos, el
número de focos de cada color que hay en existencia.
"""
# Pedir la cantidad total de focos en el lote
n = int(input("¿Cuántos focos hay en el lote? "))

# Inicializar contadores por color
verdes = 0
blancos = 0
rojos = 0

print("\nRegistro de colores de focos")
print("-" * 40)
print("Ingresa el color de cada foco:")
print("  v = verde | b = blanco | r = rojo")
print("-" * 40)

# Leer y clasificar cada foco
for i in range(1, n + 1):
    color = input(f"Foco {i}: ").strip().lower()
    
    if color == 'v':
        verdes += 1
    elif color == 'b':
        blancos += 1
    elif color == 'r':
        rojos += 1
    else:
        print("  Color no válido → vuelve a ingresar este foco")
        i -= 1  # Repetir esta posición

# Mostrar resumen final
print("-" * 40)
print(f"Focos verdes:   {verdes}")
print(f"Focos blancos:  {blancos}")
print(f"Focos rojos:    {rojos}")
print(f"Total focos:    {verdes + blancos + rojos}")
