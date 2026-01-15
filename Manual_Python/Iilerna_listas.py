# Nombre: Jonathan Villamizar
# Curso: DAM 2 - Módulo Optativo
# Fecha: 12 / 11 / 2025

# Listas principales

alumnos = ["Nahuel", "Alfredo", "Sara", "Sara", "Xavi", "Nahuel", "Bianca", "Jonathan", "Biel", "Bianca"]
edades = [19, 22, 20, 23, 18, 25, 19, 21, 24, 20]
cursos = ["DAM1", "DAM2", "DAW1", "DAW2", "ASIX1", "ASIX2", "DAM2", "DAW1", "DAM1", "ASIX2"]

modulos = ["Módulo Optativo", "Android", "Proyecto", "Procesos", "Acceso a Datos", "IPO"]
profes = ["Geraldin", "Dani", "Amanda", "Lourdes", "Lourdes", "Natalia"]

matriculas = ["M001", "M002", "M003", "M004", "M005", "M006", "M007", "M008"]
sedes = ["Madrid", "Barcelona", "Lleida"]

# Requisitos funcionales

# Alta de alumno
def alta_alumno():
    print("\nAlta de alumno")
    nombre = input("Nombre del alumno: ").capitalize()
    edad = int(input("Edad: "))
    curso = input("Curso (DAM1, DAM2, DAW1, DAW2, ASIX1, ASIX2): ").upper()
    alumnos.append(nombre)
    edades.append(edad)
    cursos.append(curso)
    print(f"{nombre} añadido correctamente.")

# Baja de alumno
def baja_alumno():
    print("\nBaja de alumno")
    nombre = input("Nombre del alumno a eliminar: ").capitalize()
    if nombre in alumnos: 
        idx = alumnos.index(nombre)
        alumnos.pop(idx)
        edades.pop(idx)
        cursos.pop(idx)
        print(f"{nombre} eliminado correctamente.")
    else:
        print("No se encontró el alumno.")

# Cambio de curso
def cambio_curso():
    print("\nCambio de curso")
    nombre = input("Nombre del alumno: ").capitalize()
    try:
        idx = alumnos.index(nombre)
        nuevo_curso = input("Nuevo curso: ").upper()
        cursos[idx] = nuevo_curso
        print(f"Curso de {nombre} actualizado a {nuevo_curso}.")
    except ValueError:
        print("Alumno no encontrado.")

# Listado por curso
def listado_por_curso():
    print("\nListado por curso")
    curso = input("Curso (DAM1, DAM2, DAW1, DAW2, ASIX1, ASIX2): ").upper()
    print(f"\nAlumnos del curso {curso}:")
    encontrados = False
    for i in range(len(alumnos)):
        if cursos[i] == curso:
            print(f"- {alumnos[i]} ({edades[i]} años)")
            encontrados = True
    if not encontrados:
        print("No hay alumnos en ese curso.")
    print("Fin del listado.")

# Top edades
def top_edades():
    print("\nTop edades")
    copia = edades.copy()
    copia.sort()
    print(f"Edad mínima: {copia[0]}")
    print(f"Edad máxima: {copia[-1]}")

# Conteo de repetidos
def conteo_repetidos():
    print("\nConteo de repetidos")
    nombre = input("Nombre a contar: ").capitalize()
    repeticiones = alumnos.count(nombre)
    print(f" {nombre} aparece {repeticiones} veces.")

# Búsqueda de módulo
def busqueda_modulo():
    print("\nBúsqueda de módulo")
    nombre_modulo = input("Nombre del módulo: ").capitalize()
    try:
        idx = modulos.index(nombre_modulo)
        print(f" {nombre_modulo} → Profe: {profes[idx]}")
    except ValueError:
        print("Módulo no encontrado.")

# Unión de grupos
def union_grupos():
    print("\nUnión de grupos")
    alumnos_DAM = ["Raúl", "Marta", "Isabel"]
    alumnos_DAW = ["Tomás", "Nerea", "Julia"]
    alumnos_totales = alumnos_DAM + alumnos_DAW
    print("DAM + DAW →", alumnos_totales)

# Reverso y slicing
def reverso_y_slicing():
    print("\nReverso y slicing")
    print("Alumnos al revés:", alumnos[::-1])
    print("Primeros 5 alumnos:", alumnos[:5])

# Limpieza controlada
def limpieza_controlada():
    print("\nLimpieza controlada")
    copia = matriculas.copy()
    copia.clear()
    print("Copia vaciada:", copia)
    print("Original intacta:", matriculas)

# Resumen IILERNA
def resumen_iilerna():
    print("\nResumen IILERNA")
    print(f"Total alumnos: {len(alumnos)}")
    print(f"Total módulos: {len(modulos)}")
    print(f"Total matrículas: {len(matriculas)}")
    print(f"DAM1: {cursos.count('DAM1')} | DAM2: {cursos.count('DAM2')} | DAW1: {cursos.count('DAW1')} | DAW2: {cursos.count('DAW2')} | ASIX1: {cursos.count('ASIX1')} | ASIX2: {cursos.count('ASIX2')}")

# Profes y módulos
def profes_y_modulos():
    print("\nProfes y módulos")
    for i in range(len(modulos)):
        print(f"{profes[i]} → {modulos[i]}")

# Edades por tramo
def edades_por_tramo():
    print("\nEdades por tramo")
    menores_20 = sum(1 for e in edades if e < 20)
    entre_20_24 = sum(1 for e in edades if 20 <= e <= 24)
    mayores_25 = sum(1 for e in edades if e >= 25)
    print(f"<20 años: {menores_20} | 20–24 años: {entre_20_24} | >=25 años: {mayores_25}")

# Normalizador
def normalizador():
    print("\nNormalizador de nombres")
    for i in range(len(alumnos)):
        alumnos[i] = alumnos[i].capitalize()
    print("Todos los nombres normalizados.")

# Depurador de duplicados
def depurar_duplicados():
    print("\nDepurador de duplicados")
    sin_repetidos = []
    for a in alumnos:
        if a not in sin_repetidos:
            sin_repetidos.append(a)
    print("Lista sin repetidos:", sin_repetidos)

# Menú principal
def menu():
    while True:
        print("\nMENÚ ILERNA")
        print("1. Alta de alumno")
        print("2. Baja de alumno")
        print("3. Cambio de curso")
        print("4. Listado por curso")
        print("5. Top edades")
        print("6. Conteo de repetidos")
        print("7. Búsqueda de módulo")
        print("8. Unión de grupos")
        print("9. Reverso y slicing")
        print("10. Limpieza controlada")
        print("11. Resumen IILERNA")
        print("12. Profes y módulos")
        print("13. Edades por tramo")
        print("14. Normalizador")
        print("15. Depurar duplicados")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1": alta_alumno()
        elif opcion == "2": baja_alumno()
        elif opcion == "3": cambio_curso()
        elif opcion == "4": listado_por_curso()
        elif opcion == "5": top_edades()
        elif opcion == "6": conteo_repetidos()
        elif opcion == "7": busqueda_modulo()
        elif opcion == "8": union_grupos()
        elif opcion == "9": reverso_y_slicing()
        elif opcion == "10": limpieza_controlada()
        elif opcion == "11": resumen_iilerna()
        elif opcion == "12": profes_y_modulos()
        elif opcion == "13": edades_por_tramo()
        elif opcion == "14": normalizador()
        elif opcion == "15": depurar_duplicados()
        elif opcion == "0":
            print("¡Bye!")
            break
        else:
            print("Opción no válida. Intenta otra vez.")

# Programa principal
if __name__ == "__main__":
    menu()
