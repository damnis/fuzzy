import streamlit as st
import random

from spelers import get_spelers
from vragen_random import genereer_random_vraag
from specials import genereer_special
from quiz import get_quizvraag

# --- Configuratie ---
st.set_page_config(page_title="🍻 Fuzzy Drankspel", layout="centered")
st.title("🍻 Fuzzy Drankspel")

# --- Session state initiëren ---
if "vraag_index" not in st.session_state:
    st.session_state.vraag_index = 0
if "spelgestart" not in st.session_state:
    st.session_state.spelgestart = False
if "vragenlijst" not in st.session_state:
    st.session_state.vragenlijst = []
if "actieve_specials" not in st.session_state:
    st.session_state.actieve_specials = []

# --- Vragenbestand laden ---
def load_standaard_vragen():
    try:
        with open("vragen_1.txt", "r", encoding="utf-8") as f:
            return [x.strip() for x in f.readlines() if x.strip()]
    except:
        return []

# --- Setup ---
if not st.session_state.spelgestart:
    spelers = get_spelers()
    aantal_vragen = st.selectbox("📋 Aantal vragen", [20, 30, 50])
    st.caption("Mix van vaste vragen, random vragen en specials (zoals virussen, quiz etc).")

    if st.button("🎬 Start het spel"):
        if len(spelers) < 2:
            st.warning("Voer minstens twee spelers in om te beginnen.")
        else:
            st.session_state.spelgestart = True
            st.session_state.spelers = spelers

            n_specials = max(1, aantal_vragen // 10)
            n_random = aantal_vragen // 2
            n_standaard = aantal_vragen - n_specials * 2 - n_random

            vragen = []
            vragen += random.sample(load_standaard_vragen(), min(n_standaard, len(load_standaard_vragen())))
            vragen += [genereer_random_vraag(spelers) for _ in range(n_random)]
            vragen += random.sample(vaste_specials, min(n_specials, len(vaste_specials)))
            vragen += [genereer_special(spelers) for _ in range(n_specials)]

            random.shuffle(vragen)
            st.session_state.vragenlijst = vragen
            st.session_state.vraag_index = 0
            st.session_state.actieve_specials = []
            st.rerun()

# --- Spelronde ---
elif st.session_state.vraag_index < len(st.session_state.vragenlijst):
    vraag = st.session_state.vragenlijst[st.session_state.vraag_index]

    # ❗ Update actieve specials
    for s in st.session_state.actieve_specials:
        s["rondes"] -= 1
    st.session_state.actieve_specials = [s for s in st.session_state.actieve_specials if s["rondes"] > 0]

    # 🎭 Toon actieve specials
    if st.session_state.actieve_specials:
        st.markdown("### ⚠️ Actieve specials:")
        for s in st.session_state.actieve_specials:
            st.markdown(f"- {s['tekst']} ({s['rondes']} rondes over)")

    # 🎲 Slokken berekenen
    slok = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    mult = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    totaal = slok * mult

    # 🎨 Kleur per zwaarte
    kleur = "#d9ead3"  # groen
    if totaal >= 7:
        kleur = "#ffcccc"  # rood
    elif totaal >= 4:
        kleur = "#fff2cc"  # geel
    if isinstance(vraag, dict):
        if vraag.get("type") in ["virus", "quiz", "opdracht", "stem"]:
            kleur = "#d0c3fc"

    # 🧠 QUIZ?
    is_quiz = isinstance(vraag, dict) and vraag.get("type") == "quiz"

    # 🎯 Vraag tonen
    st.markdown(f"### ❓ Vraag {st.session_state.vraag_index + 1} van {len(st.session_state.vragenlijst)}")
    tekst = vraag["tekst"] if isinstance(vraag, dict) else vraag
    st.markdown(
        f"<div style='background-color: {kleur}; padding: 20px; border-radius: 12px;'>"
        f"<strong>{tekst}</strong><br><br>"
        f"💧 <strong>{totaal} slokken!</strong>"
        f"</div>",
        unsafe_allow_html=True
    )

    # ❗ Special toevoegen aan actieve lijst
    if isinstance(vraag, dict) and vraag.get("rondes", 0) > 1:
        st.session_state.actieve_specials.append(vraag)

    # 🧠 Extra quizvraag tonen
    if is_quiz:
        st.markdown("#### 🎓 Moeilijke vraag:")
        st.info(get_quizvraag())

    # ➡️ Volgende
    if st.button("➡️ Volgende vraag"):
        st.session_state.vraag_index += 1
        st.rerun()

# --- Einde ---
else:
    st.success("🎉 Het spel is afgelopen! Vergeet niet wat water te drinken 😉")
    st.balloons()
    if st.button("🔁 Opnieuw beginnen"):
        st.session_state.spelgestart = False
        st.session_state.vraag_index = 0
        st.session_state.vragenlijst = []
        st.session_state.actieve_specials = []
        st.rerun()

















#w
