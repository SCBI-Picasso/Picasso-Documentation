import numpy as np
import matplotlib.pyplot as plt

def x_sin(x):
    return np.sin(x)

x = np.linspace(0,20,1000)
y = x_sin(x)


print("Plotting data")

plt.plot(x,y)
plt.title("Sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("figura.png")

print("The data has ben plotted")