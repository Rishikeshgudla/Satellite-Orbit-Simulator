import numpy as np
import matplotlib.pyplot as plt

EARTH_RADIUS = 6371

altitude = float(input("Enter satellite altitude (km): "))

orbit_radius = EARTH_RADIUS + altitude

theta = np.linspace(0, 2*np.pi, 1000)

earth_x = EARTH_RADIUS * np.cos(theta)
earth_y = EARTH_RADIUS * np.sin(theta)

orbit_x = orbit_radius * np.cos(theta)
orbit_y = orbit_radius * np.sin(theta)

plt.figure(figsize=(8,8))

plt.plot(earth_x, earth_y, label="Earth")
plt.plot(orbit_x, orbit_y, label=f"Orbit ({altitude} km)")

plt.title("User Controlled Satellite Orbit")
plt.axis("equal")
plt.grid(True)
plt.legend()

plt.show()
