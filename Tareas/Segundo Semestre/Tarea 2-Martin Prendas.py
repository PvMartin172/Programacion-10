from collections import deque

def dfs_iterativo(grafo, inicio):
    visitados = []
    pila = [inicio]
    while len(pila) > 0:
        actual = pila.pop()
        encontrado = False
        for v in visitados:
            if v == actual:
                encontrado = True
                break
        if not encontrado:
            visitados.append(actual)
            vecinos = grafo[actual]
            i = len(vecinos) - 1
            while i >= 0:
                vecino = vecinos[i]
                v_visitado = False
                for v in visitados:
                    if v == vecino:
                        v_visitado = True
                        break
                if not v_visitado:
                    pila.append(vecino)
                i = i - 1
    return visitados

def ruta_mas_corta(grafo, inicio, destino):
    if inicio == destino:
        return [inicio]
    
    cola = deque([inicio])
    visitados = [inicio]
    padres = {}
    padres[inicio] = None
    
    encontrado = False
    while len(cola) > 0:
        actual = cola.popleft()
        if actual == destino:
            encontrado = True
            break
        
        vecinos = grafo[actual]
        for vecino in vecinos:
            esta_visitado = False
            for v in visitados:
                if v == vecino:
                    esta_visitado = True
                    break
            if not esta_visitado:
                visitados.append(vecino)
                padres[vecino] = actual
                cola.append(vecino)
                
    if not encontrado:
        return None
        
    ruta = []
    actual = destino
    while actual is not None:
        ruta.append(actual)
        actual = padres[actual]
    
    ruta_invertida = []
    i = len(ruta) - 1
    while i >= 0:
        ruta_invertida.append(ruta[i])
        i = i - 1
        
    return ruta_invertida

def contar_componentes(grafo):
    visitados = []
    componentes_map = {}
    num_componentes = 0
    
    for nodo in grafo:
        encontrado = False
        for v in visitados:
            if v == nodo:
                encontrado = True
                break
        
        if not encontrado:
            num_componentes = num_componentes + 1
            pila = [nodo]
            while len(pila) > 0:
                actual = pila.pop()
                act_visitado = False
                for v in visitados:
                    if v == actual:
                        act_visitado = True
                        break
                if not act_visitado:
                    visitados.append(actual)
                    componentes_map[actual] = num_componentes
                    vecinos = grafo[actual]
                    i = len(vecinos) - 1
                    while i >= 0:
                        vecino = vecinos[i]
                        v_vis = False
                        for v in visitados:
                            if v == vecino:
                                v_vis = True
                                break
                        if not v_vis:
                            pila.append(vecino)
                        i = i - 1
    return num_componentes, componentes_map

def tiene_ciclo(grafo):
    visitados = []
    
    def dfs_ciclo(nodo, padre):
        visitados.append(nodo)
        vecinos = grafo[nodo]
        for vecino in vecinos:
            if vecino == padre:
                continue
            encontrado = False
            for v in visitados:
                if v == vecino:
                    encontrado = True
                    break
            if encontrado:
                return True
            if dfs_ciclo(vecino, nodo):
                return True
        return False

    for nodo in grafo:
        encontrado = False
        for v in visitados:
            if v == nodo:
                encontrado = True
                break
        if not encontrado:
            if dfs_ciclo(nodo, None):
                return True
    return False

def orden_topologico(grafo):
    in_degree = {}
    for nodo in grafo:
        in_degree[nodo] = 0
        
    for nodo in grafo:
        vecinos = grafo[nodo]
        for vecino in vecinos:
            if vecino in in_degree:
                in_degree[vecino] = in_degree[vecino] + 1
            else:
                in_degree[vecino] = 1
                
    cola = deque()
    for nodo in grafo:
        if in_degree[nodo] == 0:
            cola.append(nodo)
            
    orden = []
    while len(cola) > 0:
        actual = cola.popleft()
        orden.append(actual)
        vecinos = grafo[actual]
        for vecino in vecinos:
            in_degree[vecino] = in_degree[vecino] - 1
            if in_degree[vecino] == 0:
                cola.append(vecino)
                
    return orden

def main():
    red_caminos = {
        "Santiago": ["Mercedes Sur", "Barbacoas", "Candelarita"],
        "Mercedes Sur": ["Santiago", "San Rafael"],
        "Barbacoas": ["Santiago", "Grifo Alto"],
        "San Rafael": ["Mercedes Sur", "Grifo Alto"],
        "Grifo Alto": ["Barbacoas", "San Rafael"],
        "Candelarita": ["Santiago"],
        "Desamparaditos": ["Chires"],
        "Chires": ["Desamparaditos"],
        "Zapatón": []
    }

    plan_obras = {
        "Estudio": ["Permisos", "Materiales"],
        "Permisos": ["Excavación"],
        "Materiales": ["Alcantarillado", "Asfaltado"],
        "Excavación": ["Alcantarillado"],
        "Alcantarillado": ["Asfaltado"],
        "Asfaltado": ["Señalización"],
        "Señalización": []
    }

    while True:
        print("\n=== RED VIAL DE PURISCAL ===")
        print("1. Ver la red de caminos")
        print("2. Agregar un camino")
        print("3. Comunidades alcanzables desde una comunidad")
        print("4. Ruta con menos tramos entre dos comunidades")
        print("5. Componentes conexas de la red")
        print("6. Detectar caminos circulares")
        print("7. Orden de ejecución de las obras")
        print("8. Agregar un prerrequisito entre obras")
        print("9. Salir")
        
        opcion = input("Elija una opción: ").strip()
        
        if opcion == "1":
            print("\nRed de caminos de Puriscal")
            suma_grados = 0
            for comunidad in red_caminos:
                vecinos = red_caminos[comunidad]
                grado = len(vecinos)
                suma_grados = suma_grados + grado
                if grado == 0:
                    vecinos_str = "sin caminos"
                else:
                    vecinos_str = ", ".join(vecinos)
                print(comunidad + " (grado " + str(grado) + "): " + vecinos_str)
            total_caminos = suma_grados // 2
            print("Total de caminos: " + str(total_caminos))

        elif opcion == "2":
            com1 = input("Ingrese la primera comunidad: ").strip().title()
            com2 = input("Ingrese la segunda comunidad: ").strip().title()
            
            if com1 not in red_caminos or com2 not in red_caminos:
                print("Error: Una o ambas comunidades no existen en la red.")
            elif com1 == com2:
                print("Error: No se puede agregar un camino entre la misma comunidad.")
            elif com2 in red_caminos[com1]:
                print("Error: Ya existe un camino entre estas comunidades.")
            else:
                red_caminos[com1].append(com2)
                red_caminos[com2].append(com1)
                print("Camino agregado exitosamente.")

        elif opcion == "3":
            inicio = input("Ingrese la comunidad de inicio: ").strip().title()
            if inicio not in red_caminos:
                print("Error: La comunidad no existe en la red.")
            else:
                visitados = dfs_iterativo(red_caminos, inicio)
                print("Cantidad de comunidades alcanzables: " + str(len(visitados)))
                print(" -> ".join(visitados))

        elif opcion == "4":
            origen = input("Ingrese la comunidad de origen: ").strip().title()
            destino = input("Ingrese la comunidad de destino: ").strip().title()
            
            if origen not in red_caminos or destino not in red_caminos:
                print("Error: Una o ambas comunidades no existen en la red.")
            elif origen == destino:
                print("Error: El origen y el destino no pueden ser la misma comunidad.")
            else:
                ruta = ruta_mas_corta(red_caminos, origen, destino)
                if ruta is None:
                    print("Las comunidades no están comunicadas.")
                else:
                    tramos = len(ruta) - 1
                    print("Ruta: " + " -> ".join(ruta))
                    print("Cantidad de tramos: " + str(tramos))

        elif opcion == "5":
            num_comp, comp_map = contar_componentes(red_caminos)
            print("\nTotal de componentes conexas: " + str(num_comp))
            
            componentes_dict = {}
            for com in red_caminos:
                c_id = comp_map[com]
                if c_id not in componentes_dict:
                    componentes_dict[c_id] = []
                componentes_dict[c_id].append(com)
                
            for c_id in componentes_dict:
                coms = componentes_dict[c_id]
                print("Componente " + str(c_id) + ": " + ", ".join(coms))
                
            if num_comp == 1:
                print("Todas las comunidades están comunicadas entre sí.")
            else:
                print("No todas las comunidades están comunicadas entre sí.")

        elif opcion == "6":
            ciclo_dfs = tiene_ciclo(red_caminos)
            
            num_v = len(red_caminos)
            suma_grados = 0
            for com in red_caminos:
                suma_grados = suma_grados + len(red_caminos[com])
            num_e = suma_grados // 2
            num_c, _ = contar_componentes(red_caminos)
            
            sin_ciclos_conteo = (num_e == num_v - num_c)
            ciclo_conteo = not sin_ciclos_conteo
            
            print("Detección por DFS recursivo (tiene ciclo): " + str(ciclo_dfs))
            print("Detección por conteo (V=" + str(num_v) + ", E=" + str(num_e) + ", C=" + str(num_c) + "): " + str(ciclo_conteo))
            if ciclo_dfs == ciclo_conteo:
                print("Los dos métodos coinciden.")
            else:
                print("Los dos métodos NO coinciden.")

        elif opcion == "7":
            orden = orden_topologico(plan_obras)
            if len(orden) == len(plan_obras):
                print("Orden de ejecución válido:")
                print(" -> ".join(orden))
            else:
                print("Error: Los prerrequisitos forman un ciclo.")
                bloqueadas = []
                for obra in plan_obras:
                    encontrado = False
                    for o in orden:
                        if o == obra:
                            encontrado = True
                            break
                    if not encontrado:
                        bloqueadas.append(obra)
                print("Obras bloqueadas: " + ", ".join(bloqueadas))

        elif opcion == "8":
            previa = input("Ingrese la obra previa (requisito): ").strip().title()
            dependiente = input("Ingrese la obra que depende de ella: ").strip().title()
            
            if previa not in plan_obras or dependiente not in plan_obras:
                print("Error: Una o ambas obras no existen en el plan.")
            elif previa == dependiente:
                print("Error: Una obra no puede depender de sí misma.")
            elif dependiente in plan_obras[previa]:
                print("Error: La dependencia ya existe.")
            else:
                plan_obras[previa].append(dependiente)
                print("Prerrequisito agregado exitosamente.")

        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 9.")

if __name__ == "__main__":
    main()
