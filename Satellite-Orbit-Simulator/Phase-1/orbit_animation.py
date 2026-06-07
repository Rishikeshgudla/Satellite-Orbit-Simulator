import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

EARTH_RADIUS = 6371
ALTITUDE = 500

orbit_radius = EARTH_RADIUS + ALTITUDE

theta = np.linspace(0, 2*np.pi, 500)

orbit_x = orbit_radius * np.cos(theta)
orbit_y = orbit_radius * np.sin(theta)

earth_x = EARTH_RADIUS * np.cos(theta)
earth_y = EARTH_RADIUS * np.sin(theta)

fig, ax = plt.subplots(figsize=(8,8))

ax.plot(earth_x, earth_y)
ax.plot(orbit_x, orbit_y)

ax.set_aspect('equal')
ax.grid(True)

satellite, = ax.plot([], [], marker='o')

def update(frame):
    satellite.set_data(
        [orbit_x[frame]],
        [orbit_y[frame]]
    )
    return satellite,

ani = FuncAnimation(
    fig,
    update,
    frames=len(theta),
    interval=20,
    blit=True
)

plt.show()