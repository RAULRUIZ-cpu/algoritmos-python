"""
11. Estadística de edades por rangos: En una encuesta aplicada a 𝑁 personas, se
registra la edad de cada participante. Clasifica y cuenta cuántas personas son niños
(0-12 años), adolescentes (13-17 años), adultos (18-59 años) y adultos mayores (60
años o más).
"""
n = int(input("¿Cuántas personas fueron encuestadas? "))

ninos = 0
adolescentes = 0
adultos = 0
adultos_mayores = 0

# Clasificar cada edad
for i in range(1, n + 1):
    edad = int(input(f"Persona {i} - Edad: "))
    if edad <= 12:
        ninos += 1
    elif edad <= 17:
        adolescentes += 1
    elif edad <= 59:
        adultos += 1
    else:
        adultos_mayores += 1

# Reporte
print(f"Niños (0-12)      : {ninos}")
print(f"Adolescentes (13-17): {adolescentes}")
print(f"Adultos (18-59)   : {adultos}")
print(f"Adultos mayores (60+): {adultos_mayores}")
print(f"TOTAL ENCUESTADOS : {n}")
