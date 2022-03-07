from cantidad import lista_cant
class nodo:  # LISTA 1 CON NOMBRE DE PATRONES
    def __init__(self, name, row, column, F, S, pattern, siguiente=None):
        self.name = name
        self.row = row
        self.column = column
        self.F = F
        self.S = S
        self.pattern = pattern
        self.siguiente = siguiente


class lista_nombre:
    def __init__(self):
        self.root = None  # Crea la lista con un nodo null

    def agregar(self, name, row, column, F, S, pattern):
        if self.root is None:  # si el primer nodo es null (vacio)
            self.root = nodo(name=name, row=row, column=column, F=F, S=S, pattern=pattern)
            return
        aux = self.root
        while aux.siguiente:  # busca un nodo que esté vacío
            aux = aux.siguiente
        aux.siguiente = nodo(name=name, row=row, column=column, F=F, S=S, pattern=pattern)

    def imprimir(self):
        node = self.root
        while node != None:
            print('Nodo: ', node.name, node.row, node.column, node.F, node.S)
            self.siguiente = node.siguiente
            node = self.siguiente

    def getpisos(self):
        node = self.root
        while node != None:
            print('\nPISO: ', node.name, '\nFilas:', node.row, '\nColumnas:', node.column, '\nPrecio por voltear: Q.',
                  node.S, "\nPrecio por cambiar: Q.", node.F, )
            self.siguiente = node.siguiente
            node = self.siguiente

    def buscar(self, x):
        node = self.root

        if node is None:
            print("La lista esta vacia")
            return

        while node != None:
            if node.name == x:

                node.pattern.imprimir()
                break
            self.siguiente=node.siguiente
            node=self.siguiente

    def getrow(self, x):
        node = self.root

        if node is None:
            print("La lista esta vacia")
            return

        while node != None:
            if node.name == x:
                return node.row


            self.siguiente = node.siguiente
            node = self.siguiente

    def getcolumn(self, x):
        node = self.root

        if node is None:
            print("La lista esta vacia")
            return

        while node != None:
            if node.name == x:
                return node.column


            self.siguiente = node.siguiente
            node = self.siguiente

    def buscarcolor(self, x,y):
        node = self.root

        if node is None:
            print("La lista esta vacia")
            return

        while node != None:
            if node.name == x:
                x= node.pattern.buscar(y)
                return x
            self.siguiente = node.siguiente
            node = self.siguiente