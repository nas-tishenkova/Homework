import combinatorics
import areas
a = input('выберите модуль: комбинаторика или геомертия?')
if a == 'комбинаторика':
    b = int(input('выберите необходимую вам функцию:\n 1-вычислить факториал\n 2-вычислить количество перестановок(написать элементы через пробел)\n 3-вычислить количество перестановок(написать число элементов)\n 4-вычислить количество сочетаний\n 5-вычислить количество размещений'))
    if b == 1:
        n = int(input("факториал какого числа мы ищем?"))
        print(combinatorics.fact(n))
    elif b == 2:
        p = input("напишите через пробел элементы для перестановки").split()
        n = len(p)
        print(combinatorics.fact(n))
    elif b == 3:
        n = int(input("напишите число элементов, которые будем переставлять"))
        print(combinatorics.fact(n))
    elif b == 4:
        n = int(input("напишите число n"))
        m = int(input("напишите число m"))
        print(combinatorics.kolvo_sochetanii(m, n))
    elif b == 5:
        n = int(input("напишите число n"))
        m = int(input("напишите число m"))
        print(combinatorics.kolvo_razmeshch(m, n))
elif a == 'геометртия':
    print('выберите необходимую вам функцию:\n 1-площадь прямоугольника\n 2-площадь квадрата\n 3-площадь треугольника\n 4-площадь поверхности шара')
    b = int(input())
    if b == 1:
        a = int(input("длина одной стороны прямоугольника"))
        b = int(input("длина второй стороны прямоугольника"))
        print(areas.rectangle_area(a, b))
    elif b == 2:
        a = int(input("длина стороны квадрата"))
        print(areas.square_area(a))
    elif b == 3:
        a = int(input("длина основания треугольника"))
        h = int(input("длина высоты проведенной к этому основанию"))
        print(areas.triangle_area(a, h))
    elif b == 4:
        r = input("радиус шара")
        print(areas.surface_of_ball_area(r))

