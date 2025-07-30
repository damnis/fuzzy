import streamlit as st
import random

from spelers import get_spelers
from vragen_random import genereer_random_vraag
from specials import genereer_special
from quiz import get_quizvraag

# Pagina setup
st.set_page_config(page_title="🍻 Fuzzy Drankspel", layout="centered")
st.title("🍻 Fuzzy Drankspel")

# Session state initiëren
for key in ["vraag_index", "spelgestart", "vragenlijst", "actieve_specials"]:
    if key not in st.session_state:
        st.session_state[key] = 0 if key == "vraag_index" else False if key == "spelgestart" else []

# Vaste vragen laden
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
            standaard = load_standaard_vragen()
            vragen = []

            while len(vragen) < aantal_vragen:
                keuze = random.choice(["standaard", "random", "special"])
                if keuze == "standaard" and standaard:
                    vragen.append(random.choice(standaard))
                    standaard.remove(vragen[-1])
                elif keuze == "random":
                    vragen.append(genereer_random_vraag(spelers))
                elif keuze == "special":
                    vragen.append(genereer_special(spelers))

            random.shuffle(vragen)
            st.session_state.vragenlijst = vragen
            st.session_state.vraag_index = 0
            st.session_state.actieve_specials = []
            st.session_state.spelgestart = True
            st.rerun()

# Spelbeurt
elif st.session_state.vraag_index < len(st.session_state.vragenlijst):
    vraag = st.session_state.vragenlijst[st.session_state.vraag_index]

    # Specials aftellen (pas na eerste activatie)
    for s in st.session_state.actieve_specials:
        if s.get("actief", False):
            s["rondes"] -= 1
        else:
            s["actief"] = True
    st.session_state.actieve_specials = [s for s in st.session_state.actieve_specials if s["rondes"] > 0]

    # Actieve specials tonen
    if st.session_state.actieve_specials:
        st.markdown("### ⚠️ Actieve specials:")
        for s in st.session_state.actieve_specials:
            st.markdown(f"- {s['tekst']} ({s['rondes']} ronde{'s' if s['rondes'] != 1 else ''} over)")

    # Vraaggegevens ophalen
    is_special = isinstance(vraag, dict)
    tekst = vraag["tekst"] if is_special else vraag
    is_quiz = is_special and vraag.get("type") == "quiz"
    is_meermaals = is_special and vraag.get("rondes", 0) > 0

    # Nieuwe special activeren, maar pas NA het tonen
    if is_meermaals:
        def voeg_special_toe_later():
            bestaande_uids = [s["uid"] for s in st.session_state.actieve_specials if "uid" in s]
            if vraag.get("uid") not in bestaande_uids:
                special = vraag.copy()
                special["actief"] = False
                special["rondes"] += 1  # correctie: eerste beurt telt nog niet af
                st.session_state.actieve_specials.append(special)
        st.session_state["voeg_special_toe"] = voeg_special_toe_later
    

    # Slokken
    slok = random.choices([1, 2, 3], weights=[0.4, 0.4, 0.2])[0]
    mult = random.choices([1, 2, 3], weights=[0.5, 0.4, 0.1])[0]
    totaal = slok * mult

    # Kleuren
    kleur = "#d9ead3"  # groen
    if totaal >= 7:
        kleur = "#ffcccc"  # rood
    elif totaal >= 4:
        kleur = "#fff2cc"  # geel
    if is_special:
        kleur = "#d0c3fc"  # paarsblauw

    # Vraag tonen
    st.markdown(f"### ❓ Vraag {st.session_state.vraag_index + 1} van {len(st.session_state.vragenlijst)}")
    st.markdown(
        f"<div style='background-color: {kleur}; padding: 20px; border-radius: 12px;'>"
        f"<strong>{tekst}</strong><br><br>"
        f"💧 <strong>{totaal} slokken!</strong>"
        f"</div>", unsafe_allow_html=True
    )

    # Quizvraag tonen
    if is_quiz:
        st.markdown("#### 🎓 Moeilijke vraag:")
        st.info(get_quizvraag())

    # Volgende
#    if st.button("➡️ Volgende vraag"):
 #       st.session_state.vraag_index += 1
  #      st.rerun()

    if st.button("➡️ Volgende vraag"):
        if "voeg_special_toe" in st.session_state:
            st.session_state["voeg_special_toe"]()
            del st.session_state["voeg_special_toe"]
        st.session_state.vraag_index += 1
        st.rerun()


# Einde
else:
    st.success("🎉 Het spel is afgelopen! Vergeet niet wat water te drinken 😉")
    st.balloons()
    if st.button("🔁 Opnieuw beginnen"):
        for key in ["vraag_index", "spelgestart", "vragenlijst", "actieve_specials"]:
            st.session_state[key] = 0 if key == "vraag_index" else False if key == "spelgestart" else []
        st.rerun()
