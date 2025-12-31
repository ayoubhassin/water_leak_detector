from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

features_order = [
    'heure', 'pression_bar', 'temperature_c', 'occupants',
    'jour_semaine', 'est_fin_semaine',
    'consommation_rolling_mean', 'delta_consommation',
    'delta_consommation_pct', 'pression_anormale', 'pression_occupants'
]

X = data[features_order]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("✅ Train/test split et normalisation effectués")
