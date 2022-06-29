import sys
from Car import *


class Garage:
    cars = []

    def add_car_to_garage(self, car: Car):
        self.cars.append(car)

    def remove_car_from_garage(self, car_name: str):
        print('With car do you want to remove ?')
        for c in self.cars:
            if c.name == car_name:
                self.cars.remove(c)
                break

    def print_garage(self):
        print('You have given cars in your garage: ')
        for c in self.cars:
            print(f'{c.name}')

    def save_cars_to_file(self):
        plik = open("Garage_lista.txt", "w")
        for car in self.cars:
            plik.write(car + "\n")
        plik.close()

    def open_car_list(self):
        try:
            plik = open("Garage_lista.txt")
            for line in plik.readlines():
                self.cars.append(line.strip())
            plik.close()
        except FileNotFoundError:
            return


    open_car_list()