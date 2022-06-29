import PIL.Image
from Car import *


while True:
    print('Wprowadź 1 aby stworzyć samochód.')
    print('Wprowadź 2 aby wyświetlić gotowe auta. > Problem z wyświetleniem wczytanej listy')
    print('Wprowadź 3 zapisać listę aut do pliku.')
    print('Wprowadź 4 aby wczytać gotową listę aut.')
    print('Wprowadź 5 aby wyświetlić obraz auta. > Nie działa')
    print('Wprowadź 6 aby zakończyć działanie programu.')

    users_choice = int(input('Wybierz liczbę >>>\n'))


    if users_choice == 1:
        print('Podaj nazwę, moc, wagę, rok, państwo i obrazek auta')
        new_car = Car(name=input(), hp=int(input()), weight=int(input()), year=int(input()), country=input(), image_path=input())
        Car.add_car_to_list(new_car)

    if users_choice == 2:
        Car.show_car_list()

    if users_choice == 3:
        Car.save_cars_to_file()

    if users_choice == 4:
        Car.open_car_list()

    if users_choice == 5:
        Car.show_car_image()

    if users_choice == 6:
        Car.stop_working_app()