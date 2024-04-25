import matplotlib.pyplot as plt

# Data
data = {
    "Current Time": [0, 1, 5.4, 9.3, 13.2, 17.1, 21, 24.9, 28.8, 32.7, 36.6, 40.5, 44.4, 48.3, 52.2, 56.1, 60, 
                     63.9, 67.8, 71.7, 75.6, 79.5, 83.4, 87.3, 91.2, 95.1, 99, 102.9, 106.8, 110.7, 114.6, 118.5,
                     122.4, 126.3, 130.2, 134.1, 138, 141.9, 145.8, 149.7, 153.6, 158.1, 162, 165.9, 169.8, 173.7,
                     177.6, 181.5, 185.4, 189.3, 193.2, 197.1],
    "Angle": [0, 0, 16.853, 33.15, 44.583, 50.365, 50.665, 46.443, 39.24, 30.914, 23.324, 18.003, 15.882, 17.144,
              21.259, 7.192, 21.95, 36.859, 49.283, 57.43, 60.445, 58.401, 52.182, 43.289, 33.571, 24.899, 18.824,
              16.275, 11.521, 6.873, 4.183, 4.56, 8.216, 14.581, 22.613, 31.146, 39.138, 45.764, 50.432, 52.764,
              52.595, 49.586, 44.98, 38.854, 32.045, 25.565, 20.449, 17.538, 17.28, 19.62, 24.055, 29.792],
    "Torque": [0, 0, 5.6, 0.596, -0.172, -0.597, -0.757, -0.654, -0.332, 0.135, 0.648, 1.108, 1.43, 1.568, 1.514,
               1.303, 3.194, 1.145, 0.373, -0.267, -0.684, -0.833, -0.712, -0.364, 0.132, 0.673, 1.155, 1.491, 
               1.629, 2.212, 2.721, 3.065, 3.198, 3.119, 2.869, 2.508, 2.095, 1.681, 1.31, 1.02, 0.843, 0.801,
               0.947, 1.158, 1.501, 1.905, 2.307, 2.64, 2.85, 2.908, 2.815, 2.598],
    "Angular Velocity": [0, 0, 4.815, 4.179, 2.931, 1.483, 0.077, -1.083, -1.847, -2.135, -1.946, -1.364, -0.544,
                         0.323, 1.055, 1.521, 3.784, 3.823, 3.186, 2.089, 0.773, -0.524, -1.595, -2.28, -2.492,
                         -2.224, -1.558, -0.654, -1.219, -1.192, -0.69, 0.097, 0.937, 1.632, 2.059, 2.188, 2.049,
                         1.699, 1.197, 0.598, -0.043, -0.669, -1.181, -1.571, -1.746, -1.662, -1.305, -0.718, -0.066, 0.6, 1.137, 1.471]
}

# Plotting the data
plt.figure(figsize=(14, 8))

# Angle
plt.subplot(3, 1, 1)
plt.plot(data['Current Time'], data['Angle'], label='Angle', color='blue')
plt.title('Angle vs Time')
plt.ylabel('Angle (degrees)')

# Torque
plt.subplot(3, 1, 2)
plt.plot(data['Current Time'], data['Torque'], label='Torque', color='red')
plt.title('Torque vs Time')
plt.ylabel('Torque (Nm)')

# Angular Velocity
plt.subplot(3, 1, 3)
plt.plot(data['Current Time'], data['Angular Velocity'], label='Angular Velocity', color='green')
plt.title('Angular Velocity vs Time')
plt.ylabel('Angular Velocity (degrees/s)')
plt.xlabel('Current Time (s)')

plt.tight_layout()
plt.show()