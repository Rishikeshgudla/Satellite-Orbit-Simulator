import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# Earth radius (km)
R = 6371

# Create sphere coordinates
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = R * np.outer(np.cos(u), np.sin(v))
y = R * np.outer(np.sin(u), np.sin(v))
z = R * np.outer(np.ones(np.size(u)), np.cos(v))

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

# Draw Earth
ax.plot_surface(x, y, z)

# Labels
ax.set_title("3D Earth Model")

ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")

plt.show()