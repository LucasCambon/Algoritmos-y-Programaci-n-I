import random
FILAS = 4
COLUMNAS = 4
META = 2048
PIEZAS_RANDOM = (2,4,8,16,32)
TECLAS = ("w","a","s","d")

def inicializar_juego():
    juego = []
    for i in range(FILAS):
        juego.append([])
        for j in range(COLUMNAS):
            juego[i].append(0)
    fil = random.randint(0,FILAS-1)
    col = random.randint(0,COLUMNAS-1)
    juego[fil][col] = 2
    return juego

def mostrar_juego(juego):
    for i in range(len(juego)):
        for j in range(len(juego[i])):
            print("\t",juego[i][j], end="")
        print()

def juego_ganado(juego):
    for i in range(len(juego)):
        for j in range(len(juego[i])):
            if (juego[i][j] == META):
                return True
    return False

def juego_perdido(juego):
    if hay_movimientos(juego):
        return False
    for i in range(len(juego)):
        for j in range(len(juego[i])):
            if juego[i][j] == 0:
                return False
    return True

def pedir_direccion(juego):
    while True:
        direccion = input("Ingrese una dirección {}: ".format(TECLAS))
        if direccion in TECLAS:
            return direccion
            

def movimiento(juego):
    nuevo = []
    for i in range(len(juego)):
        nuevo.append([])
        for j in range(len(juego[i])):
            nuevo[i].append(juego[i][j])
    for i in range(len(nuevo)):
        for j in range(len(nuevo[i])):
            if 0 <= j+1 < len(nuevo):
                if nuevo[i][j+1] == nuevo[i][j] or nuevo[i][j+1] == 0:
                    nuevo[i][j+1] += nuevo[i][j]
                    nuevo[i][j] = 0
    for i in range(len(nuevo)):
        for j in range(len(nuevo[i])):
            if 0 <= j+1 < len(nuevo):
                if nuevo[i][j+1] == 0:
                    nuevo[i][j+1] += nuevo[i][j]
                    nuevo[i][j] = 0
    return nuevo

def trasponer(juego):
    traspuesta = []
    for i in range(len(juego[0])):
        traspuesta.append([])
        for j in range(len(juego)):
            traspuesta[i].append(juego[j][i])
    return traspuesta

def invertir(juego):
    invertida = []
    for i in range(len(juego)):
        invertida.append(juego[i][::-1])
    return invertida

def actualizar_juego(juego,dir):

    if dir == "w" or dir == "s":
        juego = trasponer(juego)
    if dir == "a" or dir == "w":
        juego = invertir(juego)
    juego = movimiento(juego)
    if dir == "a" or dir == "w":
        juego = invertir(juego)
    if dir == "w" or dir == "s":
        juego = trasponer(juego)

    return juego

def insertar_nuevo_random(nuevo_juego):
    while True:
        fil = random.randint(0,FILAS-1)
        col = random.randint(0,COLUMNAS-1)
        if (nuevo_juego[fil][col] == 0):
            nuevo_juego[fil][col] = random.choice(PIEZAS_RANDOM)
            return nuevo_juego

def hay_movimientos(juego):
    movimientos = False
    for i in range(len(juego)):
        for j in range(len(juego)-1):
            if juego[i][j] == juego[i][j+1]:
                movimientos = True
    for i in range(len(juego)-1):
        for j in range(len(juego)):
            if juego[i][j] == juego[i+1][j]:
                movimientos = True
    return movimientos
            
