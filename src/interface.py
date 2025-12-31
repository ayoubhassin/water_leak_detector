!pip install ipywidgets


import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output

def interface_graphique(ensemble, scaler, threshold=0.3):
    features_order = [
        'heure', 'pression_bar', 'temperature_c', 'occupants',
        'jour_semaine', 'est_fin_semaine',
        'consommation_rolling_mean', 'delta_consommation',
        'delta_consommation_pct', 'pression_anormale', 'pression_occupants'
    ]

    # Widgets pour la saisie
    heure_slider = widgets.IntSlider(min=0, max=23, value=12, description="Heure")
    pression_slider = widgets.FloatSlider(min=0, max=10, value=5.0, step=0.1, description="Pression")
    temp_slider = widgets.FloatSlider(min=-10, max=60, value=25.0, step=0.5, description="Température")
    occupants_slider = widgets.IntSlider(min=1, max=10, value=3, description="Occupants")
    jour_dropdown = widgets.Dropdown(options=[("Lundi",0),("Mardi",1),("Mercredi",2),("Jeudi",3),
                                              ("Vendredi",4),("Samedi",5),("Dimanche",6)],
                                    value=2, description="Jour")
    conso_slider = widgets.FloatSlider(min=0, max=500, value=100.0, step=1.0, description="Conso 24h")
    delta_slider = widgets.FloatSlider(min=0, max=200, value=20.0, step=1.0, description="Delta conso")
    press_anorm_dropdown = widgets.Dropdown(options=[("Non",0),("Oui",1)], value=0, description="Pression anormale")

    output = widgets.Output()

    # Fonction de prédiction
    def predire_fuite(button):
        fin_sem = 1 if jour_dropdown.value >= 5 else 0
        nouvelles_donnees = {
            'heure': heure_slider.value,
            'pression_bar': pression_slider.value,
            'temperature_c': temp_slider.value,
            'occupants': occupants_slider.value,
            'jour_semaine': jour_dropdown.value,
            'est_fin_semaine': fin_sem,
            'consommation_rolling_mean': conso_slider.value,
            'delta_consommation': delta_slider.value,
            'delta_consommation_pct': delta_slider.value / max(conso_slider.value, 1),
            'pression_anormale': press_anorm_dropdown.value,
            'pression_occupants': pression_slider.value * occupants_slider.value
        }

        df_new = pd.DataFrame([nouvelles_donnees], columns=features_order)
        X_scaled = scaler.transform(df_new)
        proba = ensemble.predict_proba(X_scaled)[0,1]
        prediction = int(proba > threshold)

        with output:
            clear_output()
            print("==============================")
            print("🚨 FUITE DÉTECTÉE" if prediction else "🟢 CONSOMMATION NORMALE")
            print(f"💧 Probabilité de fuite : {proba:.2%}")
            print("==============================")

    # Bouton
    bouton = widgets.Button(description="Prédire la fuite", button_style='success')
    bouton.on_click(predire_fuite)

    # Affichage
    display(widgets.VBox([heure_slider, pression_slider, temp_slider, occupants_slider,
                          jour_dropdown, conso_slider, delta_slider, press_anorm_dropdown,
                          bouton, output]))




interface_graphique(ensemble, scaler, threshold=0.3)