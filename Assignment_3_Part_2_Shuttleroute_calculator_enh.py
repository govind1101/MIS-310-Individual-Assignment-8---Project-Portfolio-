# Problem 2 - Shuttle Route Calculator
# Part c - Fastest Shuttle Route with Validation

fastest_time = None
fastest_route = None
route_number = 1

while True:

    # Distance Input with Validation
    while True:
        try:
            distance = float(input(f"Enter route {route_number} distance (miles): "))
            if distance <= 0:
                print("Distance must be positive. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Enter a numeric value.")

    # Speed Input with Validation
    while True:
        try:
            speed = float(input(f"Enter route {route_number} speed (miles/hour): "))
            if speed <= 0:
                print("Speed must be positive. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Enter a numeric value.")

    # ---- Calculate Time ----
    time_minutes = (distance / speed) * 60
    print(f"Route {route_number} will take {time_minutes:.1f} minutes.\n")

    # ---- Check Fastest ----
    if fastest_time is None or time_minutes < fastest_time:
        fastest_time = time_minutes
        fastest_route = route_number

    # ---- Ask for More Routes ----
    more = input("More routes (y/n)?: ")
    if more.lower() != 'y':
        break

    route_number += 1