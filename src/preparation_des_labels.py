# Si le CSV a une colonne de fuite réelle
if 'fuite_detectee' in data.columns:
    y = data['fuite_detectee']
else:
    y = (
        (data['delta_consommation'] > 35) |
        (data['pression_anormale'] == 1) |
        (data['consommation_rolling_mean'] > 150)
    ).astype(int)

plt.figure(figsize=(6,4))
sns.countplot(x=y)
plt.title("Distribution des fuites détectées")
plt.show()
