
class nodo: #LISTA 1 CON NOMBRE DE PATRONES
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
        self.root = None #Crea la lista con un nodo null

    def agregar(self, name, row, column, F, S, pattern):
        if self.root is None: # si el primer nodo es null (vacio)
            self.root = nodo(name=name,row=row,column=column,F=F,S=S,pattern=pattern)
            return
        aux = self.root
        while aux.siguiente: #busca un nodo que esté vacío
            aux = aux.siguiente
        aux.siguiente = nodo(name=name,row=row,column=column,F=F,S=S,pattern=pattern)

    def imprimir( self ):
        node = self.root
        while node != None:
            print('Nodo: ',node.name,node.row,node.column,node.F,node.S,node.pattern)
            node = node.siguiente


s=lista_nombre()
s.agregar(2,2,2,2,2,2)
s.agregar(1,2,3,4,5,6)
s.imprimir()