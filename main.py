from modulos.artistas import agregar_artista, editar_artista, eliminar_artista, mostrar_artistas
from modulos.paises import agregar_pais, editar_pais, eliminar_pais, mostrar_paises
from modulos.generos import agregar_genero, editar_genero, eliminar_genero, mostrar_generos
from modulos.reportes import artistas_por_pais_y_tiempo, artistas_por_genero, artistas_ultimos_10_años



def mostrar_menu():
    print("*****BIENVENIDO*****")
    while True:
        print("\n🎶 --- Menú Principal --- 🎶")
        print("1. Agregar Artista")
        print("2. Mostrar Artistas")
        print("3. Editar Artista")
        print("4. Eliminar Artista")
        print("5. Agregar País")
        print("6. Mostrar Países")
        print("7. Editar País")
        print("8. Eliminar País")
        print("9. Agregar Género")
        print("10. Mostrar Géneros")
        print("11. Editar Género")
        print("12. Eliminar Género")
        print("13. Reporte: Artistas Últimos 10 Años")
        print("14. Reporte: Número de Artistas por Año")
        print("15. Reporte: Unidades Certificadas en 2023")
        print("16. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_artista()
        elif opcion == "3":
            editar_artista()
        elif opcion == "4":
            eliminar_artista()
        elif opcion == "7":
            editar_pais()
        elif opcion == "8":
            eliminar_pais()
        elif opcion == "9":
            editar_genero()
        elif opcion == "10":
            eliminar_genero()
        elif opcion == "11":
            artistas_ultimos_10_años()
        elif opcion == "12":
            artistas_por_pais_y_tiempo("United Kingdom", 1960, 1970)
        elif opcion == "13":
            artistas_por_genero("Rock/pop")
        elif opcion == "14":
            print("Salir")
            break
        else:
            print("La opcion es invalida.")

if __name__ == "__main__":
    mostrar_menu()
