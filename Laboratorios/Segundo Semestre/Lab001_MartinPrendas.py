from functools import reduce


def registrar_cancion(playlist):
    titulo = input("Título: ").strip()

    try:
        duracion = float(input("Duración (minutos): "))
    except ValueError:
        print("La duración debe ser un número.")
        return

    if duracion <= 0:
        print("La duración debe ser mayor que 0.")
        return

    try:
        reproducciones = int(input("Reproducciones: "))
    except ValueError:
        print("Las reproducciones deben ser un número entero.")
        return

    if reproducciones < 0:
        print("Las reproducciones no pueden ser negativas.")
        return

    playlist.append({"titulo": titulo, "duracion": duracion, "reproducciones": reproducciones})
    print(f"Canción '{titulo}' registrada.")


def ver_duracion_total(playlist):
    if not playlist:
        print("No hay canciones registradas.")
        return

    total = reduce(lambda acumulado, cancion: acumulado + cancion["duracion"], playlist, 0)
    print(f"Duración total de la playlist: {total:.2f} minutos")


def ver_modo_radio(playlist):
    if not playlist:
        print("No hay canciones registradas.")
        return

    modo_radio = map(
        lambda c: {
            "titulo": c["titulo"],
            "duracion": 3 if c["duracion"] > 3 else c["duracion"],
            "reproducciones": c["reproducciones"],
        },
        playlist,
    )

    print("\n--- Playlist en modo radio ---")
    for cancion in modo_radio:
        print(f"{cancion['titulo']}: {float(cancion['duracion'])} min")


def ver_cortas(playlist):
    if not playlist:
        print("No hay canciones registradas.")
        return

    cortas = list(filter(lambda c: c["duracion"] <= 3, playlist))

    if not cortas:
        print("No hay canciones cortas registradas.")
        return

    print("\n--- Canciones cortas ---")
    for cancion in cortas:
        print(f"{cancion['titulo']}: {cancion['duracion']} min")


def ver_si_supera_mil(playlist):
    if not playlist:
        print("No hay canciones registradas.")
        return

    supera = any(c["reproducciones"] > 1000 for c in playlist)
    print(f"¿Alguna canción supera las 1000 reproducciones? {supera}")


def ver_mas_reproducida(playlist):
    if not playlist:
        print("No hay canciones registradas.")
        return

    top = max(playlist, key=lambda c: c["reproducciones"])
    print(f"Canción más reproducida: {top['titulo']} ({top['reproducciones']} reproducciones)")


playlist = []

while True:
    print("\n=== REPRODUCTOR DE MÚSICA ===")
    print("1. Registrar canción")
    print("2. Ver duración total de la playlist")
    print("3. Ver playlist en modo radio (máximo 3 minutos por canción)")
    print("4. Ver solo las canciones cortas")
    print("5. Ver si alguna canción supera las 1000 reproducciones")
    print("6. Ver la canción más reproducida")
    print("7. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        registrar_cancion(playlist)
    elif opcion == "2":
        ver_duracion_total(playlist)
    elif opcion == "3":
        ver_modo_radio(playlist)
    elif opcion == "4":
        ver_cortas(playlist)
    elif opcion == "5":
        ver_si_supera_mil(playlist)
    elif opcion == "6":
        ver_mas_reproducida(playlist)
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
