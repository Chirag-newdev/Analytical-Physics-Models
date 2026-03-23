import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random

# Calculate value of Pi using ratio of a area of a square and a circle

N=100000000 # Number of Random Numbers
random_x = np.random.uniform(low=0, high=1, size=N)
random_y = np.random.uniform(low=0, high=1, size=N)

is_inside= ((random_x)**2+(random_y)**2<1)
# changed the sum to cumsum to obtain value for each i
number_inside=np.cumsum(is_inside)
indices = np.arange(1, N + 1)
estimate = 4* (number_inside)/(indices)

#Making the circle
theta=np.linspace(0,np.pi/2,10000)
circle_x=np.cos(theta)
circle_y=np.sin(theta)

pi_est = 4 * number_inside[-1] / N

plt.scatter(random_x[:5000], random_y[:5000], s=1)
plt.plot(circle_x, circle_y, color='black')
plt.axis('equal')
plt.grid()
plt.title(f"$\\pi \\approx {pi_est:.6f}$")

factor=1000

plt.figure(figsize=(10, 6))
plt.semilogx(indices[::factor], estimate[::factor], label='Monte Carlo Estimate', color='#1f77b4')
plt.axhline(y=np.pi, color='r', linestyle='--', label='True $\pi$ (3.14159...)')
plt.title(f"Convergence of $\pi$ Estimate over $N={N}$ Samples")
plt.xlabel("Number of Samples ($N$) - Log Scale")
plt.ylabel("Estimated Value")
plt.grid(True, which="both", linestyle='--', alpha=0.5)
plt.ylim(3.10, 3.20) 


plt.show()