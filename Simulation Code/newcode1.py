import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.807  # Acceleration due to gravity (m/s^2)
rho = 1.225  # Air density (kg/m^3)

# Function to calculate air resistance constant k
def calculate_k(Cd, A):
    return 0.5 * rho * Cd * A

# Function to calculate velocity and height over time
def free_fall_with_air_resistance(mass, Cd, A, h0, t_max, dt):
    k = calculate_k(Cd, A)
    t_values = np.arange(0, t_max, dt)
    v_values = np.zeros_like(t_values)
    h_values = np.zeros_like(t_values)
    h_values[0] = h0

    # Variable to track the time when the object hits the ground
    final_time = t_max

    for i in range(1, len(t_values)):
        v_prev = v_values[i - 1]
        h_prev = h_values[i - 1]
        
        # Calculate change in velocity
        dv = (g - (k / mass) * v_prev**2) * dt
        v_values[i] = v_prev + dv
        
        # Calculate new height
        h_new = h_prev - v_values[i] * dt
        h_values[i] = max(h_new, 0)  # Ensure the height doesn't go below 0
        
        # Stop if the object hits the ground
        if h_values[i] <= 0:
            final_time = t_values[i]  # Record the time when object hits the ground
            final_velocity = v_values[i]  # Record the velocity at impact
            final_height = h_values[i]  # This will be zero when the object hits the ground
            v_values = v_values[:i+1]  # Truncate arrays to stop at impact
            h_values = h_values[:i+1]
            t_values = t_values[:i+1]
            break
    
    return t_values, v_values, h_values, final_time, final_velocity, final_height

# Parameters
mass = 0.05  # Mass of the object (kg)
hole_radii = [0, 5, 10, 15, 20, 25, 30, 40, 45, 50]  # Hole radii in mm
drag_coefficients = [1.50, 1.45, 1.40, 1.35, 1.30, 1.25, 1.20, 1.15, 1.10, 1.05]  # Corresponding drag coefficients
h0 = 9  # Initial height (m)
t_max = 3  # Time in seconds
dt = 0.0001  # Time step

# Initialize plotting
plt.figure(figsize=(12, 8))

# Loop through each hole radius and corresponding drag coefficient
for hole_radius, Cd in zip(hole_radii, drag_coefficients):
    # Calculate the area of the circle without the hole
    A = np.pi * (0.105**2) - np.pi * (hole_radius / 1000)**2  # Convert mm to m and calculate area (m^2)

    # Calculate free fall velocities and heights
    t_values, v_values, h_values, final_time, final_velocity, final_height = free_fall_with_air_resistance(mass, Cd, A, h0, t_max, dt)

    # Plotting the results
    plt.plot(t_values, v_values, label=f'Velocity (Hole Radius = {hole_radius} mm, Cd = {Cd})', alpha=0.75)
    plt.plot(t_values, h_values, linestyle='--', label=f'Height (Hole Radius = {hole_radius} mm, Cd = {Cd})', alpha=0.75)

# Finalizing the plot
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.title('Free Fall with Air Resistance for Varying Spill Hole Sizes')
plt.grid(True)
plt.legend(fontsize= 6.5)  # Adjust the font size of the legend
plt.tight_layout()

# Show the plot
plt.show()
