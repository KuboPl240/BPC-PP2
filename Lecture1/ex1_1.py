import random
import numpy as np
N = 10
x = np.random.randint(0,100,N)
y = np.random.randint(0,100,N)

NPsub = np.subtract(x,y)
NPmul = np.multiply(x,y)

sub = list()
mul = list()

for i in range(0,N):
    sub.append(x[i].item()-y[i].item())
    mul.append(x[i].item()*y[i].item())

print(sub, mul)
print(NPsub ,NPmul)

import matplotlib.pyplot as plt
N = 20
phi = np.linspace(-np.pi,np.pi,N)
sin_x = np.sin(phi)
cos_x = np.cos(phi)
tan_x = np.tan(phi)
plt.plot(sin_x)
plt.plot(cos_x)
plt.plot(tan_x)

rand_x = random.randint(-10,10)
if rand_x % 2 == 0:
   print("Number: ", rand_x, "is even")
else: 
    print("Number: ", rand_x, "is odd")

plt.show()