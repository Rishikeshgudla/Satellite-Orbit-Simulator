import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

EARTH_RADIUS = 6371

G = 6.67430e-11
M = 5.972e24

# =========================
# Mission Inputs
# =========================

print()
print("="*50)
print(" 3D ORBIT DESIGNER ")
print("="*50)

name = input("Satellite Name : ")

altitude = float(
    input("Altitude (km) : ")
)

inclination_deg = float(
    input("Inclination (deg) : ")
)

eccentricity = float(
    input("Eccentricity (0-0.9) : ")
)

# =========================
# ORBIT CALCULATIONS
# =========================


a = EARTH_RADIUS + altitude

inclination = np.radians(
    inclination_deg
)

r_m = a * 1000

velocity = math.sqrt(
    (G*M)/r_m
)

period = (
    2*np.pi*
    np.sqrt(
        r_m**3/(G*M)
    )
)

velocity_km = velocity/1000

period_min = period/60

# =========================
# EARTH
# =========================

u = np.linspace(
    0,
    2*np.pi,
    50
)

v = np.linspace(
    0,
    np.pi,
    50
)

earth_x = (
    EARTH_RADIUS*
    np.outer(
        np.cos(u),
        np.sin(v)
    )
)

earth_y = (
    EARTH_RADIUS*
    np.outer(
        np.sin(u),
        np.sin(v)
    )
)

earth_z = (
    EARTH_RADIUS*
    np.outer(
        np.ones(np.size(u)),
        np.cos(v)
    )
)

# =========================
# Elliptical ORBIT     
# =========================

theta = np.linspace(
    0,
    2*np.pi,
    1000
)

r = (
    a*(1-eccentricity**2)
) / (
    1 +
    eccentricity*np.cos(theta)
)

x = r*np.cos(theta)

y = r*np.sin(theta)

z = np.zeros_like(theta)

y_rot = (
    y*np.cos(inclination)
)

z_rot = (
    y*np.sin(inclination)
)

# =========================
# FIGURE
# =========================

fig = plt.figure(
    figsize=(12,10)
)

ax = fig.add_subplot(
    111,
    projection='3d'
)

ax.plot_surface(
    earth_x,
    earth_y,
    earth_z,
    alpha=0.5
)

ax.plot(
    x,
    y_rot,
    z_rot,
    linewidth=2
)

# =========================
# Satellite Marker
# ========================= 

satellite, = ax.plot(
    [],
    [],
    [],
    marker='o'
)

trail, = ax.plot(
    [],
    [],
    []
)

trail_x = []
trail_y = []
trail_z = []

# =========================
# DASHBOARD
# ========================= 

dashboard = ax.text2D(
    0.02,
    0.95,
    "",
    transform=ax.transAxes
)

# =========================
# Animation Update Function
# =========================     

def update(frame):

    sat_x = x[frame]
    sat_y = y_rot[frame]
    sat_z = z_rot[frame]

    satellite.set_data(
        [sat_x],
        [sat_y]
    )

    satellite.set_3d_properties(
        [sat_z]
    )

    trail_x.append(sat_x)
    trail_y.append(sat_y)
    trail_z.append(sat_z)

    trail.set_data(
        trail_x,
        trail_y
    )

    trail.set_3d_properties(
        trail_z
    )

    dashboard.set_text(
        f"Satellite : {name}\n"
        f"Altitude : {altitude:.0f} km\n"
        f"Inclination : {inclination_deg:.1f}°\n"
        f"Eccentricity : {eccentricity:.2f}\n"
        f"Velocity : {velocity_km:.2f} km/s\n"
        f"Period : {period_min:.2f} min"
    )

    ax.view_init(
        elev=25,
        azim=frame/5
    )

    return satellite, trail

# =========================
# Plot Limits                   
# =========================

limit = np.max(r)*1.2

ax.set_xlim(
    -limit,
    limit
)

ax.set_ylim(
    -limit,
    limit
)

ax.set_zlim(
    -limit,
    limit
)

ax.set_title(
    "3D Orbit Designer"
)

# =========================
# Run Animation
# ========================

ani = FuncAnimation(
    fig,
    update,
    frames=len(theta),
    interval=20
)

plt.show() 