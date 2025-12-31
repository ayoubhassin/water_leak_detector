plt.figure(figsize=(10,8))
sns.heatmap(data[[
    'consommation_liters', 'consommation_rolling_mean', 'delta_consommation',
    'delta_consommation_pct', 'pression_bar', 'pression_occupants', 'temperature_c', 'occupants'
]].corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Matrice de corrélation")
plt.show()
