import numpy as np
import matplotlib.pyplot as plt

# Function to run the simulation with a fine spatial grid
def run_fine_simulation(dt, dx, total_time=0.4):
    x_points = int(1 / dx) + 1
    t_steps = int(total_time / dt)
    
    # Initialize u(x, t)
    u = np.zeros(x_points)
    u_new = np.zeros(x_points)
    
    # Set boundary conditions
    u[0] = 100
    u[-1] = 100
    u_new[0] = 100
    u_new[-1] = 100
    
    # Simulation
    for n in range(t_steps):
        for i in range(1, x_points - 1):
            u_new[i] = u[i] + dt * (u[i + 1] - 2 * u[i] + u[i - 1]) / dx**2
        u = np.copy(u_new)  # update the temperature profile
    
    return u

# Constants for the fine simulation
dx_fine = 0.001
dt_fine = 0.5 * dx_fine**2 / 1  # Assuming D = 1 for the diffusion coefficient

# Run the simulation
u_fine = run_fine_simulation(dt_fine, dx_fine, total_time=0.4)

# Plot the results
x_values_fine = np.linspace(0, 1, int(1 / dx_fine) + 1)
plt.figure(figsize=(12, 6))
plt.plot(x_values_fine, u_fine, label=f'Δx = {dx_fine}, Δt = {dt_fine:.6f}')
plt.title('Temperature Distribution with Fine Spatial Grid at t=0.4')
plt.xlabel('Position x')
plt.ylabel('Temperature')
plt.legend()
plt.show()
