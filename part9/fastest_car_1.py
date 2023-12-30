class Car:
    def __init__(self,make,top_speed) -> None:
        self.make = make
        self.top_speed = top_speed

def fastest_car(cars):
    top = 0
    top_car = ""
    for car in cars:
        if(car.top_speed>top):
            top = car.top_speed
            top_car = car.make
    return top_car

if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))
