"""
Control de peso y sobrepeso en envíos: Se recibe un lote de N paquetes. Se debe
registrar el peso de cada uno en kg. Si un paquete pesa más de 15 kg, se le aplica
un recargo de $50 de transporte. Muestra cuántos paquetes tenían sobrepeso, el
total pagado en recargos y el peso medio de todo el lote.
"""
n = int(input("Cantidad de paquetes: "))
    paquetes_sobrepeso = 0
    total_recargos = 0
    peso_total = 0

    for i in range(1, n + 1):
        peso = float(input(f"Peso del paquete {i} en kg: "))
        peso_total += peso

        # Se aplica el recargo únicamente cuando supera los 15 kg.
        if peso > 15:
            paquetes_sobrepeso += 1
            total_recargos += 50

    # Se evita dividir entre cero si no se registraron paquetes.
    if n > 0:
        peso_promedio = peso_total / n
    else:
        peso_promedio = 0

    print(f"\nPaquetes con sobrepeso: {paquetes_sobrepeso}")
    print(f"Total pagado en recargos: ${total_recargos:.2f}")
    print(f"Peso promedio del lote: {peso_promedio:.2f} kg")
