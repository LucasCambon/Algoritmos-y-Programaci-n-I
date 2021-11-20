import vectores

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    ab = vectores.diferencia(x1, y1, z1, x2, y2, z2)
    ac = vectores.diferencia(x1, y1, z1, x3, y3, z3)
    prodVectorial = vectores.prod_vectorial(ab[0], ab[1], ab[2], ac[0], ac[1], ac[2])
    norma = vectores.norma(prodVectorial[0],prodVectorial[1],prodVectorial[2])
    area = norma/2
    return area

assert area_triangulo(1,2,3,1,2,3,1,2,3) == 0
assert area_triangulo(8,4,2,6,2,8,2,8,4) == 23.49468024894146
assert area_triangulo(9,8,4,2,5,4,6,7,3) == 3.9370039370059056