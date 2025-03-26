from modulos.archivo_json import cargar_datos, guardar_datos

GENEROS_JSON = "data/generos.json"

def agregar_genero():
    generos = cargar_datos(GENEROS_JSON)

    id_genero = input("Escriba el ID del género: ").strip()
    descripcion = input("EScriba la descripción del genero: ").strip()

    nuevo_genero = {"ID": id_genero, "Description": descripcion}

    generos.append(nuevo_genero)
    guardar_datos(GENEROS_JSON, generos)
    print("Se agregó el genero correctamente.")

def mostrar_generos():
    generos = cargar_datos(GENEROS_JSON)
    
    if not generos:
        print("No hay géneros registrados.")
        return

    print("LISTA DE GENEROS MUSICALES:")
    for genero in generos:
        print(f"- {genero['ID']}: {genero['Description']}")

def editar_genero():
   
    generos = cargar_datos(GENEROS_JSON)

    id_genero = input("Ingrese el ID del género a editar: ").strip()
    genero = next((g for g in generos if g["ID"] == id_genero), None)

    if not genero:
        print("El genero no se econtró.")
        return

    genero["Description"] = input(f"Nueva descripción ({genero['Description']}): ").strip() or genero["Description"]

    guardar_datos(GENEROS_JSON, generos)
    print("EL genero se editó correctamente.")

def eliminar_genero():
    generos = cargar_datos(GENEROS_JSON)

    id_genero = input("Escriba el ID del género que quiere eliminar: ").strip()
    generos_filtrados = [g for g in generos if g["ID"] != id_genero]

    if len(generos) == len(generos_filtrados):
        print("EL genero no se encontró.")
        return

    guardar_datos(GENEROS_JSON, generos_filtrados)
    print("Se eliminó correctamente el gnero")
