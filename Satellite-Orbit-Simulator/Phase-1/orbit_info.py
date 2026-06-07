import math

G = 6.67430e-11
M = 5.972e24

EARTH_RADIUS = 6371e3
ALTITUDE = 500e3

r = EARTH_RADIUS + ALTITUDE

velocity = math.sqrt((G*M)/r)

period = 2 * math.pi * math.sqrt((r**3)/(G*M))

print()
print("Satellite Information")
print("---------------------")
print(f"Altitude : {ALTITUDE/1000:.0f} km")
print(f"Velocity : {velocity/1000:.2f} km/s")
print(f"Period   : {period/60:.2f} minutes")
