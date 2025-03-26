from modulos.archivo_json import cargar_datos, guardar_datos

ARTISTAS_JSON = "data/artistas.json"

def agregar_artista():
    artistas = cargar_datos(ARTISTAS_JSON)

    nombre = input("EScriba el nombre del artista: ").strip()
    pais = input("Escriba el pais de origen: ").strip()
    años_actividad = input("Escriba el tiempo en años de actividad: ").strip()
    año_lanzamiento = input("Escriba la fecha en años del lanzamiento del primer disco: ").strip()
    genero = input("Escriba el genero musical: ").strip()
    unidades_certificadas = input("EScriba la cantidad de unidades certificadas: ").strip()
    ventas_reclamadas = input("Escriba las ventas reclamadas: ").strip()
    estado = input("Escribe si el artitas sigue activo (Sí/No): ").strip()

    nuevo_artista = {
        "Artist name": nombre,
        "Country": pais,
        "Active years": años_actividad,
        "Release year of first charted record": int(año_lanzamiento),
        "Genre": genero,
        "Total certified units": unidades_certificadas,
        "Claimed sales": ventas_reclamadas,
        "Active": estado.lower() == "sí"
    }

    artistas.append(nuevo_artista)
    guardar_datos(ARTISTAS_JSON, artistas)
    print("EL Artista se agregó correctamente.")

def mostrar_artistas():
    artistas = cargar_datos(ARTISTAS_JSON)
    
    if not artistas:
        print("No hay artistas registrados.")
        return

    print("LISTA DE ARTISTAS:")
    for artista in artistas:
        print(f"- {artista['Artist name']} ({artista['Country']}) - Género: {artista['Genre']}")

def editar_artista():
    """Permite editar un artista existente en la base de datos."""
    artistas = cargar_datos(ARTISTAS_JSON)

    nombre = input("Ingrese el nombre del artista que quiere editar: ").strip()
    artista = next((a for a in artistas if a["Artist name"].lower() == nombre.lower()), None)

    if not artista:
        print("El artista no se encontró.")
        return

    print(f"🎵 Editando artista: {artista['Artist name']}")

    artista["Country"] = input(f"Nuevo país ({artista['Country']}): ").strip() or artista["Country"]
    artista["Active years"] = input(f"Nuevos años de actividad ({artista['Active years']}): ").strip() or artista["Active years"]
    artista["Release year of first charted record"] = int(input(f"Nuevo año de lanzamiento ({artista['Release year of first charted record']}): ").strip() or artista["Release year of first charted record"])
    artista["Genre"] = input(f"Nuevo género ({artista['Genre']}): ").strip() or artista["Genre"]
    artista["Total certified units"] = input(f"Nuevas unidades certificadas ({artista['Total certified units']}): ").strip() or artista["Total certified units"]
    artista["Claimed sales"] = input(f"Nuevas ventas reclamadas ({artista['Claimed sales']}): ").strip() or artista["Claimed sales"]
    artista["Active"] = input(f"¿Sigue activo? ({'Sí' if artista['Active'] else 'No'}): ").strip().lower() == "sí"

    guardar_datos(ARTISTAS_JSON, artistas)
    print("✅ Artista editado correctamente.")

def eliminar_artista():
    artistas = cargar_datos(ARTISTAS_JSON)

    nombre = input("Ingrese el nombre del artista que quiere eliminar: ").strip()
    artistas_filtrados = [a for a in artistas if a["Artist name"].lower() != nombre.lower()]

    if len(artistas) == len(artistas_filtrados):
        print(" El artista no se encontró.")
        return

    guardar_datos(ARTISTAS_JSON, artistas_filtrados)
    print(" El artista se eliminó correctamente.")
