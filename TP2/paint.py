import gamelib
import png

### COLORES
COLORES_BASICOS = {
    (255,255,255):"#FFFFFF", 
    (0,0,0):"#000000",
    (255,0,0):"#FF0000",
    (0,255,0):"#00FF00",
    (0,0,255):"#0000FF",
    (255,255,0):"#FFFF00",
    (0,255,255):"#00FFFF",
    (255,0,255):"#FF00FF",
    (192,192,192):"#C0C0C0",
    (128,128,128):"#808080",
    (128,0,0):"#800000",
    (128,128,0):"#808000",
    }
COLORES_BOTON_AC = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"] #AC = AGREGAR COLOR


### VENTANA
TAMANIO_VENTANA_X = 200
TAMANIO_VENTANA_Y = 250

### LIENZO
TAMANIO_CELDAS = 10
PIXELES_ANCHO = 20
PIXELES_ALTO = 20
INICIO_LIENZO_X = 0
FIN_LIENZO_X = 200
INICIO_LIENZO_Y = 0
FIN_LIENZO_Y = 200

### INTERFAZ BOTONES
INICIO_INTERFAZ_BOTONES_X = 0
FIN_INTERFAZ_BOTONES_X = 200
INICIO_INTERFAZ_BOTONES_Y = 200
FIN_INTERFAZ_BOTONES_Y = 250

### BOTONES
NOMBRES_BOTONES = ["G.PPM", "C.PPM", "G.PNG"]
ANCHO_BOTONES = 50
ANCHO_BOTON_AC = 21
TAMANIO_BOTONES_COLORES = 15
ALTO_BOTONES = 15
INICIO_BOTONES_X = 10
FIN_BOTONES_X = 190
INICIO_BOTONES_Y = 205
FIN_BOTONES_Y = 240
ESPACIO_ENTRE_BOTONES_X = 3
ESPACIO_ENTRE_BOTONES_Y = 5
ESPACIO_ENTRE_BOTON_AC_X = 10

### TEXTO
POS_X_TEXTO = 26
POS_Y_TEXTO = 198

### PPM
ENCABEZADO_PPM = ["P3", (PIXELES_ANCHO, PIXELES_ALTO), "255"]

def paint_nuevo():
    '''inicializa el estado del programa con una imagen vacía de ancho x alto pixels'''
    lienzo = []
    for i in range(PIXELES_ANCHO):
        lienzo.append([])
        for j in range(PIXELES_ALTO):
            lienzo[i].append((255,255,255))
    return lienzo

def actualizar_paint(paint, color, x, y):
    if INICIO_LIENZO_X < x < FIN_LIENZO_X and INICIO_LIENZO_Y < y < FIN_LIENZO_Y:
        pos_x = x // 10
        pos_y = y // 10
        paint[pos_y][pos_x] = color
    return paint

def paint_mostrar(paint, color, nuevos_colores):
    pos_x = 0
    pos_y = 0
    color_x = 0
    color_y = 0
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()
    gamelib.draw_rectangle(INICIO_LIENZO_X, INICIO_LIENZO_Y, FIN_LIENZO_X, FIN_LIENZO_Y, fill="#FFFFFF")
    if color in COLORES_BASICOS:
        gamelib.draw_rectangle(INICIO_INTERFAZ_BOTONES_X, INICIO_INTERFAZ_BOTONES_Y, FIN_INTERFAZ_BOTONES_X, FIN_INTERFAZ_BOTONES_Y, fill=COLORES_BASICOS.get(color))
    else:
        gamelib.draw_rectangle(INICIO_INTERFAZ_BOTONES_X, INICIO_INTERFAZ_BOTONES_Y, FIN_INTERFAZ_BOTONES_X ,FIN_INTERFAZ_BOTONES_Y, fill=nuevos_colores.get(color))
    for i in range(len(paint)):
        gamelib.draw_line(INICIO_LIENZO_X, pos_y, FIN_LIENZO_X, pos_y, fill="#000000")
        pos_y += TAMANIO_CELDAS
        gamelib.draw_line(pos_x, INICIO_LIENZO_Y, pos_x, FIN_LIENZO_Y, fill="#000000")
        pos_x += TAMANIO_CELDAS
        for j in range(len(paint[i])):
            if paint[i][j] in COLORES_BASICOS:
                gamelib.draw_rectangle(color_x, color_y, color_x+TAMANIO_CELDAS, color_y+TAMANIO_CELDAS, fill=COLORES_BASICOS.get(paint[i][j]))
            else:
                gamelib.draw_rectangle(color_x, color_y, color_x+TAMANIO_CELDAS, color_y+TAMANIO_CELDAS, fill=nuevos_colores.get(paint[i][j]))
            color_x+=TAMANIO_CELDAS
        color_x = 0
        color_y += TAMANIO_CELDAS
    gamelib.draw_end()

def mostrar_paleta():
    pos_x = INICIO_BOTONES_X
    pos_y = INICIO_BOTONES_Y
    paleta = []
    for color in COLORES_BASICOS.keys():
        paleta.append(color)
        gamelib.draw_rectangle(pos_x, pos_y, pos_x + TAMANIO_BOTONES_COLORES, pos_y + TAMANIO_BOTONES_COLORES, fill=COLORES_BASICOS.get(color))
        pos_x += TAMANIO_BOTONES_COLORES
    return paleta

def mostrar_botones():
    pos_x = INICIO_BOTONES_X
    for i in range(len(COLORES_BOTON_AC)):
        gamelib.draw_rectangle(pos_x, INICIO_BOTONES_Y + ALTO_BOTONES + ESPACIO_ENTRE_BOTONES_Y, pos_x + ESPACIO_ENTRE_BOTONES_X, FIN_BOTONES_Y, fill=COLORES_BOTON_AC[i])
        pos_x += ESPACIO_ENTRE_BOTONES_X
    pos_x += ESPACIO_ENTRE_BOTON_AC_X
    for j in range(len(NOMBRES_BOTONES)):
        gamelib.draw_rectangle(pos_x + ESPACIO_ENTRE_BOTONES_X, INICIO_BOTONES_Y + ALTO_BOTONES + ESPACIO_ENTRE_BOTONES_Y, pos_x + ANCHO_BOTONES, FIN_BOTONES_Y, fill="#FFFFFF")
        gamelib.draw_text(NOMBRES_BOTONES[j], pos_x + POS_X_TEXTO , FIN_BOTONES_Y-INICIO_BOTONES_Y + POS_Y_TEXTO , size=10, fill="#000000")
        pos_x += ANCHO_BOTONES

def actualizar_color(paleta, color, x, y):
    if INICIO_BOTONES_X < x < FIN_BOTONES_X and INICIO_BOTONES_Y < y < FIN_BOTONES_Y - (ALTO_BOTONES + ESPACIO_ENTRE_BOTONES_Y):
        pos_x = (x - 10) // 15
        color_nuevo = paleta[pos_x]
    else:
        return color
    return color_nuevo

def agregar_color(nuevos_colores, paleta, color, x, y):
    
    if INICIO_BOTONES_X < x < INICIO_BOTONES_X + ANCHO_BOTON_AC and FIN_BOTONES_Y - ALTO_BOTONES < y < FIN_BOTONES_Y:
        hex_color = gamelib.input("Ingrese el color: ")
        if hex_color == None:
            return nuevos_colores, color, paleta
        if len(hex_color) != 7:
            gamelib.say("Color inválido!")
            return nuevos_colores, color, paleta
        if color in COLORES_BASICOS:
            return nuevos_colores, color, paleta
        color = (int(hex_color[1:3], 16),int(hex_color[3:5], 16),int(hex_color[5:7], 16))
        paleta.append(color)
        nuevos_colores[color] = hex_color
    return nuevos_colores, color, paleta

def guardar_png(paint, paleta, x, y):
    imagen = []
    if FIN_BOTONES_X - ANCHO_BOTONES < x < FIN_BOTONES_X and INICIO_BOTONES_Y + ALTO_BOTONES + ESPACIO_ENTRE_BOTONES_Y < y < FIN_BOTONES_Y:
        for i in range(len(paint)):
            imagen.append([])
            for j in range(len(paint[i])):
                if paint[i][j] in paleta:
                    imagen[i].append(paleta.index(paint[i][j]))
        while True:
            ruta = gamelib.input("Ingrese la ruta y el nombre del archivo: ") ###En caso de colocar solamente el nombre se guardará en la ruta del programa
            if ruta != "" and ruta != None:
                try:
                    ruta +=".png"
                    png.escribir(ruta, paleta, imagen)
                    break
                except FileNotFoundError:
                    gamelib.say("No existe la ruta indicada!")
                    continue
            if ruta == "":
                gamelib.say("Nombre inválido!")
            else:
                break

def guardar_ppm(paint, x, y):
    inicio_boton = INICIO_BOTONES_X + ANCHO_BOTON_AC + ESPACIO_ENTRE_BOTON_AC_X + ESPACIO_ENTRE_BOTONES_X
    fin_boton = inicio_boton + ANCHO_BOTONES - ESPACIO_ENTRE_BOTONES_X
    if inicio_boton < x < fin_boton and INICIO_BOTONES_Y + ALTO_BOTONES + ESPACIO_ENTRE_BOTONES_Y < y < FIN_BOTONES_Y:
        while True:
            ruta = gamelib.input("Ingrese la ruta y el nombre del archivo: ") ###En caso de colocar solamente el nombre se guardará en la ruta del programa
            if ruta != "" and ruta != None:
                try:
                    ruta += ".ppm"
                    with open(ruta, "w") as archivo:
                        archivo.write(ENCABEZADO_PPM[0]+"\n")
                        archivo.write(str(ENCABEZADO_PPM[1][0]) + " " + str(ENCABEZADO_PPM[1][1])+"\n")
                        archivo.write(ENCABEZADO_PPM[2]+"\n")
                        for i in range(len(paint)):
                            for j in range(len(paint[i])):
                                for k in range(len(paint[i][j])):
                                    archivo.write(str(paint[i][j][k]) + " ")
                                archivo.write("   ")
                            archivo.write("\n")
                        break
                except FileNotFoundError:
                    gamelib.say("No existe la ruta indicada!")
                    continue
            if ruta == "":
                gamelib.say("Nombre inválido!")
            else:
                break



def cargar_ppm():
    pass
        
    

def main():
    gamelib.title("AlgoPaint")
    gamelib.resize(TAMANIO_VENTANA_X , TAMANIO_VENTANA_Y)
    nuevos_colores = {}
    paint = paint_nuevo()
    color = (0,0,0)
    while gamelib.is_alive():
        paint_mostrar(paint, color, nuevos_colores)
        paleta = mostrar_paleta()
        mostrar_botones()
        
        ev = gamelib.wait()
        if not ev:
            break
        


        """if ev.type == gamelib.EventType.KeyPress and ev.key == "c":
            print("Se cambio el color")"""
        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            x,y = ev.x, ev.y
            color = actualizar_color(paleta, color, x, y)
            nuevos_colores, color, paleta = agregar_color(nuevos_colores, paleta, color, x, y)
            paint = actualizar_paint(paint, color, x, y)
            guardar_png(paint, paleta, x, y)
            guardar_ppm(paint, x, y)
        """elif ev.type == gamelib.EventType.ButtonRelease and ev.mouse_button == 1:
            print(f'se ha soltado el botón del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.KeyPress:
            print(f'se ha presionado la tecla: {ev.key}')"""

gamelib.init(main)