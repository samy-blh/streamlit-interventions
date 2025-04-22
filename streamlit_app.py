import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Outil Interventions ", page_icon="📊")

st.title("📡 Outil de gestion des interventions ")
st.markdown("Choisis une action à exécuter ci-dessous. Le script correspondant sera lancé automatiquement.")

option = st.selectbox(
    "📂 Sélectionne le type d'intervention à analyser :",
    (
        "✅ Interventions à suivre aujourd’hui",
        "📁 Planning",
        "📆 Interventions terminées"
    )
)

if st.button("🚀 Lancer le traitement"):
    st.write("Lancement en cours...")

    if option == "✅ Interventions à suivre aujourd’hui":
        subprocess.run(["python", "check_interventions_fusion.py"])
        st.success("Script 'interventions à suivre' exécuté avec succès.")

    elif option == "📁 Planning":
        subprocess.run(["python", "check_interventions_planification_demain.py"])
        st.success("Script 'planning' exécuté avec succès.")

    elif option == "📆 Interventions terminées":
        subprocess.run(["python", "check_interventions_terminees_date.py"])
        st.success("Script 'interventions terminées à une date précise' exécuté avec succès.")
