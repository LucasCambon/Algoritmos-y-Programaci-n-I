import gamelib

PIXELES_ANCHO = 20
PIXELES_ALTO = 20
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

def paint_nuevo(ancho, alto):
    '''inicializa el estado del programa con una imagen vacía de ancho x alto pixels'''
    lienzo = []
    for i in range(PIXELES_ANCHO):
        lienzo.append([])
        for j in range(PIXELES_ALTO):
            lienzo[i].append((255,255,255))
    return lienzo

def actualizar_paint(paint, color, x, y):
    print(color)
    if 0 < x < 200 and 0 < y < 200:
        pos_x = x // 10
        pos_y = y // 10
        paint[pos_y][pos_x] = color
    return paint

def paint_mostrar(paint):
    pos_x = 0
    pos_y = 0
    color_x = 0
    color_y = 0
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()
    gamelib.draw_rectangle(0,0,200,200, fill="#FFFFFF")
    gamelib.draw_rectangle(0,200,200,250, fill="#808080")
    for i in range(len(paint)):
        gamelib.draw_line(0, pos_y, 200, pos_y, fill="#000000")
        pos_y += 10
        gamelib.draw_line(pos_x, 0, pos_x, 200, fill="#000000")
        pos_x += 10
        for j in range(len(paint[i])):
            gamelib.draw_rectangle(color_x,color_y,color_x+10,color_y+10, fill=COLORES_BASICOS.get(paint[i][j]))
            color_x+=10
        color_x = 0
        color_y += 10
    gamelib.draw_end()

def mostrar_paleta():
    pos_x = 10
    pos_y = 205
    paleta = []
    for color in COLORES_BASICOS.keys():
        paleta.append(color)
        gamelib.draw_rectangle(pos_x,pos_y, pos_x+15, pos_y+15, fill=COLORES_BASICOS.get(color))
        pos_x += 15
    return paleta

def actualizar_color(paleta, color, x, y):
    if 10 < x < 190 and 205 < y < 220:
        pos_x = (x - 10) // 15
        color_nuevo = paleta[pos_x]
        print(color_nuevo)
    else:
        return color
    return color_nuevo

def main():
    gamelib.title("AlgoPaint")
    gamelib.resize(200, 250)
    
    paint = paint_nuevo(PIXELES_ANCHO, PIXELES_ALTO)
    color = (0,0,0)
    while gamelib.is_alive():
        paint_mostrar(paint)
        paleta = mostrar_paleta()
        
        ev = gamelib.wait()
        if not ev:
            break
        


        if ev.type == gamelib.EventType.KeyPress and ev.key == "c":
            print("Se cambio el color")
        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            x,y = ev.x, ev.y
            color = actualizar_color(paleta, color, x, y)
            print(color)
            paint = actualizar_paint(paint, color, x, y)
        """elif ev.type == gamelib.EventType.ButtonRelease and ev.mouse_button == 1:
            print(f'se ha soltado el botón del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.KeyPress:
            print(f'se ha presionado la tecla: {ev.key}')"""

gamelib.init(main)