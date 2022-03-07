class node:  # SIRVE PARA GUARDAR UN COLOR POR NODO
    def __init__(self, color, siguiente=None):
        self.color = color
        self.siguiente = siguiente


class lista_color:
    def __init__(self):
        self.root = None

    def agregar(self, color1):
        if self.root is None:
            self.root = node(color=color1)
            return
        aux = self.root
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = node(color=color1)

    def imprimir(self):
        node = self.root
        while node != None:
            print('Color: ', node.color)
            node = node.siguiente

    def getcolor(self):
        node = self.root
        x=""
        while node != None:
            x = x+ node.color
            node = node.siguiente
        return x