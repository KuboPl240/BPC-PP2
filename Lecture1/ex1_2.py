import numpy as np

N = 20
x = np.random.randint(-50,50,N)
x_sorted_np = np.sort(x)
sorted = False
while not(sorted):
    sorted = True
    for n in range(0,N-1):
        if x[n]>x[n+1]:
            x[n], x[n+1] = x[n+1], x[n]
            sorted = False

print("Sorted by numpy: ",x_sorted_np)
print("Sorted by bubble sort: ",x)