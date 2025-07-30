import streamlit as st

def get_spelers():
    st.subheader("👥 Spelers")
    input_namen = st.text_input("Voer namen in, gescheiden door komma’s (bijv. Sem, Sven, Ruud)")
    spelers = [naam.strip() for naam in input_namen.split(",") if naam.strip()]
    return spelers




# vaste spelers
