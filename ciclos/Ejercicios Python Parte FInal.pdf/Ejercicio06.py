"""
6. Control de peso y sobrepeso en envíos: Se recibe un lote de 𝑁 paquetes. Se debe
registrar el peso de cada uno en kg. Si un paquete pesa más de 15 kg, se le aplica
un recargo de $50 de transporte. Muestra cuántos paquetes tenían sobrepeso, el
total pagado en recargos y el peso medio de todo el lote.
"""
n = int(input("¿Cuántos paquetes vas a registrar? "))

# Inicializar variables
cont_sobrepeso = 0
total_recargos = 0.0
suma_pesos = 0.0
LIMITE = 15.0
RECARGO = 50.0

# Leer cada paquete
for i in range(1, n + 1):
    peso = float(input(f"Paquete {i} - Peso en kg: "))
    suma_pesos += peso
    if peso > LIMITE:
        cont_sobrepeso += 1
        total_recargos += RECARGO
        print(f"  → Aplica recargo de ${RECARGO:.2f}")

# Calcular promedio
peso_promedio = suma_pesos / n

# Reporte final
print(f"Paquetes con sobrepeso: {cont_sobrepeso}")
print(f"Total en recargos     : ${total_recargos:.2f}")
print(f"Peso promedio del lote: {peso_promedio:.2f} kg")
