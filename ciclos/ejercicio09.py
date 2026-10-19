contador_menores = 0

print("Registro de edades - Discoteca")
print("-" * 35)


for i in range(1, 9):
    edad = int(input(f"Edad de la persona {i}: "))
    if edad < 18:
        contador_menores += 1

print("-" * 35)
print(f"Total de menores de edad: {contador_menores}")
