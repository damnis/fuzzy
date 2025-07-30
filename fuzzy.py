import streamlit as st
import random

from spelers import get_spelers
from vragen_random import genereer_random_vraag
from specials import genereer_special
from quiz import get_quizvraag

st.set_page_config(page_title="🍻 Fuzzy Drankspel", layout="centered")
st.title("🍻 Fuzzy Drankspel")

# Init state
if "vraag_index" not in st.session_state:
    st.session_state.vraag_index = 0
if "spelgestart" not in st.session_state:
    st.session_state.spelgestart = False
if "vragenlijst" not in st.session_state:
    st.session_state.vragenlijst = []
if "actieve_specials" not in st.session_state:
    st.session_state.actieve_specials = []

# Functie: vragen inlezen
def load_standaard_vragen():
    try:
        with open("vragen_1.txt", "r", encoding="utf-8") as f:
            return [x.strip() for x in f.readlines() if x.strip()]
    except:
        return []

# Startscherm
if not st.session_state.spelgestart:
    spelers = get_spelers()
    aantal_vragen = st.selectbox("📋 Aantal vragen", [20, 30, 50])
    st.caption("Mix van vaste vragen, random gegenereerde vragen en specials.")

    if st.button("🎬 Start het spel"):
        if len(spelers) < 2:
            st.warning("Voer minstens twee spelers in om te beginnen.")
        else:
            st.session_state.spelgestart = True
            st.session_state.spelers = spelers

            vragen = []
            standaard = load_standaard_vragen()
            while len(vragen) < aantal_vragen:
                keuze = random.choice(["standaard", "random", "special"])
                if keuze == "standaard" and standaard:
                    vragen.append(standaard.pop(random.randrange(len(standaard))))
                elif keuze == "random":
                    vragen.append(genereer_random_vraag(spelers))
                elif keuze == "special":
                    s = genereer_special(spelers)
                    if isinstance(s, dict) and s.get("rondes", 0) >= 1:
                        s["rondes"] += 1  # fix: 1 extra voor correcte aftelling
                        s["actief"] = False
                        st.session_state.actieve_specials.append(s)
                    vragen.append(s)
            
            random.shuffle(vragen)
            st.session_state.vragenlijst = vragen
            st.session_state.vraag_index = 0
            st.rerun()

# Spelronde
elif st.session_state.vraag_index < len(st.session_state.vragenlijst):
    vraag = st.session_state.vragenlijst[st.session_state.vraag_index]
    spelers = st.session_state.spelers

    # Update specials
    for s in st.session_state.actieve_specials:
        if s.get("actief", False):
            s["rondes"] -= 1
        else:
            s["actief"] = True
    st.session_state.actieve_specials = [s for s in st.session_state.actieve_specials if s["rondes"] > 0]

    # Toon actieve specials
    if st.session_state.actieve_specials:
        st.markdown("### ⚠️ Actieve specials:")
        for s in st.session_state.actieve_specials:
            st.markdown(f"- {s['tekst']} ({s['rondes']} ronde{'s' if s['rondes'] != 1 else ''} over)")

    # Slokken
    slok = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    mult = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    totaal = slok * mult

    # Stijl
    kleur = "#d9ead3"
    if totaal >= 7:
        kleur = "#ffcccc"
    elif totaal >= 4:
        kleur = "#fff2cc"

    is_special = isinstance(vraag, dict)
    if is_special and vraag.get("type") in ["virus", "quiz", "opdracht", "stem", "actie", "stilte"]:
        kleur = "#d0c3fc"

    is_quiz = is_special and vraag.get("type") == "quiz"
    tekst = vraag["tekst"] if is_special else vraag

    st.markdown(f"### ❓ Vraag {st.session_state.vraag_index + 1} van {len(st.session_state.vragenlijst)}")
    st.markdown(
        f"<div style='background-color: {kleur}; padding: 20px; border-radius: 12px;'>"
        f"<strong>{tekst}</strong><br><br>"
        f"💧 <strong>{totaal} slokken!</strong>"
        f"</div>", unsafe_allow_html=True
    )

    if is_quiz:
        st.markdown("#### 🎓 Moeilijke vraag:")
        st.info(get_quizvraag())

    if st.button("➡️ Volgende vraag"):
        st.session_state.vraag_index += 1
        st.rerun()

# Einde
else:
    st.success("🎉 Het spel is afgelopen! Vergeet niet wat water te drinken 😉")
    st.balloons()
    if st.button("🔁 Opnieuw beginnen"):
        st.session_state.spelgestart = False
        st.session_state.vraag_index = 0
        st.session_state.vragenlijst = []
        st.session_state.actieve_specials = []
        st.rerun()
