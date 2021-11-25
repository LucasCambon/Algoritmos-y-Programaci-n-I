class _Nodo:
  def __init__(self, dato, prox=None):
    self.dato = dato
    self.prox = prox

class ListaEnlazada:
  def __init__(self):
    self.prim = None
  
  def append(self, elemento):
    nuevo = _Nodo(elemento)
    if not self.prim:
      self.prim = nuevo
      return
    actual = self.prim
    while actual.prox:
      actual = actual.prox
    actual.prox = nuevo

  def __str__(self):
    actual = self.prim
    cadena = ''
    while actual:
      cadena += f'| {actual.dato} | -> '
      actual = actual.prox
    return cadena

  def extend(self, otra):
    if not otra.prim:
      return
    if not self.prim:
      self.prim = _Nodo(otra.prim.dato)
      actual_otra = otra.prim.prox
    else:
      actual_otra = otra.prim
    actual = self.prim
    while actual.prox:
      actual = actual.prox
    while actual_otra:
      nuevo = _Nodo(actual_otra.dato)
      actual.prox = nuevo
      actual_otra = actual_otra.prox
      actual = actual.prox
      
  def eliminar(self, elemento):
    if not self.prim:
      return
    
    if self.prim.dato == elemento:
      self.prim = self.prim.prox
      return

    anterior = None
    actual = self.prim
    while actual:
      if actual.dato == elemento:
        break
      
      anterior = actual
      actual = actual.prox
    
    if actual is not None:
      anterior.prox = actual.prox

  def __iter__(self):
    return IteradorListaEnlazada(self)
  
  def map(self, funcion):
    resultado = ListaEnlazada()
    
    actual_nueva = resultado.prim
    actual = self.prim
    while actual:
      nuevo_nodo = _Nodo(funcion(actual.dato))
      if not actual_nueva:
        resultado.prim = nuevo_nodo
        actual_nueva = nuevo_nodo
      else:
        actual_nueva.prox = nuevo_nodo
        actual_nueva = actual_nueva.prox

      actual = actual.prox

    return resultado

  def filter(self, funcion):
    resultado = ListaEnlazada()
    
    actual_nueva = resultado.prim
    actual = self.prim
    while actual:
      if not funcion(actual.dato):
        actual = actual.prox
        continue
      
      nuevo_nodo = _Nodo(actual.dato)
      if not actual_nueva:
        resultado.prim = nuevo_nodo
        actual_nueva = nuevo_nodo
      else:
        actual_nueva.prox = nuevo_nodo
        actual_nueva = actual_nueva.prox

      actual = actual.prox

    return resultado

  def filter_mut(self, funcion):
    while self.prim:
      if funcion(self.prim.dato):
        break
      self.prim = self.prim.prox

    if not self.prim:
      return    
    
    anterior = self.prim
    actual = anterior.prox
    while actual:
      if not funcion(actual.dato):
        actual = actual.prox
        continue
      
      anterior.prox = actual
      anterior = actual
      actual = actual.prox


class IteradorListaEnlazada:
  def __init__(self, le):
    self.actual = le.prim
  
  def __next__(self):
    if not self.actual:
      raise StopIteration
    
    dato = self.actual.dato
    self.actual = self.actual.prox
    return dato

le = ListaEnlazada()
le.append(1)
le.append(2)
le.append(3)
print(le)
le2 = ListaEnlazada()
le2.append(4)
le2.append(5)
le2.append(6)
print(le2)
le.extend(le2)
print(le)


for elem in le2:
  print(elem)


le3 = le2.map(lambda x: x * 5)
print(le3)

print('pre filter: ', le)
print('filter inmutable: ', le.filter(lambda x: x % 2 == 0))
le.filter_mut(lambda x: x % 2 == 0)
print('filter mutable: ', le)
