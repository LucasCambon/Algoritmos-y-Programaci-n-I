class ListaEnlazada:


    def pop(self, i=None):
        '''Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento.'''
        actual = self.prim
        anterior = None
        indice = 0
        if i == None:
            i = self.cant-1
            print(i)
        while True:
            if i >= self.cant:
                raise IndexError
            if i == 0:
                self.prim = self.prim.prox
                self.cant -= 1
                return actual.dato
            if indice == i:
                anterior.prox = actual.prox
                self.cant -= 1
                return actual.dato
            indice += 1
            anterior = actual
            actual = actual.prox



    def insert(self, i, x):
        '''Inserta el elemento x en la posición i.
        Si la posición a insertar es menor que cero o mayor 
        que la longitud de la lista, levanta IndexError'''
        actual = self.prim
        nuevo = _Nodo(x)
        anterior = None
        indice = 0
        if i > self.cant or i < 0:
                raise IndexError
        while True:
            if i == 0:
                self.prim = nuevo
                self.prim.prox = actual
                self.cant += 1
                return
            if indice == i:
                anterior.prox = nuevo
                nuevo.prox = actual
                self.cant += 1
                return
            indice += 1
            anterior = actual
            actual = actual.prox

            



    def remove(self, x):
        '''Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, levanta ValueError.'''
        actual = self.prim
        anterior = actual
        for i in range(self.cant):
            if x == self.prim.dato:
                self.prim = self.prim.prox
            if x == actual.dato:
                anterior.prox = actual.prox
                self.cant -= 1
                return
            anterior = actual
            actual = actual.prox
        raise ValueError

    def remover_todos(self, elem):
        actual = self.prim
        contador = 0
        for i in range(self.cant):
            if elem == self.prim.dato:
                self.prim = self.prim.prox
            if elem == actual.dato:
                self.remove(elem)
                self.cant -= 1
                contador += 1
            actual = actual.prox
        return contador

                



    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0


    def append(self, dato):
        nuevo = _Nodo(dato)
        if not self.prim:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            # act es el ultimo nodo
            act.prox = nuevo
        self.cant += 1

    def __str__(self):
        actual = self.prim
        cadena = ''
        while actual:
            cadena += f'| {actual.dato} | -> '
            actual = actual.prox
        return cadena

    def __len__(self):
        return self.cant

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

le = ListaEnlazada()
le.append(1)
le.append(2)
le.append(2)
le.append(2)
le.append(2)
le.append(3)
le.append(4)
le.append(5)
print(le)
print(le.remover_todos(2))
print(le)
