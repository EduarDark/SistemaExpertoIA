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
    opciones = conocimientos.get(area, {})
    if opciones:
        print("\nSeleccione su caso específico:")
        for clave, descripcion in opciones.items():
            print(f"{clave}. {descripcion}")
        print("x. Volver al menú principal")
    return opciones

def obtener_respuesta(area, caso):
    return conocimientos.get(area, {}).get(caso, "Opción no válida. Por favor, intente nuevamente.")

def guardar_consulta(area, caso, respuesta):
    with open(HISTORIAL_FILE, "a") as file:
        file.write(f"Área {area}, Caso {caso}: {respuesta}\n")

def mostrar_historial():
    try:
        with open(HISTORIAL_FILE, "r") as file:
            contenido = file.read()
        if contenido:
            print("\n=== Historial de Consultas ===")
            print(contenido)
        else:
            print("\nNo hay historial disponible.")
    except FileNotFoundError:
        print("\nNo hay historial disponible.")

def buscar_por_palabra_clave():
    palabra = input("\nIngrese una palabra clave para buscar: ").lower()
    resultados = []
    for area in conocimientos.values():
        for descripcion in area.values():
            if palabra in descripcion.lower():
                resultados.append(descripcion)
    if resultados:
        print("\nResultados encontrados:")
        for res in resultados:
            print(f"- {res}")
    else:
        print("No se encontraron resultados para su búsqueda.")

# Menú principal
def main():
    while True:
        opcion = mostrar_menu_principal()
        if opcion == "1":
            print("\nSeleccione el área de su consulta:")
            print("1. Disputas Agrarias")
            print("2. Derechos Laborales")
            print("3. Trámites Legales")
            area = input("Ingrese el número del área: ")
            opciones = mostrar_opciones(area)
            if opciones:
                caso = input("Ingrese la letra de su elección: ")
                if caso != "x":
                    respuesta = obtener_respuesta(area, caso)
                    print("\nRespuesta:", respuesta, "\n")
                    guardar_consulta(area, caso, respuesta)
            else:
                print("Área no válida. Por favor, intente nuevamente.")
        elif opcion == "2":
            buscar_por_palabra_clave()
        elif opcion == "3":
            mostrar_historial()
        elif opcion == "4":
            print("Gracias por usar la Guía Legal Personalizada. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
