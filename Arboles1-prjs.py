#Tomás Ramírez-2251788/ Emanuel Miranda Sinning 2250913

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []   


class Arbol:

    def __init__(self):
        self.raiz = None

    def agregar_raiz(self, valor):
        self.raiz = Nodo(valor)

    def buscar(self, nodo, valor):

        if nodo is None:
            return None

        if nodo.valor == valor:
            return nodo

        for hijo in nodo.hijos:
            encontrado = self.buscar(hijo, valor)
            if encontrado:
                return encontrado

        return None

    def agregar_hijo(self, padre, valor):

        nodo_padre = self.buscar(self.raiz, padre)

        if nodo_padre:
            nuevo = Nodo(valor)
            nodo_padre.hijos.append(nuevo)
            print("Nodo agregado")
        else:
            print("No se encontró el padre")

    def peso(self, nodo):

        if nodo is None:
            return 0

        total = 1  

        for hijo in nodo.hijos:
            total += self.peso(hijo)

        return total

    def orden(self, nodo):

        if nodo is None:
            return 0

        max_hijos = len(nodo.hijos)

        for hijo in nodo.hijos:
            max_hijos = max(max_hijos, self.orden(hijo))

        return max_hijos

    def altura(self, nodo):

        if nodo is None:
            return 0

        if len(nodo.hijos) == 0:
            return 1

        alturas = []

        for hijo in nodo.hijos:
            alturas.append(self.altura(hijo))

        return 1 + max(alturas)

    def mostrar(self, nodo, nivel=0):

        if nodo is not None:
            print("  " * nivel + str(nodo.valor))

            for hijo in nodo.hijos:
                self.mostrar(hijo, nivel + 1)




arbol = Arbol()

raiz = input("Ingrese el valor de la raiz: ")
arbol.agregar_raiz(raiz)

while True:

    print("\nMENU")
    print("1 Agregar hijo")
    print("2 Mostrar arbol")
    print("3 Peso del arbol")
    print("4 Orden del arbol")
    print("5 Altura del arbol")
    print("6 Salir")

    op = input("Opcion: ")

    if op == "1":

        padre = input("Valor del nodo padre: ")
        hijo = input("Valor del nuevo nodo: ")

        arbol.agregar_hijo(padre, hijo)

    elif op == "2":

        print("\nArbol:")
        arbol.mostrar(arbol.raiz)

    elif op == "3":

        print("Peso del arbol:", arbol.peso(arbol.raiz))

    elif op == "4":

        print("Orden del arbol:", arbol.orden(arbol.raiz))

    elif op == "5":

        print("Altura del arbol:", arbol.altura(arbol.raiz))

    elif op == "6":
        break

    else:
        print("Opcion invalida")