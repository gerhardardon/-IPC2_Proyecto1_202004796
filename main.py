import webbrowser

from pisos import node, lista_color
from cantidad import node, lista_cant
from nombre import nodo, lista_nombre
from tkinter import Tk
from tkinter import filedialog as fd
from xml.dom import minidom
from os import system, startfile

mydoc = ""
lnom=""
lcant=""
lcol=""
row_inicio=""
column_inicio=""


class bcolor:
    morado = "\033[1;35m"
    reset = '\033[0m'


def llenar_listas():
    global lnom,lcant,lcol ########### PROBAR VAR GLOBALES
    piso = mydoc.getElementsByTagName('piso')  # Obtenemos los nodos con el tag 'patron'
    # print('Cantidad de elementos del xml:')
    # print(len(piso)) # Ya tenemos la cantidad de items

    i = 0
    lnom = lista_nombre()  # Creamos la lista PINCIPAL

    while i < len(piso):
        name = piso[i].attributes['nombre'].value
        row = piso[i].getElementsByTagName('R')[0].firstChild.data
        column = piso[i].getElementsByTagName('C')[0].firstChild.data
        f = piso[i].getElementsByTagName('F')[0].firstChild.data
        s = piso[i].getElementsByTagName('S')[0].firstChild.data

        lcan = lista_cant()  # Creamos lista Cantidad

        j = 0

        pat = piso[i].getElementsByTagName('patron')
        while j < len(pat):  # Recorre la cant de patron
            lcol = lista_color()  # Creamos lista Color

            # 'pat[j].firstChild.data'  codigos de colores
            for x in pat[j].firstChild.data:
                lcol.agregar(x)

            #pat[j].attributes['codigo'].value Guarda el codigo del piso
            lcan.agregar(pat[j].attributes['codigo'].value,lcol)
            #lcol.imprimir()
            j = j + 1
        i = i + 1
        #lcan.imprimir()
        lnom.agregar(name, row, column, f, s, lcan)
        #lnom.imprimir()
    print("XML cargado exitosamente! ;)")
    init()

def menu2():
    print(bcolor.morado+"Pisos INICIALES disponibles:"+bcolor.reset)
    global lnom
    lnom.getpisos()
    print("\n")
    print("Ingrese el nombre de piso que desea...")
    x = input()
    print(bcolor.morado+"\nElija un código inicial...\n"+bcolor.reset)

    global row_inicio
    row_inicio=lnom.getrow(x) # Obtiene el numero de filas para graficar
    int(row_inicio)
    global column_inicio
    column_inicio=lnom.getcolumn(x)  # Obtiene el numero de columnas para graficar
    int(column_inicio)

    lnom.buscar(x)
    codigo = input()
    code=(lnom.buscarcolor(x,codigo))
    grafica(codigo,row_inicio,column_inicio,code) # Grafica usando graphviz
    menu3()

def menu3():
    print(bcolor.morado + "Pisos FINALES disponibles:" + bcolor.reset)
    print("Recuerde que las dimensiones de piso inicial y final DEBEN SER IGUALES")
    global lnom
    lnom.getpisos()
    print("\n")
    print("Ingrese el nombre de piso que desea...")
    x = input()
    print(bcolor.morado + "\nElija un código final...\n" + bcolor.reset)

    global row_inicio
    row_inicio = lnom.getrow(x)  # Obtiene el numero de filas para graficar
    int(row_inicio)
    global column_inicio
    column_inicio = lnom.getcolumn(x)  # Obtiene el numero de columnas para graficar
    int(column_inicio)

    lnom.buscar(x)
    codigo = input()
    code = (lnom.buscarcolor(x, codigo))
    grafica(codigo,row_inicio, column_inicio, code)  # Grafica usando graphviz
    init()



def grafica(codigo,row,column,code):
    with open(codigo+'.dot', 'w') as f:
        f.write('''
        digraph {

         node [ shape=none fontname=Helvetica ]

            n [ label = <
            <table border="5" bgcolor="gray" color="white">
        ''')
        i=0
        k=0
        while i<int(row):
            f.write("<tr>")
            j=0
            while j<int(column):
                if code[k] == "W":
                    f.write('<td bgcolor="white">     </td>')
                else:
                    f.write('<td bgcolor="black">     </td>')
                k=k+1
                j=j+1
            f.write("</tr>")
            i=i+1
        f.write(''' </table>
    > ]

    }
    ''')
    try:
        system('dot -Tpng '+codigo+'.dot -o '+codigo+'.png')
        webbrowser.open_new_tab(codigo+'.png')
    except:
        print("")




def init():
    print(bcolor.morado + "\n========== MENU ==========" + bcolor.reset)
    print("Seleccione la opcion:\n   1. Cargar XML\n   2. Escoger piso inicial y final\n   3. Ver XML\n   4. Salir")
    x = input()
    if x == "1":
        print("1")
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = fd.askopenfilename(title="Select file")
        print(filename)
        global mydoc
        mydoc = minidom.parse(filename)
        llenar_listas()

    if x == "2":
        try:
            menu2()
        except:
            print("\nNo ha cargado un XML")
            init()
    if x == "3":
        print("")
        init()
    if x == "4":
        exit()
    else:
        print("\nseleccione una opcion valida")
        init()


if __name__ == '__main__':
    init()
