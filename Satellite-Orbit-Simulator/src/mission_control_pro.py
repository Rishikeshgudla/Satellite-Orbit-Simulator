import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

EARTH_RADIUS = 6371

G = 6.67430e-11
M = 5.972e24

class Satellite:

    def __init__(
        self,
        name,
        altitude,
        inclination,
        eccentricity,
        color
    ):

        self.name = name

        self.altitude = altitude

        self.inclination = np.radians(
            inclination
        )

        self.e = eccentricity

        self.color = color

        self.a = (
            EARTH_RADIUS +
            altitude
        )

        self.theta = np.linspace(
            0,
            2*np.pi,
            1000
        )

        r = (
            self.a*
            (1-self.e**2)
        ) / (
            1 +
            self.e*np.cos(
                self.theta
            )
        )

        self.x = r*np.cos(
            self.theta
        )

        y = r*np.sin(
            self.theta
        )

        self.y = (
            y*np.cos(
                self.inclination
            )
        )

        self.z = (
            y*np.sin(
                self.inclination
            )
        )

# =========================
# Satellites
# =========================

satellites = [

    Satellite(
        "ISS",
        420,
        51.6,
        0.01,
        "red"
    ),

    Satellite(
        "GPS",
        20200,
        55,
        0.15,
        "blue"
    ),

    Satellite(
        "WeatherSat",
        800,
        98,
        0.20,
        "green"
    )

]

# ==========================================
# Earth
# ==========================================    

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

# ==========================================
# Figure                                    
# ==========================================

fig = plt.figure(
    figsize=(14,10)
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

# =========================
# Orbits 
# =========================

markers = []

for sat in satellites:

    ax.plot(
        sat.x,
        sat.y,
        sat.z,
        color=sat.color
    )

    marker, = ax.plot(
        [],
        [],
        [],
        marker='o',
        color=sat.color
    )

    markers.append(
        marker
    )

    # Perigee

    ax.scatter(
        sat.x[0],
        sat.y[0],
        sat.z[0],
        marker='^',
        s=60
    )

    # Apogee

    mid = len(
        sat.theta
    ) // 2

    ax.scatter(
        sat.x[mid],
        sat.y[mid],
        sat.z[mid],
        marker='s',
        s=60
    )

# =========================
# Dashboard
# ========================= 

dashboard = ax.text2D(
    0.02,
    0.95,
    "",
    transform=ax.transAxes
)

event_log = ax.text2D(
    0.75,
    0.95,
    "",
    transform=ax.transAxes
)

# ==========================================
# Collision Check Function
# ==========================================

def distance(
    sat1,
    sat2,
    frame
):

    p1 = np.array([

        sat1.x[frame],
        sat1.y[frame],
        sat1.z[frame]

    ])

    p2 = np.array([

        sat2.x[frame],
        sat2.y[frame],
        sat2.z[frame]

    ])

    return np.linalg.norm(
        p1-p2
    )

# =========================================
# Animation Update Function 
# ========================================  

def update(frame):

    info = ""

    events = ""

    for i,sat in enumerate(
        satellites
    ):

        x = sat.x[frame]
        y = sat.y[frame]
        z = sat.z[frame]

        markers[i].set_data(
            [x],
            [y]
        )

        markers[i].set_3d_properties(
            [z]
        )

        info += (
            f"{sat.name}\n"
            f"Alt: {sat.altitude} km\n"
            f"Ecc: {sat.e}\n\n"
        )

    d = distance(
        satellites[0],
        satellites[2],
        frame
    )

    if d < 2000:

        events += (
            "WARNING\n"
            "Possible Close Approach\n"
        )

    else:

        events += (
            "All Satellites Safe\n"
        )

    dashboard.set_text(
        info
    )

    event_log.set_text(
        events
    )

    ax.view_init(
        elev=25,
        azim=frame/5
    )

    return markers

# =========================
# Limits
# ========================= 

max_orbit = max(
    np.max(
        np.sqrt(
            sat.x**2+
            sat.y**2+
            sat.z**2
        )
    )
    for sat in satellites
)

ax.set_xlim(
    -max_orbit,
    max_orbit
)

ax.set_ylim(
    -max_orbit,
    max_orbit
)

ax.set_zlim(
    -max_orbit,
    max_orbit
)

ax.set_title(
    "Mission Control Pro"
)

# =========================
# Run Animation
# =========================     

ani = FuncAnimation(
    fig,
    update,
    frames=1000,
    interval=20
)

plt.show()