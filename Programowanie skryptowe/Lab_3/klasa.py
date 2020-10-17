class Klasa(object):

    tab = [1, 2, 3]

    def __init__(self, t, a, b):
        self.tab = t
        self._zmienna1 = a
        self.__zmienna2 = b
        print("Wywołano metodę '__init__()'")

    def __del__(self):
        print("Wywołano metodę '__del__()'")

    def __str__(self):
        return "Wywołano metodę '__str__()'"

    def metodaInstancyjna(self):
        print("Wywołano metodę 'metodaInstancyjna()'")
        print(Klasa.tab)
        print(self.tab)

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę 'metodaKlasowa()'")

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę 'metodaStatyczna()'")