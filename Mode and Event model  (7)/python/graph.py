import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data.txt', sep=' - ', engine='python')

# Plotting
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
