from xgboost import XGBClassifier

model = XGBClassifier(
    objective="binary:logistic",
    eval_metric="logloss",
    n_estimators=150,
    max_depth=4,
    learning_rate=0.1,
    random_state=42
)

model.fit(X_train_scaled, y_train)
print("✅ Modèle XGBoost entraîné")
