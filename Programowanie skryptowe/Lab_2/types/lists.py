from types import lista


def zapisz(liczba):
    for i in range(10):
        counter = 0
        for char in liczba:
            if str(i) == char:
                counter += 1

        if counter > 0 and i != 9:
            lista.append(f'{i}:{counter},')
        elif counter > 0 and i == 9:
            lista.append(f'{i}:{counter}')


def wypisz():
    return_str = ''
    for i in lista:
        return_str += i
    return return_str
