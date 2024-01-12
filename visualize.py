import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data: a series of lines in 3D space
lines = [
    (0, 256, 2, 65, 256, 2),
    (0, 256, 2, 0, 256, 3),
    (65, 256, 2, 65, 256, 5),
    (65, 256, 5, 65, 386, 5),
    (65, 386, 2, 65, 386, 5),
    (65, 386, 2, 70, 386, 2),
    (65, 386, 1, 65, 386, 2),
    (70, 386, 0, 70, 386, 2),
    (65, 386, 1, 65, 419, 1),
    (65, 419, 1, 65, 419, 2),
    (65, 419, 0, 65, 419, 1),
    (65, 419, 2, 66, 419, 2),
    (66, 419, 0, 66, 419, 2)
]

# Creating a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adding lines to the plot
for line in lines:
    x = [line[0], line[3]]
    y = [line[1], line[4]]
    z = [line[2], line[5]]
    ax.plot(x, y, z)

# Setting labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.title("3D Visualization of Lines")
plt.show()
