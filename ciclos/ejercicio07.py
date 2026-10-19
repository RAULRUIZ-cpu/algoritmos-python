contador_menores = 0

print("Registro de edades - Control de acceso")
print("-" * 40)


for i in range(1, 9):
    edad = int(input(f"Ingresa la edad de la persona {i}: "))
    
    
    if edad < 18:
        contador_menores += 1

print("-" * 40)
print(f"Cantidad de menores de edad: {contador_menores}")
