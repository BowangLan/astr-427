import numpy as np

# Constants
dx = 0.1
dt = 0.005  # chosen to satisfy the stability condition
D = 1  # diffusion coefficient, assumed to be 1 for simplicity

# Number of spatial points and time steps
x_points = int(1 / dx) + 1
t_steps = 100  # number of time steps to simulate

# Initialize u(x, t)
u = np.zeros(x_points)
u_new = np.zeros(x_points)

# Set boundary conditions
u[0] = 100
u[-1] = 100
u_new[0] = 100
u_new[-1] = 100

# Simulation using the explicit method
for n in range(t_steps):
    for i in range(1, x_points - 1):
        u_new[i] = u[i] + dt * (u[i + 1] - 2 * u[i] + u[i - 1]) / dx**2
    u = np.copy(u_new)  # update the temperature profile for the next time step

print(u)