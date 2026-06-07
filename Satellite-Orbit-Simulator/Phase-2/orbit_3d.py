import numpy as np
import matplotlib.pyplot as plt

R = 6371
ALTITUDE = 1000

orbit_radius = R + ALTITUDE

# Earth sphere
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = R * np.outer(np.cos(u), np.sin(v))
y = R * np.outer(np.sin(u), np.sin(v))
z = R * np.outer(np.ones(np.size(u)), np.cos(v))

# Orbit coordinates
theta = np.linspace(0, 2*np.pi, 1000)

orbit_x = orbit_radius * np.cos(theta)
orbit_y = orbit_radius * np.sin(theta)
orbit_z = np.zeros_like(theta)

# Plot
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z)

ax.plot(
    orbit_x,
    orbit_y,
    orbit_z,
    linewidth=2
)

ax.set_title("3D Satellite Orbit")

ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")

plt.show()