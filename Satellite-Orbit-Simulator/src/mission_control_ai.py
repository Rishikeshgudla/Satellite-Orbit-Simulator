import json
import random
from datetime import datetime

# ==========================================
# DATABASE
# ==========================================

satellites = []

# ==========================================
# CREATE SATELLITE
# ==========================================

def create_satellite():

    print("\n=== Create Satellite ===")

    name = input("Satellite Name: ")

    altitude = float(
        input("Altitude (km): ")
    )

    inclination = float(
        input("Inclination (deg): ")
    )

    eccentricity = float(
        input("Eccentricity (0-0.9): ")
    )

    satellite = {

        "name": name,

        "altitude": altitude,

        "inclination": inclination,

        "eccentricity": eccentricity,

        "health": 100
    }

    satellites.append(
        satellite
    )

    print(
        f"\n{name} added successfully!"
    )

# ==========================================
# VIEW SATELLITES
# ==========================================

def view_satellites():

    if len(satellites) == 0:

        print("\nNo satellites available.")

        return

    print("\n=== Satellite Database ===\n")

    for i, sat in enumerate(
        satellites,
        start=1
    ):

        print(
            f"{i}. {sat['name']}"
        )

        print(
            f"   Altitude     : {sat['altitude']} km"
        )

        print(
            f"   Inclination  : {sat['inclination']} deg"
        )

        print(
            f"   Eccentricity : {sat['eccentricity']}"
        )

        print(
            f"   Health       : {sat['health']}%"
        )

        print("-" * 40)

# ==========================================
# SAVE MISSION
# ==========================================

def save_mission():

    try:

        with open(
            "mission.json",
            "w"
        ) as file:

            json.dump(
                satellites,
                file,
                indent=4
            )

        print(
            "\nMission saved successfully!"
        )

    except Exception as e:

        print(
            f"\nError saving mission: {e}"
        )

# ==========================================
# LOAD MISSION
# ==========================================

def load_mission():

    global satellites

    try:

        with open(
            "mission.json",
            "r"
        ) as file:

            satellites = json.load(
                file
            )

        print(
            "\nMission loaded successfully!"
        )

    except FileNotFoundError:

        print(
            "\nmission.json not found."
        )

    except Exception as e:

        print(
            f"\nError loading mission: {e}"
        )

# ==========================================
# HEALTH SIMULATION
# ==========================================

def simulate_health():

    if len(satellites) == 0:

        print(
            "\nNo satellites available."
        )

        return

    print("\n=== Health Simulation ===\n")

    for sat in satellites:

        loss = random.randint(
            0,
            5
        )

        sat["health"] -= loss

        if sat["health"] < 0:

            sat["health"] = 0

        print(
            f"{sat['name']} -> "
            f"{sat['health']}%"
        )

# ==========================================
# MISSION REPORT
# ==========================================

def generate_report():

    print()

    print("=" * 60)

    print("MISSION REPORT")

    print("=" * 60)

    print(
        f"Generated: {datetime.now()}"
    )

    print()

    print(
        f"Total Satellites: "
        f"{len(satellites)}"
    )

    print()

    for sat in satellites:

        print(
            f"Satellite Name : "
            f"{sat['name']}"
        )

        print(
            f"Altitude       : "
            f"{sat['altitude']} km"
        )

        print(
            f"Inclination    : "
            f"{sat['inclination']} deg"
        )

        print(
            f"Eccentricity   : "
            f"{sat['eccentricity']}"
        )

        print(
            f"Health         : "
            f"{sat['health']}%"
        )

        print("-" * 40)

# ==========================================
# DELETE SATELLITE
# ==========================================

def delete_satellite():

    if len(satellites) == 0:

        print(
            "\nNo satellites available."
        )

        return

    view_satellites()

    try:

        index = int(
            input(
                "\nEnter satellite number to delete: "
            )
        )

        deleted = satellites.pop(
            index - 1
        )

        print(
            f"\n{deleted['name']} deleted."
        )

    except:

        print(
            "\nInvalid selection."
        )

# ==========================================
# MAIN MENU
# ==========================================

while True:

    print()

    print("=" * 60)
    print("        MISSION CONTROL AI")
    print("=" * 60)

    print("1. Create Satellite")
    print("2. View Satellites")
    print("3. Save Mission")
    print("4. Load Mission")
    print("5. Simulate Health")
    print("6. Generate Report")
    print("7. Delete Satellite")
    print("8. Exit")

    choice = input(
        "\nSelect Option: "
    )

    if choice == "1":

        create_satellite()

    elif choice == "2":

        view_satellites()

    elif choice == "3":

        save_mission()

    elif choice == "4":

        load_mission()

    elif choice == "5":

        simulate_health()

    elif choice == "6":

        generate_report()

    elif choice == "7":

        delete_satellite()

    elif choice == "8":

        print(
            "\nMission Control Closed."
        )

        break

    else:

        print(
            "\nInvalid Option."
        )