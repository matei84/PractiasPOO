from car import Car
from account import Account

if __name__=="__main__":
    print("Hola Mundo")
    car = Car("AMS234", Account("Andres Herrera", "ANDA876"))
    #car.license = "123-QWA"
    #car.driver = "Juan"
    print(vars(car))
    print(vars(car.driver))

    car2 = Car("AMS234+1", Account("Andres Herrera+1", "ANDA876+1"))
    #car2.license = "456-you"
    #car2.driver = "Alex"
    print(vars(car2))