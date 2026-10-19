numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:")
print("-" * 25)

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} × {i:2} = {resultado}")
