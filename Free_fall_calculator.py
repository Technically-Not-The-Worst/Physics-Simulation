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
    
    print(f"The object hits the ground at t = {final_time:.5f} seconds, v = {final_velocity:.5f} m/s, h = {final_height:.5f} m")
    return t_values, v_values, h_values, final_time, final_velocity, final_height

# Parameters
mass = 0.05  # Mass of the object (kg)
Cd = 1.5  # Drag coefficient for a sphere
A = 0.034636059- ((0.00**2)*3.14159263)  # Cross-sectional area (m^2)
h0 = 9  # Initial height (m)
t_max = 3  # Time in seconds
dt = 0.000001  # Time step

# Calculate free fall velocities and heights
t_values, v_values, h_values, final_time, final_velocity, final_height = free_fall_with_air_resistance(mass, Cd, A, h0, t_max, dt)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(t_values, v_values, label='Velocity (m/s)', color='b')
plt.plot(t_values, h_values, label='Height (m)', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.title('Free Fall with Air Resistance')
plt.grid(True)
plt.legend()

# Annotate a single box for both velocity and height
plt.annotate(
    f"t = {final_time:.5f} s\nv = {final_velocity:.5f} m/s\nh = {final_height:.5f} m",
    xy=(final_time, final_velocity),
    xytext=(final_time + 0.09, final_velocity - 2),
    arrowprops=dict(arrowstyle="->", lw=1.5, color='blue'),
    bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white')
)

# Second arrow pointing to the final height value with shifted connection point
plt.annotate(
    "",
    xy=(final_time, final_height),
    xytext=(final_time + 0.2, final_velocity - 2.11),  # Shifted connection point
    arrowprops=dict(arrowstyle="->", lw=1.5, color='red')
)

# Show the plot
plt.show()
