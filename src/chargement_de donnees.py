import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le CSV
data = pd.read_csv("eau_domestique.csv")
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Extraire features temporelles
data['heure'] = data['timestamp'].dt.hour
data['jour_semaine'] = data['timestamp'].dt.dayofweek
data['est_fin_semaine'] = (data['jour_semaine'] >= 5).astype(int)

# Features dérivées
data['consommation_rolling_mean'] = data['consommation_liters'].rolling(24).mean().fillna(0)
data['delta_consommation'] = data['consommation_liters'].diff().fillna(0)
data['delta_consommation_pct'] = data['delta_consommation'] / data['consommation_rolling_mean'].replace(0,1)
data['pression_anormale'] = (data['pression_bar'] > data['pression_bar'].quantile(0.95)).astype(int)
data['pression_occupants'] = data['pression_bar'] * data['occupants']

# Visualisation
print(data.head())
plt.figure(figsize=(12,5))
plt.plot(data['timestamp'], data['consommation_liters'], label="Consommation")
plt.plot(data['timestamp'], data['consommation_rolling_mean'], label="Moyenne 24h")
plt.legend()
plt.title("Consommation sur le temps")
plt.show()
