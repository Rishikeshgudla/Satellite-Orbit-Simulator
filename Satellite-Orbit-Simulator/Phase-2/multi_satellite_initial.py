import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# ==========================================
# CONSTANTS
# ==========================================

EARTH_RADIUS = 6371

G = 6.67430e-11
M = 5.972e24

# ==========================================
# SATELLITE CLASS
# ==========================================

class Satellite:

    def __init__(self, name, altitude, inclination):

        self.name = name

        self.altitude = altitude

        self.inclination = np.radians(inclination)

        self.radius = EARTH_RADIUS + altitude

        self.theta = np.linspace(0, 2*np.pi, 500)

        self.x = self.radius*np.cos(self.theta)

        y = self.radius*np.sin(self.theta)

        self.y = y*np.cos(self.inclination)

        self.z = y*np.sin(self.inclination)

        self.marker = None

        self.trail = None

        self.trail_x = []

        self.trail_y = []

        self.trail_z = []

# ==========================================
# SATELLITES
# ==========================================

satellites = [

    Satellite("ISS", 420, 51.6),

    Satellite("GPS-1", 20200, 55),

    Satellite("WeatherSat", 800, 98),

    Satellite("DemoSat", 500, 30)

]

# ==========================================
# EARTH
# ==========================================

u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, np.pi, 50)

earth_x = EARTH_RADIUS*np.outer(np.cos(u), np.sin(v))
earth_y = EARTH_RADIUS*np.outer(np.sin(u), np.sin(v))
earth_z = EARTH_RADIUS*np.outer(np.ones(np.size(u)), np.cos(v))

# ==========================================
# FIGURE
# ==========================================

fig = plt.figure(figsize=(12,10))

ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    earth_x,
    earth_y,
    earth_z,
    alpha=0.5
)

# ==========================================
# DRAW ORBITS
# ==========================================

max_radius = 0

for sat in satellites:

    ax.plot(
        sat.x,
        sat.y,
        sat.z
    )

    sat.marker, = ax.plot([], [], [], marker='o')

    sat.trail, = ax.plot([], [], [])

    max_radius = max(max_radius, sat.radius)

# ==========================================
# LIMITS
# ==========================================

limit = max_radius * 1.2

ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit, limit)

ax.set_title("Multi-Satellite Constellation")

# ==========================================
# DASHBOARD
# ==========================================

dashboard = ax.text2D(
    0.02,
    0.95,
    "",
    transform=ax.transAxes
)

# ==========================================
# ANIMATION
# ==========================================

def update(frame):

    info = ""

    for sat in satellites:

        index = frame % len(sat.theta)

        x = sat.x[index]
        y = sat.y[index]
        z = sat.z[index]

        sat.marker.set_data([x], [y])
        sat.marker.set_3d_properties([z])

        sat.trail_x.append(x)
        sat.trail_y.append(y)
        sat.trail_z.append(z)

        sat.trail.set_data(
            sat.trail_x,
            sat.trail_y
        )

        sat.trail.set_3d_properties(
            sat.trail_z
        )

        info += (
            f"{sat.name}\n"
            f"Alt: {sat.altitude} km\n\n"
        )

    dashboard.set_text(info)

    return []

ani = FuncAnimation(
    fig,
    update,
    frames=500,
    interval=20
)

plt.show()