class node:  # LISTA 2 SIRVE SOLO PARA CONTENER LOS PATRONES EJ. DE CADA PATRON
    def __init__(self, data, codigo, siguiente=None):
        self.data = data
        self.codigo= codigo
        self.siguiente = siguiente


class lista_cant:
    def __init__(self):
        self.root = None

    def agregar(self, codigo, data):
        if self.root is None:
            self.root = node(codigo=codigo,data=data)
            return
        aux = self.root
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = node(codigo=codigo,data=data)

    def imprimir(self):
        node = self.root
        while node != None:
            print('Codigo: ', node.codigo)
            node = node.siguiente

    def buscar(self, y):
        node = self.root

        if node is None:
            print("La lista esta vacia")
            return

        while node != None:
            if node.codigo == y:

                x=node.data.getcolor()
                return x

            self.siguiente=node.siguiente
            node=self.siguiente