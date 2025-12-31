# Histogramme de la pression
plt.figure(figsize=(10,5))
sns.histplot(data['pression_bar'], bins=30, kde=True)
plt.title("Distribution de la pression")
plt.show()

# Pression anormale
plt.figure(figsize=(6,4))
sns.countplot(x='pression_anormale', data=data)
plt.title("Occurrences de pression anormale")
plt.show()

# Relation pression vs consommation
plt.figure(figsize=(10,5))
sns.scatterplot(x='pression_bar', y='consommation_liters', hue='pression_anormale', data=data)
plt.title("Consommation vs Pression")
plt.show()
