import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

R1 = np.random.randint(20,size=4)
R2 = np.random.randint(20,size=4)
print(R1)
while R1[2]==0 or R1[3]==0:
    R1 = np.random.randint(20,size=4)

while R2[2]==0 or R2[3]==0:
    R2 = np.random.randint(20,size=4)

R1_center = ((R1[0] + R1[2] / 2),(R1[1] + R1[3] / 2))
R2_center = ((R2[0] + R2[2] / 2),(R2[1] + R2[3] / 2))

print("Coordinates of rectangle R1 center point are: ",R1_center)
print("Coordinates of rectangle R2 center point are: ",R2_center)

R1x_min, R1x_max = R1[0], R1[0] + R1[2]
R1y_min, R1y_max = R1[1], R1[1] + R1[3]
    
R2x_min, R2x_max = R2[0], R2[0] + R2[2]
R2y_min, R2y_max = R2[1], R2[1] + R2[3]

if R1x_max < R2x_min or R2x_max < R1x_min or R1y_max < R2y_min or R2y_max < R1y_min:
    intersection = False
else:
    intersection = True

print(f"Rectangles are {'intersecting' if intersection else 'not intersecting'}")
rect1=plt.Rectangle(xy=(R1[0],R1[1]), width=R1[2], height=R1[3], color='r' , label='R1')
rect2=plt.Rectangle(xy=(R2[0],R2[1]), width=R2[2], height=R2[3], color='b' , label='R2')

fig, ax = plt.subplots()
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.autoscale()

fig.subplots_adjust()
plt.show()