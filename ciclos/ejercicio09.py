#Una discoteca tiene 8 personas registradas. Usa un contador para determinar cuántas personas son menores de edad (menores a 18 años).
# Inicializamos el contador de menores de edad
contador_menores = 0

print("Registro de edades - Discoteca")
print("-" * 35)

# Revisamos las 8 personas
for i in range(1, 9):
    edad = int(input(f"Edad de la persona {i}: "))
    if edad < 18:
        contador_menores += 1

print("-" * 35)
print(f"Total de menores de edad: {contador_menores}")
