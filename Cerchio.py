import math


class Cerchio(object):

    def __init__(self, value):
        self.raggio = value

    @property
    def raggio(self):
        return self.__raggio

    @raggio.setter
    def raggio(self, value):
        if value < 0:
            raise ValueError("passato un valore negativo per il raggio")
        self.__raggio = value

    @property
    def area(self):
        return self.raggio ** 2 * math.pi

    @property
    def circonferenza(self):
        return self.diametro * math.pi

    @property
    def diametro(self):
        return 2 * self.raggio


if __name__ == '__main__':
    def main():
        try:
            circle = Cerchio(10)
            print(circle.raggio)
            print(circle.area)
            print(circle.diametro)
            print(circle.circonferenza)
        except ValueError as ve:
            print(ve)


    main()
