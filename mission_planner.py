def show_menu():

    print()
    print("="*40)
    print(" SATELLITE MISSION PLANNER ")
    print("="*40)

    print("1. ISS")
    print("2. GPS Satellite")
    print("3. Weather Satellite")
    print("4. Custom Satellite")

    choice = input("\nSelect option: ")

    return choice

choice = show_menu()

if choice == "1":

    satellite = {
        "name": "ISS",
        "altitude": 420,
        "inclination": 51.6
    }

elif choice == "2":

    satellite = {
        "name": "GPS",
        "altitude": 20200,
        "inclination": 55
    }

elif choice == "3":

    satellite = {
        "name": "WeatherSat",
        "altitude": 800,
        "inclination": 98
    }

elif choice == "4":

    name = input("Satellite Name: ")

    altitude = float(
        input("Altitude (km): ")
    )

    inclination = float(
        input("Inclination (deg): ")
    )

    satellite = {
        "name": name,
        "altitude": altitude,
        "inclination": inclination
    }

else:

    print("Invalid Choice")
    exit()

print("\nMission Parameters")
print("-"*30)

print(
    f"Name        : {satellite['name']}"
)

print(
    f"Altitude    : {satellite['altitude']} km"
)

print(
    f"Inclination : {satellite['inclination']} deg"
)