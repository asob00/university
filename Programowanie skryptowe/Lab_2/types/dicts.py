from types import slownik


def zapisz(string):
    for liczba in string:
        if liczba in slownik.keys():
            slownik[liczba] += 1
        else:
            slownik[liczba] = 1


def wypisz():
    return_string = ''

    for i in range(10):
        if str(i) in slownik.keys() and i != 9:
            return_string += f'{i}:{slownik[str(i)]},'
        elif str(i) in slownik.keys() and i == 9:
            return_string += f'{i}:{slownik[str(i)]}'

    return return_string
