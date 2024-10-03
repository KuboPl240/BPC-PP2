import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

C1 = np.random.randint(20,size=3)
C2 = np.random.randint(20,size=3)

while C1[2]==0:
    C1 = np.random.randint(20,size=3)

while C2[2]==0:
    C2 = np.random.randint(20,size=3)


print("Coordinates of circle C1 center point are: ",(C1[0].item(),C1[1].item()))
print("Coordinates of circle C2 center point are: ",(C2[0].item(),C2[1].item()))

distance = math.sqrt((C2[0] - C1[0])**2 + (C2[1] - C1[1])**2)

if distance<C1[2] or distance<C2[2]:
    intersection = True
else:
    intersection = False


print(f"Circles are {'intersecting.' if intersection else 'not intersecting.'}")
circle1=plt.Circle(xy=(C1[0],C1[1]), radius=C1[2], color='r')
circle2=plt.Circle(xy=(C2[0],C2[1]), radius=C2[2], color='b')

fig, ax = plt.subplots()
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.autoscale()

plt.show()