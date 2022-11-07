def fact(n):
    '''вычисляет факториал числа'''

    if n == 0:
        return 1
    return fact(n-1) * n




def kolvo_perestanovok_s(p):
    '''принимает на вход элементы через пробел и определяет количество их перестановок'''

    n = len(p)
    return fact(n)



def kolvo_perestanovok_n(n):
    '''принимает на вход число элементов, для которых мы хотим посчитать количество перестановок'''

    return fact(n)



def kolvo_sochetanii(m, n):
    '''формула количества сочетаний: сколькими способами можно выбрать m объектов из n'''

    return fact(n) / ((fact(n - m)) * fact(m))



def kolvo_razmeshch(m, n):
    '''формула количества размещений'''

    return kolvo_sochetanii(m, n) * fact(m)