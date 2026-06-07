import numpy as np
import matplotlib.pyplot as plt

R = 6371
ALTITUDE = 1000

orbit_radius = R + ALTITUDE

inclination = np.radians(45)

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

earth_x = R*np.outer(np.cos(u), np.sin(v))
earth_y = R*np.outer(np.sin(u), np.sin(v))
earth_z = R*np.outer(np.ones(np.size(u)), np.cos(v))

theta = np.linspace(0, 2*np.pi, 1000)

x = orbit_radius*np.cos(theta)
y = orbit_radius*np.sin(theta)
z = np.zeros_like(theta)

# Rotate orbit plane
y_new = y*np.cos(inclination)
z_new = y*np.sin(inclination)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    earth_x,
    earth_y,
    earth_z
)

ax.plot(
    x,
    y_new,
    z_new,
    linewidth=2
)

ax.set_title("Inclined Orbit")

plt.show()
