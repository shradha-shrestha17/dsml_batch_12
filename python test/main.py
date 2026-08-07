from vehicles import Bike, Car
from decorators import ride_logger
from exceptions import InvalidDistanceError

@ride_logger
def book_ride():
    vehicle_type = input("ENter vehicle type(bike/car:)")
    driver = input("Enter driver name:")
    distance = float(input("Enter distance:"))
    rating = float(input("Enter rating:"))

    if distance<=0:
        raise InvalidDistanceError("Distance must be greater than 0km")

    if vehicle_type == "bike":
        vehicle = Bike(driver, rating)
    elif vehicle_type == "car":
        vehicle = Car(driver, rating)
    else:
        print("Invalid vehicle type.")
        return

    fare = vehicle.calculate_fare(distance)

    
    print("------------------------------")
    print("Driver:", driver)
    print("Vehicle:", vehicle_type)
    print("Distance:", distance, "km")
    print("Fare: RS.", fare)

    try:
        with open("ride_history.txt", "a")as file:
            file.write(
                f"Driver: {driver},"
                f"Vehicle: {vehicle_type},"
                f"Distance: {distance} km,"
                f"Fare: RS. {fare}"

            )
    except Exception as e:
        print("Error", e)

try:
    book_ride()
except Exception as e:
    print("Error", e)