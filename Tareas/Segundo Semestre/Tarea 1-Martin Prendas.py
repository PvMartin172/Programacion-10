#Programacion tarea:
#Programacion = buena
#Errores = 0
#Nota 100%

from abc import ABC, abstractmethod


#-----------------------------------------------------------------------------------------
class Atraccion(ABC):
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self._capacidad = capacidad
        self._visitantes_actuales = 0

    @abstractmethod
    def calcular_tiempo_ciclo(self):
       
        pass

    @abstractmethod
    def verificar_restriccion(self, altura):
        pass

    def subir_visitantes(self, cantidad):
        if self._visitantes_actuales + cantidad <= self._capacidad:
            self._visitantes_actuales += cantidad
            return True
        return False

    def vaciar(self):
        self._visitantes_actuales = 0

    def cupos_disponibles(self):
        return self._capacidad - self._visitantes_actuales


#-----------------------------------------------------------------------------------------
class MontañaRusa(Atraccion):
    def __init__(self, nombre, capacidad, altura_minima):
        super().__init__(nombre, capacidad)
        self.altura_minima = altura_minima

    def calcular_tiempo_ciclo(self):
        return 3

    def verificar_restriccion(self, altura):
        return altura >= self.altura_minima


class RuedaFortuna(Atraccion):
    def __init__(self, nombre, capacidad, altura_minima):
        super().__init__(nombre, capacidad)
        self.altura_minima = altura_minima

    def calcular_tiempo_ciclo(self):
        return 10

    def verificar_restriccion(self, altura):
        return altura >= self.altura_minima


class Carrusel(Atraccion):
    def __init__(self, nombre, capacidad):
        super().__init__(nombre, capacidad)

    def calcular_tiempo_ciclo(self):
        return 5

    def verificar_restriccion(self, altura):
        return True


#-----------------------------------------------------------------------------------------
class Parque:
    def __init__(self, nombre):
        self.nombre = nombre
        self._atracciones = []

    def agregar_atraccion(self, atraccion):
        self._atracciones.append(atraccion)

    def listar_atracciones(self):
        return self._atracciones.copy()

    def buscar_atraccion(self, nombre):
        for atraccion in self._atracciones:
            if atraccion.nombre == nombre:
                return atraccion
        return None

    def atracciones_disponibles(self):
        return [a for a in self._atracciones if a.cupos_disponibles() > 0]

    def tiempo_total_recorrido(self, nombres):
        total = 0
        no_encontradas = []
        for nombre in nombres:
            atraccion = self.buscar_atraccion(nombre)
            if atraccion is not None:
                total += atraccion.calcular_tiempo_ciclo()
            else:
                no_encontradas.append(nombre)
        return total, no_encontradas

    def _nombres_registrados(self):
        return [a.nombre for a in self._atracciones]


#-----------------------------------------------------------------------------------------
def mostrar_menu():
    print("\n=== PARQUE AVENTURA PURISCAL ===")
    print("1. Ver todas las atracciones")
    print("2. Ver atracciones con cupo disponible")
    print("3. Subir visitantes a una atracción")
    print("4. Vaciar una atracción")
    print("5. Verificar restricción de altura")
    print("6. Calcular tiempo total de un recorrido")
    print("7. Salir")


def opcion_1_ver_todas(parque):
    atracciones = parque.listar_atracciones()
    print()
    for atraccion in atracciones:
        tipo = type(atraccion).__name__
        print(f"{atraccion.nombre} ({tipo}): "
              f"{atraccion._visitantes_actuales}/{atraccion._capacidad} visitantes, "
              f"ciclo de {atraccion.calcular_tiempo_ciclo()} min")


def opcion_2_cupo_disponible(parque):
    disponibles = parque.atracciones_disponibles()
    print()
    if not disponibles:
        print("Ninguna atracción tiene cupo disponible en este momento.")
        return
    for atraccion in disponibles:
        print(f"{atraccion.nombre}: {atraccion.cupos_disponibles()} cupo(s) disponible(s)")


def opcion_3_subir_visitantes(parque):
    nombre = input("Nombre de la atracción: ")
    atraccion = parque.buscar_atraccion(nombre)
    if atraccion is None:
        print(f"\nNo existe una atracción llamada '{nombre}'.")
        return

    try:
        cantidad = int(input("Cantidad de visitantes: "))
    except ValueError:
        print("\nEntrada inválida. Debe digitar un número entero.")
        return

    print()
    if atraccion.subir_visitantes(cantidad):
        print(f"{cantidad} visitante(s) subieron a {atraccion.nombre}.")
    else:
        print(f"No hay cupo suficiente. Cupos disponibles: {atraccion.cupos_disponibles()}")


def opcion_4_vaciar(parque):
    nombre = input("Nombre de la atracción: ")
    atraccion = parque.buscar_atraccion(nombre)
    print()
    if atraccion is None:
        print(f"No existe una atracción llamada '{nombre}'.")
        return
    atraccion.vaciar()
    print(f"{atraccion.nombre} fue vaciada. Cupos disponibles: {atraccion.cupos_disponibles()}")


def opcion_5_verificar_restriccion(parque):
    nombre = input("Nombre de la atracción: ")
    atraccion = parque.buscar_atraccion(nombre)
    if atraccion is None:
        print(f"\nNo existe una atracción llamada '{nombre}'.")
        return

    try:
        altura = float(input("Estatura del visitante (cm): "))
    except ValueError:
        print("\nEntrada inválida. Debe digitar un número.")
        return

    print()
    if atraccion.verificar_restriccion(altura):
        print(f"El visitante SÍ puede subir a {atraccion.nombre}.")
    else:
        print(f"El visitante NO puede subir a {atraccion.nombre}.")


def _reconstruir_nombres(entrada, nombres_registrados):
    palabras = entrada.split()
    resultado = []
    i = 0
    while i < len(palabras):
        coincidencia = None

        max_palabras = min(4, len(palabras) - i)
        for longitud in range(max_palabras, 0, -1):
            candidato = " ".join(palabras[i:i + longitud])
            if candidato in nombres_registrados:
                coincidencia = candidato
                i += longitud
                break
        if coincidencia is not None:
            resultado.append(coincidencia)
        else:

            resultado.append(palabras[i])
            i += 1
    return resultado


def opcion_6_tiempo_total(parque):
    entrada = input("Ingrese las atracciones a visitar, separadas por espacio: ")
    nombres_registrados = parque._nombres_registrados()
    nombres = _reconstruir_nombres(entrada, nombres_registrados)
    total, no_encontradas = parque.tiempo_total_recorrido(nombres)
    print()
    print(f"Tiempo total del recorrido: {total} minutos")
    if no_encontradas:
        print(f"Advertencia: no se encontraron las siguientes atracciones: {', '.join(no_encontradas)}")


#-----------------------------------------------------------------------------------------
def main():
    parque = Parque("Parque Aventura Puriscal")

    parque.agregar_atraccion(MontañaRusa("Trueno Salvaje", 8, 140))
    parque.agregar_atraccion(RuedaFortuna("Vista Central", 12, 100))
    parque.agregar_atraccion(Carrusel("Caballitos", 16))

    while True:
        mostrar_menu()
        opcion = input("\nElija una opción: ")

        if opcion == "1":
            opcion_1_ver_todas(parque)
        elif opcion == "2":
            opcion_2_cupo_disponible(parque)
        elif opcion == "3":
            opcion_3_subir_visitantes(parque)
        elif opcion == "4":
            opcion_4_vaciar(parque)
        elif opcion == "5":
            opcion_5_verificar_restriccion(parque)
        elif opcion == "6":
            opcion_6_tiempo_total(parque)
        elif opcion == "7":
            print("\n¡Gracias por visitar el Parque Aventura Puriscal! Hasta pronto.")
            break
        else:
            print("\nOpción inválida. Debe digitar un número del 1 al 7.")


if __name__ == "__main__":
    main()
