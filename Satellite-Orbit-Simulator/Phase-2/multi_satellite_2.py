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

    def __init__(self, name, altitude, inclination, eccentricity=0):

        self.name = name

        self.altitude = altitude

        self.inclination = np.radians(inclination)

        self.e = eccentricity

        self.G = 6.67430e-11
        
        self.M = 5.972e24

        self.a = EARTH_RADIUS + altitude

        self.theta = np.linspace(0, 2*np.pi, 500)

        r = self.a*(1-self.e**2) / (
            1 + self.e*np.cos(self.theta)
        )

        self.x = r*np.cos(self.theta)

        y = r*np.sin(self.theta)

        self.y = y*np.cos(self.inclination)

        self.z = y*np.sin(self.inclination)

        self.marker = None

        self.ground_marker = None

        self.trail = None

        self.trail_x = []

        self.trail_y = []

        self.trail_z = []

# ==========================================
# SATELLITES
# ==========================================

satellites = [

    Satellite("ISS",420,51.6,0.01),

    Satellite("GPS-1",20200,55,0.15),

    Satellite("WeatherSat",800,98,0.25),

    Satellite("DemoSat",500,30,0.4)

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

    sat.ground_marker, = ax.plot([], [], [], marker='x')

    sat.trail, = ax.plot([], [], [])

    max_radius = max(max_radius, sat.a)

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

earth_surface = ax.plot_surface(
    earth_x,
    earth_y,
    earth_z,
    alpha=0.5
)

# ==========================================
# Earth Rotation Function
# ==========================================

def rotate_earth(angle):

    cos_a = np.cos(angle)
    sin_a = np.sin(angle)

    x_rot = earth_x*cos_a - earth_y*sin_a
    y_rot = earth_x*sin_a + earth_y*cos_a

    return x_rot, y_rot

# ==========================================
# ANIMATION
# ==========================================

def update(frame):

    global earth_surface

    earth_surface.remove()

    angle = frame * 0.02

    x_rot, y_rot = rotate_earth(angle)

    earth_surface = ax.plot_surface(
    x_rot,
    y_rot,
    earth_z,
    alpha=0.5
    )

    info = ""

    for sat in satellites:

        index = frame % len(sat.theta)

        x = sat.x[index]
        y = sat.y[index]
        z = sat.z[index]

        r = np.sqrt(x**2 + y**2 + z**2) * 1000

        a_m = sat.a * 1000

        velocity = np.sqrt(
            sat.G * sat.M *
            (
                2/r -
                1/a_m
            )
        )

        velocity_km = velocity / 1000

        magnitude = np.sqrt(x**2 + y**2 + z**2)

        ground_x = EARTH_RADIUS * x / magnitude
        ground_y = EARTH_RADIUS * y / magnitude
        ground_z = EARTH_RADIUS * z / magnitude

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

        sat.ground_marker.set_data(
            [ground_x],
            [ground_y]
        )

        sat.ground_marker.set_3d_properties(
            [ground_z]
        )

        latitude = np.degrees(
            np.arcsin(z/magnitude)
        )

        longitude = np.degrees(
            np.arctan2(y, x)
        )

        info += (
            f"{sat.name}\n"
            f"Alt : {sat.altitude} km\n\n"
            f"Ecc : {sat.e:.2f}\n"
            f"Vel : {velocity_km:.2f} km/s\n"
            f"Lat : {latitude:.1f}°\n"
            f"Lon : {longitude:.1f}°\n\n"
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

