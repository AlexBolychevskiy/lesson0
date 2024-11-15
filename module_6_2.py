class Vehicle:
    def __init__(self,owner,__model,__engine_power,__color):
       self.owner = owner
       self.__model = __model
       self.__engine_power = __engine_power
       self.__color = __color
       self.__COLOR_VARIANTS = ['BLUE', 'RED', 'GREEN', 'BLACK', 'WHITE']
    #__COLOR_VARIANTS = ['yellow','pink','purple','orange','black']
    def get_model(self):
        return f'Модель:{self.__model}'
    def get_horsepower (self):
        return f'Мощность двигателя:{self.__engine_power}'
    def  get_color(self):
        return f'Цвет:{self.__color}'
    def set_color(self,new_color):
        #new_color.lower()
        if new_color in self.__COLOR_VARIANTS:
           self.__color = new_color
        elif new_color not in self.__COLOR_VARIANTS:
            print(f'Нельзя сменить цвет на {new_color}')
        return self

    def print_info(self):
        print(Vehicle.get_model(self))
        print(Vehicle.get_horsepower(self))
        print(Vehicle.get_color(self))
        print(f'Владелец:{self.owner}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500,'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()