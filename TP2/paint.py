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
INICIO_BOTONES_X = 10
FIN_BOTONES_X = 190
INICIO_BOTONES_Y = 205
FIN_BOTONES_Y = 240

def paint_nuevo(ancho, alto):
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
        pos_y += 10
        gamelib.draw_line(pos_x, INICIO_LIENZO_Y, pos_x, FIN_LIENZO_Y, fill="#000000")
        pos_x += 10
        for j in range(len(paint[i])):
            if paint[i][j] in COLORES_BASICOS:
                gamelib.draw_rectangle(color_x, color_y, color_x+10, color_y+10, fill=COLORES_BASICOS.get(paint[i][j]))
            else:
                gamelib.draw_rectangle(color_x, color_y, color_x+10, color_y+10, fill=nuevos_colores.get(paint[i][j]))
            color_x+=10
        color_x = 0
        color_y += 10
    gamelib.draw_end()

def mostrar_paleta():
    pos_x = INICIO_BOTONES_X
    pos_y = 205
    paleta = []
    for color in COLORES_BASICOS.keys():
        paleta.append(color)
        gamelib.draw_rectangle(pos_x, pos_y, pos_x + 15, pos_y + 15, fill=COLORES_BASICOS.get(color))
        pos_x += 15
    pos_x = 10
    return paleta

def mostrar_botones():
    pos_x = INICIO_BOTONES_X
    for i in range(len(COLORES_BOTON_AC)):
        gamelib.draw_rectangle(pos_x, INICIO_BOTONES_Y + 20, pos_x + 3, FIN_BOTONES_Y, fill=COLORES_BOTON_AC[i])
        pos_x +=3
    pos_x += 10
    for j in range(len(NOMBRES_BOTONES)):
        gamelib.draw_rectangle(pos_x + 3, INICIO_BOTONES_Y + 20, pos_x + 50, FIN_BOTONES_Y, fill="#FFFFFF")
        gamelib.draw_text(NOMBRES_BOTONES[j], pos_x + 26, FIN_BOTONES_Y-INICIO_BOTONES_Y + 198, size=10, fill="#000000")
        pos_x += 50

def actualizar_color(paleta, color, x, y):
    if INICIO_BOTONES_X < x < FIN_BOTONES_X and INICIO_BOTONES_Y < y < FIN_BOTONES_Y - 20:
        pos_x = (x - 10) // 15
        color_nuevo = paleta[pos_x]
    else:
        return color
    return color_nuevo

def agregar_color(nuevos_colores, paleta, color, x, y):
    
    if INICIO_BOTONES_X < x < INICIO_BOTONES_X + 21 and FIN_BOTONES_Y - 15 < y < FIN_BOTONES_Y:
        hex_color = gamelib.input("Ingrese el color: ")
        if hex_color == None or len(hex_color) != 7:
            return nuevos_colores, color, paleta
        color = (int(hex_color[1:3], 16),int(hex_color[3:5], 16),int(hex_color[5:7], 16))
        paleta.append(color)
        if color in COLORES_BASICOS:
            return nuevos_colores, color, paleta
        nuevos_colores[color] = hex_color
    return nuevos_colores, color, paleta

def guardar_png(paint, paleta, x, y):
    imagen = []
    if FIN_BOTONES_X - 50 < x < FIN_BOTONES_X and INICIO_BOTONES_Y + 20 < y < FIN_BOTONES_Y:
        for i in range(len(paint)):
            imagen.append([])
            for j in range(len(paint[i])):
                if paint[i][j] in paleta:
                    imagen[i].append(paleta.index(paint[i][j]))
        while True:
            nombre_archivo = gamelib.input("Ingrese el nombre del archivo: ")
            if nombre_archivo != "" and nombre_archivo != None:
                nombre_archivo +=".png"
                png.escribir(nombre_archivo, paleta, imagen)
                break
            if nombre_archivo == "":
                gamelib.say("Nombre inválido!")
            else:
                break
        
    

def main():
    gamelib.title("AlgoPaint")
    gamelib.resize(TAMANIO_VENTANA_X , TAMANIO_VENTANA_Y)
    nuevos_colores = {}
    paint = paint_nuevo(PIXELES_ANCHO, PIXELES_ALTO)
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
        """elif ev.type == gamelib.EventType.ButtonRelease and ev.mouse_button == 1:
            print(f'se ha soltado el botón del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.KeyPress:
            print(f'se ha presionado la tecla: {ev.key}')"""

gamelib.init(main)