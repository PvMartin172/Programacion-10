class Contenido:
    def __init__(self, titulo, calificacion):
        self.titulo = titulo
        self.calificacion = calificacion  # esto ya llama al setter de abajo

    @property
    def calificacion(self):
        # Usar un atributo privado
        return self._calificacion

    @calificacion.setter
    def calificacion(self, calificacion):
        if float(calificacion) < 0:
            self._calificacion = 0
        else:
            self._calificacion = float(calificacion)

    def __str__(self):
        return f"{self.titulo} (Calificación: {self.calificacion})"

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

class Pelicula(Contenido):
    def __init__(self, titulo, calificacion, duracion_minutos):
        super().__init__(titulo, calificacion)
        self.duracion_minutos = duracion_minutos

    def __str__(self):
        return f"{self.titulo}, Duración: {self.duracion_minutos}min, Calificación: {self.calificacion}"

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

class Serie(Contenido):
    def __init__(self, titulo, calificacion, temporadas):
        super().__init__(titulo, calificacion)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.titulo}, Temporadas: {self.temporadas}, Calificación: {self.calificacion}"
        
    @classmethod
    def desde_cadena(cls, texto):
        titulo, temporadas, calificacion = texto.split(',')
        return cls(titulo.strip(), float(calificacion.strip()), int(temporadas.strip()))

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
class Playlist:
    def __init__(self):
        self._contenido = []

    def agregar_contenido(self, contenido):
        self._contenido.append(contenido)

    def vaciar_playlist(self):
        self._contenido = []

    def mostrar_playlist(self):
        return self._contenido.copy()

    def ordenar_por_calificacion(self):
        _contenido_ordenado = sorted(self._contenido, key=lambda x: x.calificacion, reverse=True)
        return _contenido_ordenado

    def __len__(self):
        return len(self._contenido)

    def calcular_calificacion_promedio(self):
        if not self._contenido:
            return 0
        total = 0
        cantidad = len(self._contenido)
        for elemento in self._contenido:
            total += elemento.calificacion
        promedio = total / cantidad
        return promedio

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

# Prueba en main(casi me da una embolia haciendo esta parte, no entendia como declarar algo sin 'input')
if __name__ == "__main__":

    # 1.-------------------------------------------------------------------------

    c1 = Contenido('Mapache comiendo uvas', 5.0)
    p1 = Pelicula("Brokeback Mountain: En terreno vedado", 1.0, 167)
    #Muy buena pelicula, se la recomiendo, family friendly(es broma no lo haga)
    s1 = Serie("Karmaland", 4.9, 5)
    #Muy bueno Karmaland, aunque preferia Planeta Vegeta o Apocalipsis Minecraft

    # 2.-------------------------------------------------------------------------
    s2 = Serie.desde_cadena("Los simpsons, 2425234334, 1.2")
    #Tiene mas temporadas que la biblia

    # 3.-------------------------------------------------------------------------

    mi_playlist = Playlist()
    mi_playlist.agregar_contenido(c1)
    mi_playlist.agregar_contenido(p1)
    mi_playlist.agregar_contenido(s1)
    mi_playlist.agregar_contenido(s2)

    # 4.-------------------------------------------------------------------------

    print('--- Mostrar contenido playlist ---')
    for item in mi_playlist.mostrar_playlist():
        print(item)

    # 5.-------------------------------------------------------------------------

    print('\n--- Asignar calificación negativa (-5) a Contenido ---')
    c1.calificacion = -5
    #No se quien fue el desalmado que le puso una mala calificacion
    print(c1)

    # 6.-------------------------------------------------------------------------

    print('\n--- Lista ordenada por calificación (Mayor a menor) ---')
    for item in mi_playlist.ordenar_por_calificacion():
        print(item)

    # 7.-------------------------------------------------------------------------

    print('\n--- Calcular calificación promedio ---')
    print(f"{mi_playlist.calcular_calificacion_promedio():.2f}")

    # 8.-------------------------------------------------------------------------

    print('\n--- Vaciar lista ---')
    mi_playlist.vaciar_playlist()
    print(f"Elementos en la playlist: {len(mi_playlist)}")

#Profe de tips para que el codigo se vea mas ordenado
#Esta vara pareciera que es el codigo de Undertale o Balatro
