import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------------
# USER INPUT
# ------------------------

EARTH_RADIUS = 6371

altitude = float(input("Enter satellite altitude (km): "))
inclination_deg = float(input("Enter inclination (degrees): "))

inclination = np.radians(inclination_deg)

orbit_radius = EARTH_RADIUS + altitude

# ------------------------
# EARTH
# ------------------------

u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, np.pi, 50)

earth_x = EARTH_RADIUS * np.outer(np.cos(u), np.sin(v))
earth_y = EARTH_RADIUS * np.outer(np.sin(u), np.sin(v))
earth_z = EARTH_RADIUS * np.outer(np.ones(np.size(u)), np.cos(v))

# ------------------------
# ORBIT
# ------------------------

theta = np.linspace(0, 2*np.pi, 500)

x = orbit_radius * np.cos(theta)
y = orbit_radius * np.sin(theta)
z = np.zeros_like(theta)

# Apply inclination
y_rot = y * np.cos(inclination)
z_rot = y * np.sin(inclination)

# ------------------------
# FIGURE
# ------------------------

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    earth_x,
    earth_y,
    earth_z,
    alpha=0.6
)

ax.plot(
    x,
    y_rot,
    z_rot,
    linewidth=1
)

satellite, = ax.plot([], [], [], marker='o')

trail, = ax.plot([], [], [])

trail_x = []
trail_y = []
trail_z = []

# ------------------------
# LIMITS
# ------------------------

limit = orbit_radius * 1.2

ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit, limit)

ax.set_title("Animated Satellite Orbit")

# ------------------------
# ANIMATION
# ------------------------

def update(frame):

    sat_x = x[frame]
    sat_y = y_rot[frame]
    sat_z = z_rot[frame]

    satellite.set_data([sat_x], [sat_y])
    satellite.set_3d_properties([sat_z])

    trail_x.append(sat_x)
    trail_y.append(sat_y)
    trail_z.append(sat_z)

    trail.set_data(trail_x, trail_y)
    trail.set_3d_properties(trail_z)

    return satellite, trail

ani = FuncAnimation(
    fig,
    update,
    frames=len(theta),
    interval=20,
    blit=False
)

plt.show()