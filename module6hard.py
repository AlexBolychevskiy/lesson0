
import math

class Figure:
    sides_count = 0
    def __init__(self,filled):
        self.__sides = []
        self.__color = []
        self.filled = filled
    def get_color(self):
        return self.__color
    def _is_valid_color(self,r,g,b):
        for i in range(255+1):
            if isinstance(r,int):
                self.__color.append(r)
            if isinstance(g,int):
                self.__color.append(g)
            if isinstance(b,int):
                self.__color.append(b)
            else:
                return self.__color
    def set_color(self,r,g,b):
        if isinstance(r, int) and r in range(255+1):
            self.__color.pop(0)
            self.__color.insert(0, r)
        if isinstance(g, int) and g in range(255+1):
            self.__color.pop(1)
            self.__color.insert(1, g)
        if isinstance(b, int) and b in range(255+1):
            self.__color.pop(2)
            self.__color.insert(2, b)
    def get_sides(self,*args):
        self.__sides.append(args)
        return self.__sides
    def _is_valid_sides(self,*args):
            if isinstance(args,int) and args in self.__sides:
                return True
            else:
                return False
    def __len__(self):
        return len(self.__sides)

    def set_sides(self, *new_sides):
        if isinstance(*new_sides, int) and len(*new_sides) == self.sides_count:
            self.__sides.append(*new_sides)
        else:
            return self.__sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, (r,g,b),area_of_circle, __radius,__sides):
        super().__init__(self)
        #if len(self.__sides) != self.sides_count:
        self.area_of_circle = area_of_circle
        self.__radius = len(self.__sides)/2 * math.pi
    def get_square(self):
        self.area_of_circle = math.pi * self.__radius ** 2
        return self.area_of_circle
class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        s = len(self.__sides)/2
        return (s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2])) ** 0.5
class Cube(Figure):
    sides_count = 12
    def get_volume(self):
        self.volume = self.__sides[0] ** 3
        return self.volume

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())









