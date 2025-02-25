# Checking Matplotlib Version
import matplotlib as plt
print(plt.__version__)
print()

# Pyplot
import matplotlib.pyplot as plt
import numpy as np 
xpoints = np.array([6, 66])
ypoints = np.array([6, 260])

# plt.plot(xpoints, ypoints)
# # plt.show()

# Plotting Without Line
# plt.plot(xpoints, ypoints, 'o')
# # plt.show()

# Multiple Points
xpoints = np.array([6, 66, 34, 260])
# ypoints = np.array([6, 260, 6, 166])
# # plt.plot(xpoints, ypoints)
# # plt.show()

# Default X-Points
# # plt.plot(ypoints)
# # plt.show()

# # plt.plot(xpoints)
# # plt.show()


# Matplotlib Markers
# Markers
ypoints = np.array([3, 8, 1, 10])
# # plt.plot(ypoints, marker = 'o')
# # plt.show()

# # plt.plot(xpoints, marker = 'o')
# # plt.show()

# # plt.plot(ypoints, marker = '*')
# # plt.show()

# # plt.plot(xpoints, marker = '*')
# # plt.show()

# Format Strings fmt
ypoints = np.array([3, 8, 1, 10])
# # plt.plot(ypoints, 'o:r')
# # plt.show()


# Line Reference
# # plt.plot(ypoints, ':')
# # plt.show()

# # plt.plot(ypoints, '--')
# # plt.show()

# # plt.plot(ypoints, '-.')
# # plt.show()

# Color Reference
# # plt.plot(ypoints, 'or')
# # plt.show()

# # plt.plot(ypoints, 'og')
# # plt.show()

# # plt.plot(ypoints, 'oy')
# # plt.show()

# Marker Size
# plt.plot(ypoints, marker = 'o', ms = 10)
# # plt.show()

# plt.plot(xpoints, marker = 'x', ms = 20)
# plt.show()

# plt.plot(ypoints, marker = '*', ms = 30)
# plt.show()

# plt.plot(xpoints, marker = '<', ms = 40)
# plt.show()

# plt.plot(ypoints, marker = '+', ms = 50)
# plt.show()

# plt.plot(xpoints, marker = 'D', ms = 60)
# plt.show()

# plt.plot(ypoints, marker = '|', ms = 70)
# plt.show()

# plt.plot(xpoints, marker = '4', ms = 80)
# plt.show()

# Marker Color
# plt.plot(ypoints, marker = 'o', ms = 10, mec = 'r')
# plt.show()

# plt.plot(xpoints, marker = 'x', ms = 20, mec = 'g')
# plt.show()

# plt.plot(ypoints, marker = '*', ms = 30, mec = 'y')
# plt.show()

# plt.plot(xpoints, marker = '<', ms = 40, mec = 'b')
# plt.show()

# plt.plot(ypoints, marker = '+', ms = 50, mec = 'r')
# plt.show()

# plt.plot(xpoints, marker = 'D', ms = 60, mec = 'g')
# plt.show()

# plt.plot(ypoints, marker = '|', ms = 70, mec = 'y')
# plt.show()

# plt.plot(xpoints, marker = '4', ms = 80, mec = 'b')
# plt.show()

# You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers
# plt.plot(ypoints, marker = 'o', ms = 10, mfc = 'r')
# plt.show()

# plt.plot(xpoints, marker = 'x', ms = 20, mfc = 'g')
# plt.show()

# plt.plot(ypoints, marker = '*', ms = 30, mfc = 'y')
# plt.show()

# plt.plot(xpoints, marker = '<', ms = 40, mfc = 'b')
# plt.show()

# plt.plot(ypoints, marker = '+', ms = 50, mfc = 'r')
# plt.show()

# plt.plot(xpoints, marker = 'D', ms = 60, mfc = 'g')
# plt.show()

# plt.plot(ypoints, marker = '|', ms = 70, mfc = 'y')
# plt.show()

# plt.plot(xpoints, marker = '4', ms = 80, mfc = 'b')
# plt.show()


# Use both the mec and mfc arguments to color of the entire marker
# plt.plot(ypoints, marker = 'o', ms = 10, mec = 'b', mfc = 'r')
# plt.show()

# plt.plot(xpoints, marker = 'x', ms = 20, mec = 'y', mfc = 'g')
# plt.show()

# plt.plot(ypoints, marker = '*', ms = 30, mec = 'g', mfc = 'y')
# plt.show()

# plt.plot(xpoints, marker = '<', ms = 40, mec = 'r', mfc = 'b')
# plt.show()

# plt.plot(ypoints, marker = '+', ms = 50, mec = 'b', mfc = 'r')
# plt.show()

# plt.plot(xpoints, marker = 'D', ms = 60, mec = 'y', mfc = 'g')
# plt.show()

# plt.plot(ypoints, marker = '|', ms = 70, mec = 'g', mfc = 'y')
# plt.show()

# plt.plot(xpoints, marker = '4', ms = 80, mec = 'r', mfc = 'b')
# plt.show()

# Mark each point with a beautiful green color
# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
# plt.show()

# Mark each point with the color named "hotpink"
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
# plt.show()

# Matplotlib Line
xpoints = np.array([1,30,15,70])
ypoints = np.array([5,35,20,75])
zpoints = np.array([15,45,5,50])
ipoints = np.array([100,15,10,90])
# plt.plot(xpoints, linestyle = 'dotted')
# plt.show()

# plt.plot(ypoints, linestyle = 'dashed')
# plt.show()

# Line Color
# plt.plot(zpoints, color = 'r')
# plt.show()

# Line Width
# # plt.plot(ipoints, linewidth = '20.5')
# plt.show()

# Multiple Lines
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)

# plt.show()

# Matplotlib Scatter
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))

# plt.scatter(x, y, c=colors, cmap='Accent_r')

# plt.colorbar()

# plt.show()

# Size
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# plt.scatter(x, y, s=sizes)

# plt.show()

# Alpha
# plt.scatter(x, y, s=sizes, alpha=0.5)

# plt.show()

# Combine Color Size and Alpha
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

# plt.colorbar()

# # plt.show()

# Matplotlib Bars
# Creating Bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# plt.bar(x,y)
# plt.show()

x = ["APPLES", "BANANAS"]
y = [400, 350]

# plt.bar(x, y)
# plt.show()

# Horizontal Bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# plt.barh(x, y)
# plt.show()

# Bar Color
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# plt.bar(x, y, color = "red")
# plt.show()

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# plt.bar(x, y, color = "hotpink")
# plt.show()

# Matplotlib Bars
x = np.random.normal(170, 10, 250)

print(x)
plt.hist(x)
plt.show()

# Matplotlib Pie Charts
y = np.array([55, 15, 25, 10])
plt.pie(y)
plt.show()

# Labels
y = np.array([55, 15, 25, 10])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels= mylabels)
plt.show()

# Start Angle
y = np.array([55, 15, 25, 10])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels= mylabels, startangle = 90)
plt.show()

# Explode
y = np.array([55, 15, 25, 10])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0.1]
plt.pie(y, labels= mylabels, startangle = 90, explode = myexplode)
plt.show()

# Shadow
plt.pie(y, labels= mylabels, startangle = 90, explode = myexplode, shadow = True)
plt.show()

# Colors
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

# Legend
plt.pie(y, labels = mylabels)
plt.legend()
plt.show()

# Legend With Header
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits")
plt.show()