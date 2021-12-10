class Cola:
    '''
    Representa a una cola, con operaciones de encolar y
    desencolar. El primero en ser encolado es también el primero
    en ser desencolado.
    '''
    
    def __init__(self):
        '''
        Crea una cola vacía.
        '''
        self.items = []

    def encolar(self, x):
        '''
        Encola el elemento x.
        '''
        self.items.append(x)

    def desencolar(self):
        '''
        Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía, levanta ValueError.
        '''
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        return self.items.pop(0)

    def esta_vacia(self):
        '''
        Devuelve True si la cola esta vacía, False si no.
        '''
        return len(self.items) == 0
    
    # Este método **no** es parte del TDA Cola y sólo está 
    # para simplificar las pruebas
    def encolar_muchos(self, iterable):
        '''
        Encola todos los elementos del iterable en la cola.
        '''
        for elem in iterable:
            self.encolar(elem)

    # Este método **no** es parte del TDA Cola y sólo está 
    # para simplificar las pruebas
    def __str__(self):
        '''
        Devuelve una representación en la forma > [e1, e2, ...] -> de la cola.
        '''
        return '> [' + ', '.join(map(str, reversed(self.items))) + ' ] ->'


class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox