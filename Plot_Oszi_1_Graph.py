import matplotlib.pyplot as plt

def load_and_plot_csv_custom(file_path):
    x_vals = []
    y_vals = []

    with open(file_path, 'r') as file:
        lines = file.readlines()[2:]  # Überspringe die ersten 2 Zeilen (Kopfzeilen)

        for line in lines:
            if ',' in line:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        x = float(parts[0].replace('E', 'e'))
                        y = float(parts[1].replace('E', 'e'))
                        x_vals.append(x)
                        y_vals.append(y)
                    except ValueError:
                        continue  # Ignoriere fehlerhafte Zeilen

    # Plot erstellen
    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label="Messkurve")
    plt.xlabel("Zeit (s)")
    plt.ylabel("Spannung (V)")
    plt.title("Messdaten aus CSV-Datei")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Beispielaufruf:
load_and_plot_csv_custom("Data/FGEN_1_Square.csv")
