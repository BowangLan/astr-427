import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0, 1, int(1 / 0.1) + 1)

# Correcting the function to ensure capturing at specific times
def run_simulation_corrected(dt, total_time=0.4):
    # Constants and setup
    dx = 0.1
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
    
    # Store results
    results_u_0_4 = []
    results_x_0_12 = np.zeros(x_points)
    results_x_0_4 = np.zeros(x_points)
    
    # Simulation
    for n in range(t_steps):
        for i in range(1, x_points - 1):
            u_new[i] = u[i] + dt * (u[i + 1] - 2 * u[i] + u[i - 1]) / dx**2
        u = np.copy(u_new)  # update the temperature profile
        
        # Collect data for u(0.4, t)
        results_u_0_4.append(u[int(0.4 / dx)])
        
        # Record data for specific times
        if abs(n * dt - 0.12) < dt/2:
            results_x_0_12 = u.copy()
        if abs(n * dt - 0.4) < dt/2:
            results_x_0_4 = u.copy()
    
    return results_u_0_4, results_x_0_12, results_x_0_4

# Run simulations with the corrected function
u_0_4_dt_0_01, x_0_12_dt_0_01, x_0_4_dt_0_01 = run_simulation_corrected(0.01)
u_0_4_dt_0_002, x_0_12_dt_0_002, x_0_4_dt_0_002 = run_simulation_corrected(0.002)

# Re-plot results for u(x, 0.12) and u(x, 0.4)
plt.figure(figsize=(12, 6))
plt.plot(x_values, x_0_12_dt_0_01, label='t=0.12, Δt=0.01')
plt.plot(x_values, x_0_4_dt_0_01, label='t=0.4, Δt=0.01')
plt.plot(x_values, x_0_12_dt_0_002, label='t=0.12, Δt=0.002', linestyle='--')
plt.plot(x_values, x_0_4_dt_0_002, label='t=0.4, Δt=0.002', linestyle='--')
plt.title('Spatial Temperature Distribution at Specific Times')
plt.xlabel('Position x')
plt.ylabel('Temperature')
plt.legend()
plt.show()
