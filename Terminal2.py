import Car
from Car import *
from CarShowroom import *



while True:
    print('Wprowadź 1 aby stworzyć salon samochodowy.')
    print('Wprowadź 2 aby wyświetlić gotowe salony samochodowe. > Problem z wyświetleniem wczytanej listy')
    print('Wprowadź 3 zapisać listę salonów do pliku.')
    print('Wprowadź 4 aby wczytać gotową listę salonów.')
    print('Wprowadź 5 aby dodać auto do salonu.')

    users_choice = int(input('Wybierz liczbę >>>\n'))

    if users_choice == 1:
        print('Podaj nazwę, państwo oraz miasto.')
        new_showroom = CarShowroom(name=input(), country=input(), city=input())
        CarShowroom.add_new_showroom_to_list(new_showroom)

    if users_choice == 2:
        CarShowroom.showrooms_list()
        # print('Wybierz 1 aby dodać auto do salonu.')
        # print('Wybierz 2 aby dodać auto do salonu.')
        # # users_choice2 = int(input())
        # # while users_choice2 == 1:
        # #     pass


    if users_choice == 3:
        CarShowroom.save_showrooms_to_file()

    if users_choice == 4:
        CarShowroom.open_showrooms_list()

    if users_choice == 7:
        Car.open_car_list()
        Car.cars
