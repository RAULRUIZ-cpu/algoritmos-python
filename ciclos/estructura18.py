"""
Análisis de velocidad de vehículo (Multas y promedios): Un radar registra la
velocidad de 12 vehículos en una carretera donde el límite es 90 km/h. Cuenta
cuántos vehículos iban dentro del límite y cuántos cometieron infracción. De los
infractores, indica cuántos superaban los 110 km/h (multa grave).
"""
dentro_limite = 0
    infractores = 0
    multas_graves = 0

    for vehiculo in range(1, 13):
        velocidad = float(input(f"Velocidad del vehiculo {vehiculo} en km/h: "))

        if velocidad <= 90:
            dentro_limite += 1
        else:
            infractores += 1

            # Una velocidad mayor de 110 km/h se considera multa grave.
            if velocidad > 110:
                multas_graves += 1

    print(f"\nVehiculos dentro del limite: {dentro_limite}")
    print(f"Vehiculos infractores: {infractores}")
    print(f"Infractores con multa grave: {multas_graves}")
