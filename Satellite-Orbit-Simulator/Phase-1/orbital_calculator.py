import math

G = 6.67430e-11
M = 5.972e24

EARTH_RADIUS = 6371e3

altitude = float(input("Enter altitude (km): "))

r = EARTH_RADIUS + altitude*1000

velocity = math.sqrt((G*M)/r)

period = 2*math.pi*math.sqrt((r**3)/(G*M))

print()
print("------ Orbit Parameters ------")
print(f"Altitude : {altitude:.0f} km")
print(f"Velocity : {velocity/1000:.2f} km/s")
print(f"Period   : {period/60:.2f} minutes")