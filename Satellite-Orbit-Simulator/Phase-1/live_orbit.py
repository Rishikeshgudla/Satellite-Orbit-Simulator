import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

EARTH_RADIUS = 6371
ALTITUDE = 500

r = EARTH_RADIUS + ALTITUDE

theta = np.linspace(0, 2*np.pi, 500)

orbit_x = r*np.cos(theta)
orbit_y = r*np.sin(theta)

earth_x = EARTH_RADIUS*np.cos(theta)
earth_y = EARTH_RADIUS*np.sin(theta)

fig, ax = plt.subplots(figsize=(8,8))

ax.plot(earth_x, earth_y)
ax.plot(orbit_x, orbit_y)

ax.set_aspect('equal')
ax.grid()

satellite, = ax.plot([], [], 'o')

trail, = ax.plot([], [])

trail_x = []
trail_y = []

def update(frame):

    x = orbit_x[frame]
    y = orbit_y[frame]

    satellite.set_data([x], [y])

    trail_x.append(x)
    trail_y.append(y)

    trail.set_data(trail_x, trail_y)

    return satellite, trail

ani = FuncAnimation(
    fig,
    update,
    frames=len(theta),
    interval=30,
    blit=True
)

plt.show()
