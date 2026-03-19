import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random

# Calculate value of Pi using ratio of a area of a square and a circle
N=100000000
random_x = np.random.uniform(low=0, high=1, size=N)
random_y = np.random.uniform(low=0, high=1, size=N)

is_inside= ((random_x)**2+(random_y)**2<1)
number_inside=np.sum(is_inside)

theta=np.linspace(0,np.pi/2,10000)
circle_x=np.cos(theta)
circle_y=np.sin(theta)

plt.scatter(random_x[:5000],random_y[:5000],s=1)
plt.plot(circle_x,circle_y,color='black')
plt.axis('equal')
plt.grid()
plt.xlabel(number_inside/N*4)
plt.show()
