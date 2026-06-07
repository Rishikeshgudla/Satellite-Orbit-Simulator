import numpy as np
import matplotlib.pyplot as plt

EARTH_RADIUS = 6371

orbits = [500, 2000, 35786]

theta = np.linspace(0, 2*np.pi, 1000)

earth_x = EARTH_RADIUS*np.cos(theta)
earth_y = EARTH_RADIUS*np.sin(theta)

plt.figure(figsize=(8,8))

plt.plot(earth_x, earth_y, label="Earth")

for alt in orbits:
    r = EARTH_RADIUS + alt

    x = r*np.cos(theta)
    y = r*np.sin(theta)

    plt.plot(x, y, label=f"{alt} km")

plt.axis("equal")
plt.grid(True)
plt.legend()

plt.title("LEO, MEO and GEO Orbits")

plt.show()