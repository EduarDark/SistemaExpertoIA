# Base de Conocimientos
conocimientos = {
    "1": {
        "a": "Debe acudir al INRA para resolver conflictos sobre tierras comunales.",
        "b": "Puede denunciar el uso de títulos ilegales ante la ABT.",
        "c": "Consulte un abogado especializado para mediar en uso indebido de tierras.",
    },
    "2": {
        "a": "Tiene derecho a solicitar una copia de su contrato firmado por ambas partes.",
        "b": "Debe presentar una denuncia en el Ministerio de Trabajo por despido injustificado.",
        "c": "Puede reclamar el pago de beneficios sociales atrasados ante la autoridad laboral.",
    },
    "3": {
        "a": "Debe dirigirse al SEGIP para renovar o solicitar su cédula de identidad.",
        "b": "Puede realizar el trámite en el SERECI de su localidad.",
        "c": "Para registrar un título de propiedad, acuda a Derechos Reales.",
    },
}

# Archivo para guardar el historial
HISTORIAL_FILE = "historial.txt"

# Funciones principales
def mostrar_menu_principal():
    print("\n=== Guía Legal Personalizada ===")
    print("1. Consultar por área")
    print("2. Buscar por palabras clave")
    print("3. Ver historial de consultas")
    print("4. Salir")
    return input("Ingrese el número de su elección: ")

def mostrar_opciones(area):
    opciones = conocimientos.get(area)
    if opciones:
        print("\nSeleccione su caso específico:")
        for clave, descripcion in opciones.items():
            print(f"{clave}. {descripcion}")
        print("x. Volver al menú principal")
    else:
        print("\nÁrea no válida. Por favor, intente nuevamente.")
    return opciones

def obtener_respuesta(area, caso):
    return conocimientos.get(area, {}).get(caso, "Opción no válida. Por favor, intente nuevamente.")

def guardar_consulta(area, caso, respuesta):
    with open(HISTORIAL_FILE, "a") as file:
        file.write(f"Área {area}, Caso {caso}:\n{respuesta}\n{'-' * 50}\n")

def mostrar_historial():
    try:
        with open(HISTORIAL_FILE, "r") as file:
            contenido = file.read().strip()
        if contenido:
            print("\n=== Historial de Consultas ===")
            print(contenido)
        else:
            print("\nNo hay historial disponible.")
    except FileNotFoundError:
        print("\nNo hay historial disponible.")

def buscar_por_palabra_clave():
    palabra = input("\nIngrese una palabra clave para buscar: ").strip().lower()
    resultados = [
        descripcion
        for area in conocimientos.values()
        for descripcion in area.values()
        if palabra in descripcion.lower()
    ]
    if resultados:
        print("\n=== Resultados encontrados ===")
        for res in resultados:
            print(f"- {res}")
    else:
        print("No se encontraron resultados para su búsqueda.")

# Validación de entrada para números
def entrada_numerica_valida(prompt, opciones_validas):
    entrada = input(prompt).strip()
    while entrada not in opciones_validas:
        print("Entrada no válida. Intente nuevamente.")
        entrada = input(prompt).strip()
    return entrada

# Menú principal
def main():
    while True:
        opcion = entrada_numerica_valida(mostrar_menu_principal(), ["1", "2", "3", "4"])
        if opcion == "1":
            print("\nSeleccione el área de su consulta:")
            print("1. Disputas Agrarias")
            print("2. Derechos Laborales")
            print("3. Trámites Legales")
            area = entrada_numerica_valida("Ingrese el número del área: ", ["1", "2", "3"])
            opciones = mostrar_opciones(area)
            if opciones:
                caso = input("Ingrese la letra de su elección: ").strip().lower()
                if caso == "x":
                    continue
                respuesta = obtener_respuesta(area, caso)
                print("\nRespuesta:", respuesta, "\n")
                if respuesta != "Opción no válida. Por favor, intente nuevamente.":
                    guardar_consulta(area, caso, respuesta)
        elif opcion == "2":
            buscar_por_palabra_clave()
        elif opcion == "3":
            mostrar_historial()
        elif opcion == "4":
            print("\nGracias por usar la Guía Legal Personalizada. ¡Hasta luego!")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()
