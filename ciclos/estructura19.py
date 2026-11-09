"""
Sensor de nivel de depósito con alerta: Un tanque de agua de 1,000 litros recibe
descargas periódicas de agua. En cada ciclo se ingresa el volumen en litros de cada
descarga hasta que el tanque alcance o supere el 95% de su capacidad total.
Reporta cuántas descargas se necesitaron y el volumen total almacenado.
"""
capacidad = 1000
    objetivo = capacidad * 0.95
    volumen_total = 0
    descargas = 0

    # Se reciben descargas mientras no se alcance el 95% (950 litros).
    while volumen_total < objetivo:
        volumen = float(input("Litros de la descarga: "))

        # Solo se aceptan volúmenes positivos.
        if volumen <= 0:
            print("La descarga debe ser mayor que cero.")
            continue

        volumen_total += volumen
        descargas += 1
        print(f"Volumen almacenado: {volumen_total:.2f} litros")

    print(f"\nSe necesitaron {descargas} descargas.")
    print(f"Volumen total almacenado: {volumen_total:.2f} litros")
