class node: #LISTA 2 SIRVE SOLO PARA CONTENER LOS PATRONES EJ. DE CADA PATRON
    def __init__(self, data=None, siguiente=None):
        self.data = data
        self.siguiente = siguiente

class lista_cant: 
    def __init__(self):
        self.root = None

    def agregar(self, data):
        if self.root is None:
            self.root = node(data=data)
            return
        aux = self.root
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = node(data=data)

    def imprimir( self ):
        node = self.root
        while node != None:
            print('Nodo: ',node.data)
            node = node.siguiente

