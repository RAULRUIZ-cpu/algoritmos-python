"""
16. Validación e intentos de cobro en cajero: Un usuario intenta retirar dinero de un
cajero que solo permite hasta 3 intentos fallidos por saldo insuficiente o clave
incorrecta. Si el usuario ingresa un monto mayor a su saldo disponible (𝑁),
descuenta un intento. El ciclo termina si el retiro es exitoso o si agota sus 3 intentos.
"""
saldo = float(input("Ingresa tu saldo disponible: $"))
intentos = 0
MAX_INTENTOS = 3

while intentos < MAX_INTENTOS:
    monto = float(input("\nIngresa el monto a retirar: $"))
    
    if monto > saldo:
        intentos += 1
        restantes = MAX_INTENTOS - intentos
        if restantes > 0:
            print(f"Saldo insuficiente. Te quedan {restantes} intentos")
        else:
            print("Se agotaron tus 3 intentos. Operación cancelada.")
    else:
        saldo -= monto
        print(f"¡Retiro exitoso! Retiraste ${monto:.2f}")
        print(f"Saldo restante: ${saldo:.2f}")
        break
