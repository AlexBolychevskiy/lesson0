import math
import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self,_cords,speed,dx,dy,dz):
        self._cords = [0,0,0]
        self.speed = speed
        self.dx = dx
        self.dy = dy
        self.dz = dz
    def move(self):
        self.dx = dx * self.speed
        self.dy = dy * self.speed
        self.dz = dz * self.speed
        self._cords.pop(0)
        self._cords.insert(0,self.dx)
        self._cords.pop(1)
        self._cords.insert(1, self.dy)
        self._cords.pop(2)
        self._cords.insert(2, self.dz)
    def get_cords(self):
        print(f'X:{self.dx}')
        print(f'Y:{self.dy}')
        print(f'Z:{self.dz}')
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
class Bird(Animal):
    beak =True
    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1,4)} eggs for you')
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self):
        self.dz = self.dz - abs(self.dz) * self.speed/2
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Animal,Bird,AquaticAnimal,PoisonousAnimal):
    sound = "Click-click-click"
    #def __init__(self):
    super().attack()
    super().move()
    super().get_cords()
    super().dive_in()
    super().lay_eggs()


    def speak(self):
        self.sound = "Click-click-click"
        print(self.sound)





print(Duckbill.mro())

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()





