import numpy as np
import matplotlib.pyplot as plt
import math

EARTH_RADIUS = 6371      # km

G = 6.67430e-11
M = 5.972e24

def get_mission():

    print()
    print("="*50)
    print(" ORBIT DESIGNER TOOL ")
    print("="*50)

    name = input(
        "Satellite Name : "
    )

    altitude = float(
        input("Altitude (km) : ")
    )

    inclination = float(
        input("Inclination (deg) : ")
    )

    eccentricity = float(
        input("Eccentricity (0 to 0.9) : ")
    )

    return (
        name,
        altitude,
        inclination,
        eccentricity
    )

def calculate_orbit(
    altitude,
    eccentricity
):

    a = EARTH_RADIUS + altitude

    perigee = a*(1-eccentricity)

    apogee = a*(1+eccentricity)

    r_m = a*1000

    velocity = math.sqrt(
        (G*M)/r_m
    )

    period = (
        2*np.pi*
        np.sqrt(
            r_m**3/(G*M)
        )
    )

    return (
        a,
        perigee,
        apogee,
        velocity/1000,
        period/60
    )

(
    name,
    altitude,
    inclination,
    eccentricity
) = get_mission()

(
    a,
    perigee,
    apogee,
    velocity,
    period
) = calculate_orbit(
    altitude,
    eccentricity
)

print()
print("="*50)
print(" MISSION REPORT ")
print("="*50)

print(
    f"Satellite    : {name}"
)

print(
    f"Altitude     : {altitude:.0f} km"
)

print(
    f"Inclination  : {inclination:.1f} deg"
)

print(
    f"Eccentricity : {eccentricity:.2f}"
)

print(
    f"Perigee      : {perigee:.0f} km"
)

print(
    f"Apogee       : {apogee:.0f} km"
)

print(
    f"Velocity     : {velocity:.2f} km/s"
)

print(
    f"Period       : {period:.2f} min"
)

theta = np.linspace(
    0,
    2*np.pi,
    1000
)

r = (
    a*(1-eccentricity**2)
) / (
    1 +
    eccentricity*np.cos(theta)
)

x = r*np.cos(theta)
y = r*np.sin(theta)

earth_x = (
    EARTH_RADIUS*
    np.cos(theta)
)

earth_y = (
    EARTH_RADIUS*
    np.sin(theta)
)

plt.figure(figsize=(8,8))

plt.plot(
    x,
    y,
    label=name
)

plt.plot(
    earth_x,
    earth_y,
    label="Earth"
)

plt.axis("equal")

plt.grid(True)

plt.legend()

plt.title(
    f"{name} Orbit"
)

plt.show()