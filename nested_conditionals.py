print("="*25)
print("Welcome to Ride Builder!")
print("="*25)
choice = int(input("Enter 1 for Bike, 2 for Car:"))
if choice == 1:
    bike_type = int(input("Enter 1 for Scooty, 2 for Mountain Bike."))
    if bike_type == 1:
        print("You picked Scooty.")
        print("It has two seats")
        print("It is good for city roads.")
    else :
        print("You picked Mountain Bike.")
        print("It has two seats")
        print("It is good for mountain trails.")
if choice == 2:
    car_type = int(input("Enter 1 for Sedan, 2 for SUV."))
    if car_type == 1:
        print("You picked Sedan.")
        print("It has 5 seats.")
        print("It is good for family trips.")
    else :
        print("You picked SUV.")
        print("It has 7 seats.")
        print("It is best for off road adventures.")
else:
    print("Please select 1 for Bike or 2 for Car.")