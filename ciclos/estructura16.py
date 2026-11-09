"""
Validación e intentos de cobro en cajero: Un usuario intenta retirar dinero de un
cajero que solo permite hasta 3 intentos fallidos por saldo insuficiente o clave
incorrecta. Si el usuario ingresa un monto mayor a su saldo disponible (N),
descuenta un intento. El ciclo termina si el retiro es exitoso o si agota sus 3 intentos.
"""
saldo = float(input("Saldo disponible: $"))
    clave_correcta = "1234"
    intentos = 0
    retiro_exitoso = False

    # El ciclo continúa mientras queden intentos y no haya retiro exitoso.
    while intentos < 3 and not retiro_exitoso:
        clave = input("Ingresa tu clave: ")
        monto = float(input("Monto que deseas retirar: $"))

        # Una clave incorrecta o saldo insuficiente consume un intento.
        if clave != clave_correcta:
            intentos += 1
            print(f"Clave incorrecta. Intentos fallidos: {intentos}")
        elif monto > saldo:
            intentos += 1
            print(f"Saldo insuficiente. Intentos fallidos: {intentos}")
        elif monto <= 0:
            intentos += 1
            print(f"Monto no valido. Intentos fallidos: {intentos}")
        else:
            # Si los datos son correctos, se realiza el retiro.
            saldo -= monto
            retiro_exitoso = True
            print("Retiro exitoso.")

    if retiro_exitoso:
        print(f"Saldo restante: ${saldo:.2f}")
    else:
        print("Se agotaron los 3 intentos. Operacion bloqueada.")
