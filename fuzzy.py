import streamlit as st
import random
from spelers import get_spelers
from vragen_random import genereer_random_vraag


st.set_page_config(page_title="🍻 Drankspel", layout="centered")

# vragen inladen
def load_standaard_vragen():
    try:
        with open("vragen_1.txt", "r", encoding="utf-8") as f:
            return [x.strip() for x in f.readlines() if x.strip()]
    except:
        return []


# Fasebeheer
st.title("🍻 Fuzzy Drankspel")

if "vraag_index" not in st.session_state:
    st.session_state.vraag_index = 0
if "spelgestart" not in st.session_state:
    st.session_state.spelgestart = False


# 🎲 Instelscherm
spelers = get_spelers()  # bijv. via dropdown of tekstinput
aantal_vragen = st.selectbox("Aantal vragen", [20, 30, 50])

if st.button("🎬 Start"):
    st.session_state.spelgestart = True
    st.session_state.vragenlijst = random.sample(
        load_standaard_vragen(), min(aantal_vragen // 2, len(load_standaard_vragen()))
    ) + [genereer_random_vraag(spelers) for _ in range(aantal_vragen // 2)]
    random.shuffle(st.session_state.vragenlijst)


# 🍻 Speelscherm
if st.session_state.spelgestart and st.session_state.vraag_index < len(st.session_state.vragenlijst):
    vraag = st.session_state.vragenlijst[st.session_state.vraag_index]

    slokken = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    multiplier = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    totaal = slokken * multiplier

    st.markdown(f"### ❓ Vraag {st.session_state.vraag_index + 1}")
    st.markdown(f"**{vraag}**")
    st.markdown(f"💧 **{totaal} slokken!**")

    if st.button("➡️ Volgende vraag"):
        st.session_state.vraag_index += 1

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
