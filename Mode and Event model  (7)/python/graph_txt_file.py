import pandas as pd
import matplotlib.pyplot as plt

def preprocess_and_load_data(filename):
    # Initialize a list to store processed data
    processed_lines = []
    with open(filename, 'r') as file:
        for line in file:
            # Clean the line and split based on hyphen, limit splits
            parts = line.strip().split(' - ')
            parts = [part.strip() for part in parts]  # Strip spaces from each part
            if len(parts) == 6:  # Ensure only lines with the correct number of parts are kept
                processed_lines.append(parts)

    # Create DataFrame from the processed lines
    column_names = ["Current Time", "Angle", "Torque", "Angular Velocity", "State 1", "State 2"]
    df = pd.DataFrame(processed_lines, columns=column_names)

    # Convert numerical columns to float
    for col in ["Current Time", "Angle", "Torque", "Angular Velocity"]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Drop rows with NaN values in numerical columns
    df = df.dropna(subset=["Current Time", "Angle", "Torque", "Angular Velocity"])
    return df

def plot_data(df):
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(df["Current Time"], df["Angle"], label="Angle", marker='o')
    plt.plot(df["Current Time"], df["Torque"], label="Torque", marker='x')
    plt.plot(df["Current Time"], df["Angular Velocity"], label="Angular Velocity", marker='s')

    plt.xlabel("Current Time (s)")
    plt.ylabel("Value")
    plt.title("Angle, Torque, and Angular Velocity Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Replace 'data.txt' with the path to your text file
    filename = r'C:\Users\peder\OneDrive - Aarhus universitet\_Programmering og modellering\Robot-Arm-Project\Mode and Event model  (7)\python\data.txt'
    df = preprocess_and_load_data(filename)
    plot_data(df)
