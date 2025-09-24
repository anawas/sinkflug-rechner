import streamlit as st

# Title of the app
st.title("✈️ Sinkflug-Rechner")

# Input fields
altitude = st.number_input("Flughöhe (in Fuss)", min_value=0, value=8000)
descent_rate = st.number_input("Sinkrate (in Fuss/Minute)", min_value=1, value=500)
ground_speed = st.number_input("Geschwindigkeit (in Knoten)", min_value=1, value=80)

# Perform calculation if inputs are valid
if altitude > 0 and descent_rate > 0 and ground_speed > 0:
    descent_time_min = altitude / descent_rate
    speed_nm_per_min = ground_speed / 60
    distance_nm = descent_time_min * speed_nm_per_min

    # Display results
    st.subheader("📍 Ergebnisse")
    st.write(f"**Sinkflugdauer:** {descent_time_min:.2f} Minuten")
    st.write(f"**Entfernung zum Flughafen:** {distance_nm:.2f} nautische Meilen")
else:
    st.warning("Bitte gib gültige Werte für Flughöhe, Sinkrate und Geschwindigkeit ein.")
