import streamlit as st
import random

from spelers import get_spelers
from vragen_random import genereer_random_vraag
from specials import vaste_specials, genereer_special

# --- Configuratie ---
st.set_page_config(page_title="🍻 Fuzzy Drankspel", layout="centered")
st.title("🍻 Fuzzy Drankspel")

# --- Init session state ---
if "vraag_index" not in st.session_state:
    st.session_state.vraag_index = 0
if "spelgestart" not in st.session_state:
    st.session_state.spelgestart = False
if "vragenlijst" not in st.session_state:
    st.session_state.vragenlijst = []

# --- Functie om standaardvragen te laden ---
def load_standaard_vragen():
    try:
        with open("vragen_1.txt", "r", encoding="utf-8") as f:
            return [x.strip() for x in f.readlines() if x.strip()]
    except:
        return []

# --- Spelinstellingen ---
if not st.session_state.spelgestart:
    spelers = get_spelers()

    aantal_vragen = st.selectbox("📋 Aantal vragen", [20, 30, 50])
    st.caption("Vragen bestaan uit een mix van eigen, random en speciale opdrachten.")

    if st.button("🎬 Start het spel"):
        if len(spelers) < 2:
            st.warning("Voer minstens twee spelers in om te beginnen!")
        else:
            st.session_state.spelgestart = True
            st.session_state.spelers = spelers

            # Stel vragenlijst samen
            n_specials = max(1, aantal_vragen // 10)
            n_random = aantal_vragen // 2
            n_standaard = aantal_vragen - n_specials - n_random

            vragen = []
            vragen += random.sample(load_standaard_vragen(), min(n_standaard, len(load_standaard_vragen())))
            vragen += [genereer_random_vraag(spelers) for _ in range(n_random)]
            vragen += random.sample(vaste_specials, min(n_specials, len(vaste_specials)))
            vragen += [genereer_special(spelers) for _ in range(n_specials)]

            random.shuffle(vragen)
            st.session_state.vragenlijst = vragen
            st.session_state.vraag_index = 0
            st.rerun()

# --- Speelscherm ---
elif st.session_state.vraag_index < len(st.session_state.vragenlijst):
    vraag = st.session_state.vragenlijst[st.session_state.vraag_index]
    spelers = st.session_state.spelers

    # Slokken en multiplier
    slok = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    mult = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    totaal = slok * mult

    # Visuele kleur op basis van slokken
    if totaal >= 7:
        kleur = "#ffcccc"  # rood
    elif totaal >= 4:
        kleur = "#fff2cc"  # oranje
    else:
        kleur = "#d9ead3"  # groen

    # Speciale opdracht?
    is_special = vraag.startswith("🦠") or vraag.startswith("🎭") or vraag.startswith("🔄") or vraag.startswith("📸") or "QUIZ" in vraag.upper()
    if is_special:
        kleur = "#d0c3fc"  # paars-blauw

    # Toon vraag
    st.markdown(f"### ❓ Vraag {st.session_state.vraag_index + 1} van {len(st.session_state.vragenlijst)}")
    st.markdown(
        f"<div style='background-color: {kleur}; padding: 25px; border-radius: 12px; font-size: 20px;'>"
        f"👉 <strong>{vraag}</strong><br><br>"
        f"💧 <strong>{totaal} slokken!</strong>"
        f"</div>",
        unsafe_allow_html=True
    )

    if is_special:
        st.balloons()

    if st.button("➡️ Volgende vraag"):
        st.session_state.vraag_index += 1
        st.rerun()

# --- Einde ---
else:
    st.success("🎉 Het spel is afgelopen! Bedankt voor het meespelen.")
    st.balloons()
    if st.button("🔁 Opnieuw beginnen"):
        st.session_state.spelgestart = False
        st.session_state.vraag_index = 0
        st.session_state.vragenlijst = []
        st.rerun()






















# w
