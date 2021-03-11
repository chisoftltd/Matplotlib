# Checking Matplotlib Version
import matplotlib as plt
print(plt.__version__)
print()

# Pyplot
import matplotlib.pyplot as plt
import numpy as np 
xpoints = np.array([6, 66])
ypoints = np.array([6, 260])

plt.plot(xpoints, ypoints)
# plt.show()

# Plotting Without Line
plt.plot(xpoints, ypoints, 'o')
# plt.show()

# Multiple Points
xpoints = np.array([6, 66, 34, 260])
# ypoints = np.array([6, 260, 6, 166])
# plt.plot(xpoints, ypoints)
# plt.show()

# Default X-Points
# plt.plot(ypoints)
# plt.show()

# plt.plot(xpoints)
# plt.show()


# Matplotlib Markers
# Markers
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
# plt.show()

# plt.plot(xpoints, marker = 'o')
# plt.show()

# plt.plot(ypoints, marker = '*')
# plt.show()

# plt.plot(xpoints, marker = '*')
# plt.show()

# Format Strings fmt
plt.plot(ypoints, 'o:r')
plt.show()

# Line Reference
plt.plot(ypoints, 'o-:')
plt.show()

plt.plot(ypoints, 'o--')
plt.show()

plt.plot(ypoints, 'o-.')
plt.show()