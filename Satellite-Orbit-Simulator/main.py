import numpy as np
import matplotlib.pyplot as plt

EARTH_RADIUS = 6371
ALTITUDE = 1000

orbit_radius = EARTH_RADIUS + ALTITUDE

theta = np.linspace(0, 2*np.pi, 1000)

earth_x = EARTH_RADIUS * np.cos(theta)
earth_y = EARTH_RADIUS * np.sin(theta)

orbit_x = orbit_radius * np.cos(theta)
orbit_y = orbit_radius * np.sin(theta)

satellite_x = orbit_x[200]
satellite_y = orbit_y[200]

plt.figure(figsize=(8,8))

plt.plot(earth_x, earth_y, label="Earth")
plt.plot(orbit_x, orbit_y, label="Orbit")

plt.scatter(
    satellite_x,
    satellite_y,
    s=100
)

plt.text(
    satellite_x,
    satellite_y,
    " Satellite"
)

plt.axis('equal')
plt.grid(True)
plt.legend()

plt.show()