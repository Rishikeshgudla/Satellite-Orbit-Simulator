import numpy as np
import matplotlib.pyplot as plt

EARTH_RADIUS = 6371

a = 12000          # Semi-major axis
e = 0.4            # Eccentricity

theta = np.linspace(0, 2*np.pi, 1000)

r = a*(1-e**2)/(1+e*np.cos(theta))

x = r*np.cos(theta)
y = r*np.sin(theta)

earth_x = EARTH_RADIUS*np.cos(theta)
earth_y = EARTH_RADIUS*np.sin(theta)

plt.figure(figsize=(8,8))

plt.plot(x, y, label="Satellite Orbit")
plt.plot(earth_x, earth_y, label="Earth")

plt.axis('equal')
plt.grid(True)
plt.legend()

plt.title("Elliptical Orbit")

plt.show()