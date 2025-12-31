proba_all = model.predict_proba(scaler.transform(X))[:,1]
pred_all = (proba_all > 0.3).astype(int)
data['prediction_fuite'] = pred_all
data['probabilite_fuite'] = proba_all

plt.figure(figsize=(12,5))
plt.plot(data['timestamp'], data['consommation_liters'], label="Consommation")
plt.scatter(data['timestamp'][pred_all==1], data['consommation_liters'][pred_all==1],
            color='red', label='Fuite détectée', s=20)
plt.xlabel("Temps")
plt.ylabel("Consommation (L)")
plt.title("Fuites détectées sur le temps")
plt.legend()
plt.show()
