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
INICIO_GPPM_X = INICIO_BOTONES_X + ANCHO_BOTON_AC + ESPACIO_ENTRE_BOTON_AC_X + ESPACIO_ENTRE_BOTONES_X
INICIO_CPPM_X = INICIO_BOTONES_X + ANCHO_BOTON_AC + ESPACIO_ENTRE_BOTON_AC_X + ESPACIO_ENTRE_BOTONES_X + ANCHO_BOTONES

### TEXTO
POS_X_TEXTO = 26
POS_Y_TEXTO = 198

### PPM
ENCABEZADO_PPM = ["P3", (PIXELES_ANCHO, PIXELES_ALTO), "255"]

class Paint:

    def __init__(self):
        self.nuevos_colores = COLORES_BASICOS.copy()
        self.color = (0,0,0)
        self.lienzo = []

    def paint_nuevo(self):
        '''inicializa el estado del programa con una imagen vacía de ancho x alto pixels'''
        for i in range(PIXELES_ANCHO):
            self.lienzo.append([])
            for j in range(PIXELES_ALTO):
                self.lienzo[i].append((255,255,255))

    def actualizar_paint(self, x, y):
        
        try:
            pos_x = x // 10
            pos_y = y // 10
            self.lienzo[pos_y][pos_x] = self.color
        except IndexError:
            gamelib.say("No se puede pintar fuera del lienzo!")


    def actualizar_color(self, x):
            pos_x = (x - 10) // 15
            paleta = list(self.nuevos_colores.keys())
            self.color = paleta[pos_x]

        

    def agregar_color(self):
        
        hex_color = gamelib.input("Ingrese el color: ")
        if hex_color == None:
            return
        if len(hex_color) != 7:
            gamelib.say("Color inválido!")
            return 
        color = (int(hex_color[1:3], 16),int(hex_color[3:5], 16),int(hex_color[5:7], 16))
        self.nuevos_colores[color] = hex_color

    def guardar_png(self):
        imagen = []
        paleta = list(self.nuevos_colores.keys())
        for i in range(len(self.lienzo)):
            imagen.append([])
            for j in range(len(self.lienzo[i])):
                if self.lienzo[i][j] in paleta:
                    imagen[i].append(paleta.index(self.lienzo[i][j]))
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

    def guardar_ppm(self):

        while True:
            ruta = gamelib.input("Ingrese la ruta y el nombre del archivo: ") ###En caso de colocar solamente el nombre se guardará en la ruta del programa
            if ruta != "" and ruta != None:
                try:
                    ruta += ".ppm"
                    with open(ruta, "w") as archivo:
                        archivo.write(ENCABEZADO_PPM[0]+"\n")
                        archivo.write(str(ENCABEZADO_PPM[1][0]) + " " + str(ENCABEZADO_PPM[1][1])+"\n")
                        archivo.write(ENCABEZADO_PPM[2]+"\n")
                        for i in range(len(self.lienzo)):
                            for j in range(len(self.lienzo[i])):
                                for k in range(len(self.lienzo[i][j])):
                                    archivo.write(str(self.lienzo[i][j][k]) + " ")
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



    def cargar_ppm(self):

        cont_lineas = 0
        while True:
            ruta = gamelib.input("Ingrese la ruta y el nombre del archivo: ") ###En caso de colocar solamente el nombre se cargará el archivo dentro de la ruta del programa
            if ruta != "" and ruta != None:
                try:
                    ruta += ".ppm"
                    with open(ruta) as archivo:
                        self.lienzo.clear()
                        archivo_sin_encabezado = archivo.readlines()[3:]
                        for linea in archivo_sin_encabezado:
                            self.lienzo.append([])
                            lista_palabras = linea.rsplit()
                            for i in range(len(lista_palabras)):
                                if 0 <= i <= len(lista_palabras):
                                    if i % 3 == 2:
                                        color = (int(lista_palabras[i-2]), int(lista_palabras[i-1]), int(lista_palabras[i]))
                                        self.lienzo[cont_lineas].append(color)
                                        if color not in self.nuevos_colores:
                                            color_nuevo = "#" + f"{color[0]:02x}" + f"{color[1]:02x}" + f"{color[2]:02x}"
                                            self.nuevos_colores[color] = color_nuevo
                            cont_lineas += 1                            
                except FileNotFoundError:
                    gamelib.say("No se encuentra el archivo en la ruta indicada!")
                    continue
            if ruta == "":
                gamelib.say("Nombre inválido!")
            else:
                break


def paint_mostrar(paint):
    color_x = 0
    color_y = 0
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_rectangle(INICIO_LIENZO_X, INICIO_LIENZO_Y, (len(paint.lienzo)*10), (len(paint.lienzo[len(paint.lienzo)-1])*10), fill="#FFFFFF")
    if paint.color in paint.nuevos_colores:
        gamelib.draw_rectangle(INICIO_INTERFAZ_BOTONES_X, (len(paint.lienzo[len(paint.lienzo)-1])*10), (len(paint.lienzo)*10) ,FIN_INTERFAZ_BOTONES_Y, fill=paint.nuevos_colores.get(paint.color))
    for i in range(len(paint.lienzo)):
        for j in range(len(paint.lienzo[i])):
            if paint.lienzo[i][j] in paint.nuevos_colores:
                gamelib.draw_rectangle(color_x, color_y, color_x+TAMANIO_CELDAS, color_y+TAMANIO_CELDAS, fill=paint.nuevos_colores.get(paint.lienzo[i][j]))
            color_x+=TAMANIO_CELDAS
        color_x = 0
        color_y += TAMANIO_CELDAS

def mostrar_paleta():
    pos_x = INICIO_BOTONES_X
    pos_y = INICIO_BOTONES_Y
    for color in COLORES_BASICOS.keys():
        gamelib.draw_rectangle(pos_x, pos_y, pos_x + TAMANIO_BOTONES_COLORES, pos_y + TAMANIO_BOTONES_COLORES, fill=COLORES_BASICOS.get(color))
        pos_x += TAMANIO_BOTONES_COLORES

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
    

def main():
    gamelib.title("AlgoPaint")
    gamelib.resize(TAMANIO_VENTANA_X , TAMANIO_VENTANA_Y)
    paint = Paint()
    paint.paint_nuevo()
    print(paint.lienzo)
    while gamelib.is_alive():
        gamelib.draw_begin()
        paint_mostrar(paint)
        mostrar_paleta()
        mostrar_botones()
        gamelib.draw_end()
        
        ev = gamelib.wait()
        if not ev:
            break
        
        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            x,y = ev.x, ev.y
            if INICIO_BOTONES_X < x < FIN_BOTONES_X and INICIO_BOTONES_Y < y < FIN_BOTONES_Y - (ALTO_BOTONES + ESPACIO_ENTRE_BOTONES_Y):
                paint.actualizar_color(x)
            if INICIO_BOTONES_X < x < INICIO_BOTONES_X + ANCHO_BOTON_AC and FIN_BOTONES_Y - ALTO_BOTONES < y < FIN_BOTONES_Y:
                paint.agregar_color()
            if INICIO_LIENZO_X < x < FIN_LIENZO_X and INICIO_LIENZO_Y < y < FIN_LIENZO_Y:
                paint.actualizar_paint(x, y)
            if FIN_BOTONES_X - ANCHO_BOTONES < x < FIN_BOTONES_X and INICIO_BOTONES_Y + ALTO_BOTONES + ESPACIO_ENTRE_BOTONES_Y < y < FIN_BOTONES_Y:
                paint.guardar_png()
            if INICIO_GPPM_X < x < INICIO_GPPM_X + ANCHO_BOTONES - ESPACIO_ENTRE_BOTONES_X and INICIO_BOTONES_Y + ALTO_BOTONES + ESPACIO_ENTRE_BOTONES_Y < y < FIN_BOTONES_Y:
                paint.guardar_ppm()
            if INICIO_CPPM_X < x < INICIO_CPPM_X + ANCHO_BOTONES - ESPACIO_ENTRE_BOTONES_X and INICIO_BOTONES_Y + ALTO_BOTONES + ESPACIO_ENTRE_BOTONES_Y < y < FIN_BOTONES_Y:    
                paint.cargar_ppm()

gamelib.init(main)