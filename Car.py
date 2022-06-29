import sys
import PIL.Image

cars = []


class Car:
    name = ""
    image_path = ""

    def __init__(self, name: str, hp: int, weight: int, year: int, country: str, image_path: str):
        self.name = name
        self.hp = hp
        self.weight = weight
        self.year = year
        self.country = country
        self.image_path = image_path

    def add_car_to_list(self):
        cars.append(self)

    @staticmethod
    def show_car_list():
        car_index = 1
        print('Lista gotowych aut.')
        for c in cars:
            print('[' + str(car_index) + ']' + ' ' + c.name, c.hp, c.weight, c.year, c.country, c.image_path)
            car_index +=1

    @staticmethod
    def save_cars_to_file():
        plik1 = open("Cars_list.txt", "w")
        for c in cars:
            plik1.write(str(c.name) + ' ' + str(c.hp) + ' ' + str(c.weight) + ' ' + str(c.year) + ' ' + c.country + ' ' + c.image_path + "\n")
        plik1.close()

    @staticmethod
    def open_car_list():
        try:
            plik1 = open("Cars_list.txt", "r")
            for line in plik1.readlines():
                params = line.split()
                c = Car(name=params[0], hp=int(params[1]), weight=int(params[2]), year=int(params[3]),
                        country=str(params[4]), image_path=str(params[5]))
                cars.append(c)
            plik1.close()
        except FileNotFoundError:
            return


    def show_car_image(self):
        try:
            image = PIL.Image.open(self.image_path)
            image.show()
        except Exception:
            print(f'Cannot open car image on given path : {self.image_path}')

    @staticmethod
    def stop_working_app():
        sys.exit("Zakończyłeś działanie programu")