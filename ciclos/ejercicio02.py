#Mostrar la tabla de multiplicar de un n numero ingresado por teclado
# Pedir al usuario que ingrese un número
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
# Pedir la tabla de multiplicar de tal numero
print(f"\nTabla de multiplicar del {numero}:")
print("-" * 25)

# Generar y mostrar la tabla
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} × {i:2} = {resultado}")
