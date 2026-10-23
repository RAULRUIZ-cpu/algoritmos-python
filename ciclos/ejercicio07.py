#Un sensor en la puerta de una discoteca registra la edad de 8 personas que intentan entrar. Usa un contador para determinar cuántas personas son menores de edad (menores a 18 años).
# Pedir cuántos números se van a ingresar
# Inicializamos el contador de menores en 0
contador_menores = 0

# Lista con las edades de las 8 personas
edades = [17, 22, 15, 18, 30, 12, 19, 16]

# Recorremos cada edad y contamos los menores de 18
for edad in edades:
    if edad < 18:
        contador_menores += 1  # Aumentamos el contador en 1

# Mostramos el resultado
print(f"Cantidad de personas menores de edad: {contador_menores}")
