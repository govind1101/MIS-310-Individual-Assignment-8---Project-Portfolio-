# Problem 2 - Shuttle Route Calculator
# Part a - Determine the Fastest Route

fastest_time = None
fastest_route = None
route_number = 1

while True:
    #Prompt for Distance and Speed
    distance = float(input(f"Enter route {route_number} distance (miles): "))
    speed = float(input(f"Enter route {route_number} speed (miles/hours): "))

    # Calculate time in minutes
    time_minutes = (distance/speed) * 60
    print(f"Route {route_number} will take {time_minutes:.1f} minutes. \n")

    #Check if this is the fastest route
    if fastest_time is None or time_minutes < fastest_time:
        fastest_time = time_minutes
        fastest_route = route_number
    #Ask if there are more routes
    more = input("More routes (y/n)?: ")
    if more != 'y':
        break
    route_number += 1
print(f"\n{fastest_route} is the fastest route at {fastest_time:.1f} minutes ")
