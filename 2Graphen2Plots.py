import pandas as pd
import matplotlib.pyplot as plt

# CSV-Datei einlesen
df = pd.read_csv("Data\RC_Grenzfrequenz.csv")

# Entferne die zweite Zeile mit Einheiten und benenne die Spalten
df_clean = df.iloc[1:].copy()
df_clean.columns = ['time', 'V1', 'V2', 'F1']

# Wandle Strings in Gleitkommazahlen um
df_clean = df_clean.apply(pd.to_numeric)

# Erstelle das Plot-Fenster mit zwei übereinanderliegenden Plots
fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Erster Plot: Spannung V1
axs[0].plot(df_clean['time'], df_clean['V1'], label='Spannung 1 (V1)', color='blue')
axs[0].set_ylabel('Spannung (V)')
axs[0].set_title('Spannung 1 (V1)')
axs[0].legend()
axs[0].grid(True)

# Zweiter Plot: Spannung V2
axs[1].plot(df_clean['time'], df_clean['V2'], label='Spannung 2 (V2)', color='red')
axs[1].set_xlabel('Zeit (s)')
axs[1].set_ylabel('Spannung (V)')
axs[1].set_title('Spannung 2 (V2)')
axs[1].legend()
axs[1].grid(True)

# Layout anpassen und anzeigen
plt.tight_layout()
plt.show()
