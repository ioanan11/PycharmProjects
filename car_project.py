class Car:
    def __init__(self, speed = 0, maxspeed=180):
        self._speed = 0
        self.__maxspeed = 180

    def get_speed(self):
        return self._speed

    def accelerate(self, a):
        if self._speed +a > self.__maxspeed:
            self._speed = self.__maxspeed
            print("You have reached maximum speed")
        else:
            self._speed += a


    def decelerate(self, d):
        if self._speed -d < 0:
            self._speed = 0
            print("You have reached 0 km/h")
        else:
            self._speed -= d


m = Car(0 , 180)
m.accelerate(15)
print(m.get_speed())
m.decelerate(30)
print(m.get_speed())