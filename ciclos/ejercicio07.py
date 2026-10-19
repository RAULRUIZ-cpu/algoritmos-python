#Un sensor en la puerta de una discoteca registra la edad de 8 personas que intentan entrar. Usa un contador para determinar cuántas personas son menores de edad (menores a 18 años).
# Pedir cuántos números se van a ingresar
n = int(input("¿Cuántos números deseas ingresar? "))

suma_pares = 0
print("\nNúmeros pares encontrados:")
print("-" * 30)

# Recorrer e ingresar cada número
for i in range(1, n + 1):
    numero = int(input(f"Ingresa el número {i}: "))
    
    # Verificar si es par
    if numero % 2 == 0:
        print(f"- {numero}")
        suma_pares += numero

print("-" * 30)
print(f"Suma total de los números pares: {suma_pares}")
