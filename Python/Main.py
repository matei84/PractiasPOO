from Car import car
if __name__=="__main__":
    print("Hola Mundo")
    car = Car()
    car.license = "123-QWA"
    car.driver = "Juan"
    print(vars(car))

    car2 = Car()
    car2.license = "456-you"
    car2.driver = "Alex"
    print(vars(car2))