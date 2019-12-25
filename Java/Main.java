class Main{
    public static void main(final String[] args) {
        System.out.println("Hola mundo que loco es leo");
        Car car = new Car("AMQ-123", new Account("Andres Herrero", "Andres-123"));
        car.passanger = 4;
        //System.out.println("Car License: " + car.license);
        Car car2 = new Car("AMQ-124", new Account("Andres Herrero", "Y2705348Z"));
        //car2.passanger = 5;

        car.printDataCar();
        car2.printDataCar();       
    }
}