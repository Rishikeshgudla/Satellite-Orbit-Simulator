import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# ==================================
# USER INPUT
# ==================================

sat_name = input("Satellite Name: ")

altitude = float(input("Altitude (km): "))
inclination_deg = float(input("Inclination (deg): "))

# ==================================
# CONSTANTS
# ==================================

EARTH_RADIUS = 6371
G = 6.67430e-11
M = 5.972e24

inclination = np.radians(inclination_deg)

orbit_radius = EARTH_RADIUS + altitude

# ==================================
# VELOCITY AND PERIOD
# ==================================

r_meters = orbit_radius * 1000

velocity = math.sqrt((G*M)/r_meters)

period = 2*np.pi*np.sqrt((r_meters**3)/(G*M))

# ==================================
# EARTH
# ==================================

u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, np.pi, 50)

earth_x = EARTH_RADIUS*np.outer(np.cos(u), np.sin(v))
earth_y = EARTH_RADIUS*np.outer(np.sin(u), np.sin(v))
earth_z = EARTH_RADIUS*np.outer(np.ones(np.size(u)), np.cos(v))

# ==================================
# ORBIT
# ==================================

theta = np.linspace(0, 2*np.pi, 500)

x = orbit_radius*np.cos(theta)
y = orbit_radius*np.sin(theta)
z = np.zeros_like(theta)

y_rot = y*np.cos(inclination)
z_rot = y*np.sin(inclination)

# ==================================
# FIGURE
# ==================================

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    earth_x,
    earth_y,
    earth_z,
    alpha=0.5
)

ax.plot(
    x,
    y_rot,
    z_rot
)

satellite, = ax.plot([], [], [], marker='o')

trail, = ax.plot([], [], [])

trail_x = []
trail_y = []
trail_z = []

limit = orbit_radius * 1.2

ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit, limit)

# ==================================
# DASHBOARD TEXT
# ==================================

dashboard = ax.text2D(
    0.02,
    0.95,
    "",
    transform=ax.transAxes
)

# ==================================
# UPDATE FUNCTION
# ==================================

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

    dashboard.set_text(
        f"Satellite : {sat_name}\n"
        f"Altitude  : {altitude:.0f} km\n"
        f"Velocity  : {velocity/1000:.2f} km/s\n"
        f"Period    : {period/60:.2f} min\n\n"
        f"X = {sat_x:.0f} km\n"
        f"Y = {sat_y:.0f} km\n"
        f"Z = {sat_z:.0f} km"
    )

    return satellite, trail

ani = FuncAnimation(
    fig,
    update,
    frames=len(theta),
    interval=20
)

plt.show()