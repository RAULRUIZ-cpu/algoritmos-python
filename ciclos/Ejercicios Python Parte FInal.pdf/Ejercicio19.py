"""
19. Sensor de nivel de depósito con alerta: Un tanque de agua de 1,000 litros recibe
descargas periódicas de agua. En cada ciclo se ingresa el volumen en litros de cada
descarga hasta que el tanque alcance o supere el 95% de su capacidad total.
Reporta cuántas descargas se necesitaron y el volumen total almacenado.
"""
capacidad_total = 1000
limite_alerta = capacidad_total * 0.95

nivel = 0  # Aquí vamos sumando cuánto tiene el tanque
veces = 0  # Para contar cuántas veces le metimos agua

print("Vamos llenando el tanque poco a poco...")
# Seguimos metiendo agua hasta que llegue a la alerta
while nivel < limite_alerta:
    litros = float(input(f"¿Cuántos litros metemos en la descarga {veces + 1}? "))
    nivel += litros
    veces += 1
    # Si ya casi está lleno, avisamos
    if nivel >= limite_alerta:
        print("¡Ya está lleno lo suficiente, paramos!")

# Al final mostramos todo
print(f"Metimos agua {veces} veces")
print(f"En total hay guardados {nivel:.2f} litros")
