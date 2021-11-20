import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 300
TURNO_INICIAL = 1

def juego_crear():
    """Inicializar el estado del juego"""
    juego = []
    for i in range(10):
        juego.append([])
        for j in range(10):
            juego[i].append(0)
    print(juego)
    return juego

def juego_actualizar(juego, x, y, turno):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    if 50 <= x <= 250 and 50 <= y <= 250:
        pos_x = (x-50) // 20
        pos_y = (y-50) // 20
        if juego[pos_y][pos_x] == 0:
            if turno % 2 == 1:
                juego[pos_y][pos_x] = 1
            else:
                juego[pos_y][pos_x] = 2
            turno +=1
    return juego, turno

def juego_mostrar(juego, turno):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea Matrix style', 150, 20, fill="green")
    gamelib.draw_rectangle(50,50,250,250, outline="green", fill="black")
    pos_x = 50
    pos_y = 50
    posicion_x_fichas = 10
    posicion_y_fichas = 10
    if turno % 2 == 1:
        gamelib.draw_text('Turno: X', 150, 275, fill="green")
    else:
        gamelib.draw_text('Turno: O', 150, 275, fill="green")
    
    for i in range(len(juego)):
        gamelib.draw_line(50,pos_y+20,250,pos_y+20, fill="green")
        pos_y += 20
        gamelib.draw_line(pos_x+20,50,pos_x+20,250, fill="green")
        pos_x += 20
        for j in range(len(juego[i])):
            if juego[i][j] == 1:
                gamelib.draw_text('X', posicion_x_fichas+50, posicion_y_fichas+50, fill="green")
                posicion_x_fichas += 20
            elif juego[i][j] == 0:
                gamelib.draw_text('-', posicion_x_fichas+50, posicion_y_fichas+50, fill="black")
                posicion_x_fichas += 20
            elif juego[i][j] == 2:
                gamelib.draw_text('O', posicion_x_fichas+50, posicion_y_fichas+50, fill="green")
                posicion_x_fichas += 20
        posicion_x_fichas = 10
        posicion_y_fichas += 20



def main():
    juego = juego_crear()
    turno = TURNO_INICIAL
    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego, turno)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego, turno = juego_actualizar(juego, x, y, turno)
            

gamelib.init(main)