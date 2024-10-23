import matplotlib.pyplot as plt

# Data from the table
hole_radii = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
run_1 = [2.68, 2.30, 2.01, 2.05, 2.26, 2.14, 2.21, 2.25, 2.09, 2.25, 2.09]
run_2 = [2.30, 2.55, 2.28, 2.38, 2.02, 2.28, 2.18, 2.15, 2.20, 2.23, 2.16]
run_3 = [2.48, 2.03, 2.38, 2.20, 2.14, 2.01, 2.29, 2.16, 2.12, 2.20, 2.13]
avg = [2.49, 2.29, 2.22, 2.21, 2.14, 2.14, 2.19, 2.19, 2.14, 2.22, 2.13]
variance = [0.03613, 0.06763, 0.03663, 0.02730, 0.01440, 0.01823, 0.00910, 0.00303, 0.00330, 0.00033, 0.00123]

# Create scatter plots for Run 1, Run 2, Run 3, and Avg
plt.figure(figsize=(10, 6))
plt.scatter(hole_radii, variance, label='Varience', color='blue', marker='o')

plt.xlim(0, 50)
plt.ylim(0, 0.07)

# Add labels, title, and legend
plt.xlabel('Hole Radii')
plt.ylabel('Variance')
plt.title('Variance vs. Spill Hole Radii')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
