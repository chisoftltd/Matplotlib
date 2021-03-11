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
# plt.plot(ypoints, marker = 'o')
# plt.show()

# plt.plot(xpoints, marker = 'o')
# plt.show()

# plt.plot(ypoints, marker = '*')
# plt.show()

# plt.plot(xpoints, marker = '*')
# plt.show()

# Format Strings fmt
ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'o:r')
# plt.show()


# Line Reference
# plt.plot(ypoints, ':')
# plt.show()

# plt.plot(ypoints, '--')
# plt.show()

# plt.plot(ypoints, '-.')
# plt.show()

# Color Reference
# plt.plot(ypoints, 'or')
# plt.show()

# plt.plot(ypoints, 'og')
# plt.show()

# plt.plot(ypoints, 'oy')
# plt.show()

# Marker Size
plt.plot(ypoints, marker = 'o', ms = 10)
plt.show()

plt.plot(xpoints, marker = 'x', ms = 20)
plt.show()

plt.plot(ypoints, marker = '*', ms = 30)
plt.show()

plt.plot(xpoints, marker = '<', ms = 40)
plt.show()

plt.plot(ypoints, marker = '+', ms = 50)
plt.show()

plt.plot(xpoints, marker = 'D', ms = 60)
plt.show()

plt.plot(ypoints, marker = '|', ms = 70)
plt.show()

plt.plot(xpoints, marker = '4', ms = 80)
plt.show()

# Marker Color
plt.plot(ypoints, marker = 'o', ms = 10, mec = 'r')
plt.show()

plt.plot(xpoints, marker = 'x', ms = 20, mec = 'g')
plt.show()

plt.plot(ypoints, marker = '*', ms = 30, mec = 'y')
plt.show()

plt.plot(xpoints, marker = '<', ms = 40, mec = 'b')
plt.show()

plt.plot(ypoints, marker = '+', ms = 50, mec = 'r')
plt.show()

plt.plot(xpoints, marker = 'D', ms = 60, mec = 'g')
plt.show()

plt.plot(ypoints, marker = '|', ms = 70, mec = 'y')
plt.show()

plt.plot(xpoints, marker = '4', ms = 80, mec = 'b')
plt.show()

# You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers
plt.plot(ypoints, marker = 'o', ms = 10, mfc = 'r')
plt.show()

plt.plot(xpoints, marker = 'x', ms = 20, mfc = 'g')
plt.show()

plt.plot(ypoints, marker = '*', ms = 30, mfc = 'y')
plt.show()

plt.plot(xpoints, marker = '<', ms = 40, mfc = 'b')
plt.show()

plt.plot(ypoints, marker = '+', ms = 50, mfc = 'r')
plt.show()

plt.plot(xpoints, marker = 'D', ms = 60, mfc = 'g')
plt.show()

plt.plot(ypoints, marker = '|', ms = 70, mfc = 'y')
plt.show()

plt.plot(xpoints, marker = '4', ms = 80, mfc = 'b')
plt.show()


# Use both the mec and mfc arguments to color of the entire marker
plt.plot(ypoints, marker = 'o', ms = 10, mec = 'b', mfc = 'r')
plt.show()

plt.plot(xpoints, marker = 'x', ms = 20, mec = 'y', mfc = 'g')
plt.show()

plt.plot(ypoints, marker = '*', ms = 30, mec = 'g', mfc = 'y')
plt.show()

plt.plot(xpoints, marker = '<', ms = 40, mec = 'r', mfc = 'b')
plt.show()

plt.plot(ypoints, marker = '+', ms = 50, mec = 'b', mfc = 'r')
plt.show()

plt.plot(xpoints, marker = 'D', ms = 60, mec = 'y', mfc = 'g')
plt.show()

plt.plot(ypoints, marker = '|', ms = 70, mec = 'g', mfc = 'y')
plt.show()

plt.plot(xpoints, marker = '4', ms = 80, mec = 'r', mfc = 'b')
plt.show()

# Mark each point with a beautiful green color
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()

# Mark each point with the color named "hotpink"
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()