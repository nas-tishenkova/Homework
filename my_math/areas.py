def rectangle_area(a, b):
    '''формула для вычисления площади прямоугольника; аргументы - длины сторон прямоугольника'''

    return a * b



def square_area(a):
    '''формула для вычисления площади квадрата; аргумент - длина стороны квадрата'''

    return a ** 2



def triangle_area(a, h):
    '''формула для вычисления площади треугольника; аргументы - длина основания и высота проведенная к этому основанию'''

    return 1/2 * a * h


def surface_of_ball_area(r):
    '''формула для вычисления площади поверхности шара; аргумент - радиус шара'''
    
    from math import pi
    return 4 * pi * r ** 2