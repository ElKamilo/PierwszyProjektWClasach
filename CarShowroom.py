import sys
from Car import *

showrooms = []
cars_in_showroom = []

class CarShowroom:
    name = ""

    def __init__(self, name: str, country: str, city: str):
        self.name = name
        self.country = country
        self.city = city

    def add_new_showroom_to_list(self):
        showrooms.append(self)

    @staticmethod
    def showrooms_list():
        showroom_index = 1
        print('Lista gotowych salonów.')
        for room in showrooms:
            print('[' + str(showroom_index) + ']' + ' ' + room.name, room.country, room.city)
            showroom_index += 1

    def add_car_to_showroom(self):
        Car.show_car_list()

    @staticmethod
    def save_showrooms_to_file():
        plik2 = open("Showrooms_list.txt", "w")
        for room in showrooms:
            plik2.write(room.name + ' ' + room.country + ' ' + room.city + "\n")
        plik2.close()

    @staticmethod
    def open_showrooms_list():
        try:
            plik2 = open("Showrooms_list.txt", "r")
            for line in plik2.readlines():
                params = line.split()
                s = CarShowroom(name=params[0], country=params[1], city=params[2])
                showrooms.append(s)
            plik2.close()
        except FileNotFoundError:
            return


    @staticmethod
    def add_car_to_car_showroom(car):
        cars_in_showroom.append(car)

    def get_user_input_car(self) -> Car:
        print(f'Welcome in {self.name} showroom')
        index = 1
        for c in self.cars:
            print(f'{index} : {c.name}')
            index += 1

        choice = int(input())
        return self.cars[choice - 1]