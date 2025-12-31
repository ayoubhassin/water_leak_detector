# Distribution consommation
plt.figure(figsize=(10,5))
sns.histplot(data['consommation_liters'], bins=50, kde=True)
plt.title("Distribution de la consommation")
plt.show()

# Variation consommation
plt.figure(figsize=(12,5))
plt.plot(data['timestamp'], data['delta_consommation'])
plt.title("Delta consommation sur le temps")
plt.show()
