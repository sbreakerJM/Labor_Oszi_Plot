
import pandas as pd
import matplotlib.pyplot as plt

def plot_all_voltage_traces(csv_path):
    # Skip header and load data
    df = pd.read_csv(csv_path, skiprows=2)
    header = pd.read_csv(csv_path, nrows=1).values.flatten().tolist()

    # Assign proper column names
    df.columns = ['time'] + [f"{label.strip()}_{i}" for i, label in enumerate(header[1:], start=1)]

    # Convert strings to float
    df = df.applymap(lambda x: float(str(x).replace('+', '').replace('E', 'e')))

    # Plotting
    plt.figure(figsize=(12, 7))
    for col in df.columns[1:]:
        plt.plot(df['time'], df[col], label=col)
    plt.xlabel('Zeit (s)')
    plt.ylabel('Spannung (V)')
    plt.title('Alle Messspuren über der Zeit')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Beispiel-Aufruf:
plot_all_voltage_traces("Data/ue1/RLC_Kreis.csv")
