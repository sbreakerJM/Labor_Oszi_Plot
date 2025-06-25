
import pandas as pd
import matplotlib.pyplot as plt

def plot_voltage_data(csv_path):
    # Skip header and convert to float
    df = pd.read_csv(csv_path, skiprows=2)
    df.columns = ['time', 'voltage_1', 'voltage_2']
    df = df.applymap(lambda x: float(str(x).replace('+', '').replace('E', 'e')))

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['time'], df['voltage_1'], label='Spannung 1')
    plt.plot(df['time'], df['voltage_2'], label='Spannung 2')
    plt.xlabel('Zeit (s)')
    plt.ylabel('Spannung (V)')
    plt.title('Spannungsverlauf über der Zeit')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Beispiel-Aufruf:
plot_voltage_data("Data\Tau_RLC_Oszi.csv")
