import streamlit as st
import random
from spelers import get_spelers
from vragen_random import genereer_random_vraag


st.set_page_config(page_title="🍻 Drankspel", layout="centered")

st.title("🍻 Het Grote Drankspel")

# Fasebeheer
if 'vraag_index' not in st.session_state:
    st.session_state.vraag_index = 0
if 'vragenlijst' not in st.session_state:
    st.session_state.vragenlijst = []

# 🎲 Instelscherm
if st.session_state.vraag_index == 0:
    st.subheader("👥 Voeg spelers toe")
    input_namen = st.text_input("Voer namen in, gescheiden door komma’s (bijv. Sem, Sven, Ruud)")

    aantal_vragen = st.selectbox("Aantal vragen", [20, 30, 50])

    if st.button("🎬 Start spel"):
        namen = [naam.strip() for naam in input_namen.split(",") if naam.strip()]
        if len(namen) < 2:
            st.warning("Minimaal twee spelers vereist!")
        else:
            st.session_state.spelers = namen
            st.session_state.vragenlijst = list(range(aantal_vragen))  # dummy nummers
            st.session_state.vraag_index = 1

# 🍻 Speelscherm
elif st.session_state.vraag_index <= len(st.session_state.vragenlijst):
    vraag_nummer = st.session_state.vraag_index

    # Random slokken en multiplier
    slokken = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    multiplier = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    totaal = slokken * multiplier

    speler = random.choice(st.session_state.spelers)

    # Simpele vraaggeneratoren
    landen = ["Rusland", Frankrijk", "Thailand", "Italië", "Canada"]
    acties = [
        f"Wie nog nooit in {random.choice(landen)} is geweest",
        f"{speler}, geef een compliment aan iemand of drink",
        f"Alle spelers met een baard drinken",
        f"{speler}, wijs 2 mensen aan die moeten drinken",
        f"{speler}, vertel een gênant verhaal of drink",
        f"Iedereen die vandaag te laat was drinkt",
        f"De jongste in het gezelschap drinkt",
        f"{speler} en {random.choice([n for n in st.session_state.spelers if n != speler])} drinken samen"
    ]
    vraag = random.choice(acties)

    # Speciale styling
    is_speciaal = "gênant" in vraag or "samen" in vraag

    st.markdown(f"### ❓ Vraag {vraag_nummer}:")
    st.markdown(f"<div style='background-color: {'#ffc2c2' if is_speciaal else '#f0f2f6'}; padding: 20px; border-radius: 10px;'>"
                f"<strong>{vraag}</strong><br><br>"
                f"💧 <strong>{totaal} slokken!</strong>"
                f"</div>", unsafe_allow_html=True)

    if st.button("➡️ Volgende vraag"):
        st.session_state.vraag_index += 1

# 🏁 Einde
else:
    st.success("🎉 Het spel is afgelopen! Vergeet niet wat water te drinken 😉")
    if st.button("🔁 Opnieuw starten"):
        st.session_state.vraag_index = 0
        st.session_state.vragenlijst = []
