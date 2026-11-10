Mango = 67

nodos = ["E", "C", "J", "R", "T", "S"]

nombres_espacios = {
    "E": "Entrada",
    "C": "Exposición de ciencias",
    "J": "Zona de juegos",
    "R": "Robótica",
    "T": "Talleres",
    "S": "Salida"
}

mapa = {
    "E": ["C", "J"],
    "C": ["E", "R", "T"],
    "J": ["E", "S"],
    "R": ["C", "S"],
    "T": ["C", "S"],
    "S": ["J", "R", "T"]
}

#-----------------------------------------------------------------

def construir_matriz(mapa_grafo, lista_nodos):
    n = len(lista_nodos)
    matriz = [[0] * n for _ in range(n)]
    indices = {nodo: i for i, nodo in enumerate(lista_nodos)}
    
    for nodo, vecinos in mapa_grafo.items():
        i = indices[nodo]
        for vecino in vecinos:
            if vecino in indices:
                j = indices[vecino]
                matriz[i][j] = 1
                
    return matriz


def dfs_recursivo(mapa_grafo, inicio):
    visitados = set()
    resultado = []
    
    def dfs(nodo):
        visitados.add(nodo)
        resultado.append(nodo)
        for vecino in mapa_grafo[nodo]:
            if vecino not in visitados:
                dfs(vecino)
                
    dfs(inicio)
    return resultado


def dfs_iterativo(mapa_grafo, inicio):
    visitados = set()
    resultado = []
    pila = [inicio]
    
    while pila:
        nodo = pila.pop()
        if nodo not in visitados:
            visitados.add(nodo)
            resultado.append(nodo)
            for vecino in reversed(mapa_grafo[nodo]):
                if vecino not in visitados:
                    pila.append(vecino)
                    
    return resultado


#---------------------------------------------------------------

def mostrar_menu():
    print("\n=== MAPA DE LA FERIA CIENTÍFICA ===")
    print("1. Ver conexiones de un espacio")
    print("2. Ver matriz de adyacencia")
    print("3. Recorrer con DFS recursivo")
    print("4. Recorrer con DFS iterativo")
    print("5. Consultar si hay un pasillo directo")
    print("6. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            nodo = input("Ingrese el espacio a consultar: ").strip().upper()
            if nodo in mapa:
                nombre = nombres_espacios[nodo]
                vecinos_str = ", ".join(mapa[nodo])
                print(f"{nodo} · {nombre} se conecta con: {vecinos_str}")
            else:
                print("Ese espacio no existe en el mapa.")
                
        elif opcion == "2":
            matriz = construir_matriz(mapa, nodos)
            print("\n  " + " ".join(nodos))
            for i, nodo in enumerate(nodos):
                fila_str = " ".join(str(val) for val in matriz[i])
                print(f"{nodo} {fila_str}")
                
        elif opcion == "3":
            inicio = input("Ingrese el nodo inicial para DFS recursivo: ").strip().upper()
            if inicio in nodos:
                resultado = dfs_recursivo(mapa, inicio)
                print(" -> ".join(resultado))
            else:
                print("Ese espacio no existe en el mapa.")
                
        elif opcion == "4":
            inicio = input("Ingrese el nodo inicial para DFS iterativo: ").strip().upper()
            if inicio in nodos:
                resultado = dfs_iterativo(mapa, inicio)
                print(" -> ".join(resultado))
            else:
                print("Ese espacio no existe en el mapa.")
                
        elif opcion == "5":
            origen = input("Ingrese el espacio de origen: ").strip().upper()
            destino = input("Ingrese el espacio de destino: ").strip().upper()
            
            if origen not in nodos or destino not in nodos:
                print("Uno o ambos espacios no existen en el mapa.")
            else:
                matriz = construir_matriz(mapa, nodos)
                idx_or = nodos.index(origen)
                idx_dest = nodos.index(destino)
                
                if matriz[idx_or][idx_dest] == 1:
                    print(f"Sí, existe un pasillo directo entre {origen} ({nombres_espacios[origen]}) y {destino} ({nombres_espacios[destino]}).")
                else:
                    print(f"No existe un pasillo directo entre {origen} ({nombres_espacios[origen]}) y {destino} ({nombres_espacios[destino]}).")
                    
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 6.")


if __name__ == "__main__":
    main()
