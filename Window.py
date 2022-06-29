import PIL.Image
from Car import *
from Garage import *
from CarShowroom import *

bmw_showroom = CarShowroom('BMW Showroom')


bmw = Car('BMW X5', 250, 1800, 2019, 'P:\Zadania i funkcje\Obrazk\\bmw-x5.jpg')
bmw1 = Car('BMW X8', 370, 1600, 2015, 'path')

# bmw_showroom.add_car_to_car_showroom(bmw)
# bmw_showroom.add_car_to_car_showroom(bmw1)
#
# bmw.get_car_name()
# # bmw.show_car_image()
#
# # user_choice_car = bmw_showroom.get_user_input_car()
#
# garage = Garage()
#
# # garage.add_car_to_garage(user_choice_car)
# garage.print_garage()
#
# print(bmw.name)