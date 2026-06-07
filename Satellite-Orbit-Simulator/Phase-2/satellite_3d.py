import numpy as np
import matplotlib.pyplot as plt

R = 6371
ALTITUDE = 1000

orbit_radius = R + ALTITUDE

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

earth_x = R * np.outer(np.cos(u), np.sin(v))
earth_y = R * np.outer(np.sin(u), np.sin(v))
earth_z = R * np.outer(np.ones(np.size(u)), np.cos(v))

theta = np.linspace(0, 2*np.pi, 1000)

orbit_x = orbit_radius*np.cos(theta)
orbit_y = orbit_radius*np.sin(theta)
orbit_z = np.zeros_like(theta)

sat_index = 200

sat_x = orbit_x[sat_index]
sat_y = orbit_y[sat_index]
sat_z = orbit_z[sat_index]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    earth_x,
    earth_y,
    earth_z
)

ax.plot(
    orbit_x,
    orbit_y,
    orbit_z
)

ax.scatter(
    sat_x,
    sat_y,
    sat_z,
    s=100
)

ax.text(
    sat_x,
    sat_y,
    sat_z,
    "Satellite"
)

ax.set_title("3D Earth + Satellite")

plt.show()