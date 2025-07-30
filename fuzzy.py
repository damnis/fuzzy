import streamlit as st
import random

from spelers import get_spelers
from vragen_random import genereer_random_vraag
from specials import genereer_special
from quiz import get_quizvraag

# --- Pagina-instellingen ---
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

# --- Vaste vragen inlezen ---
def load_standaard_vragen():
    try:
        with open("vragen_1.txt", "r", encoding="utf-8") as f:
            return [x.strip() for x in f.readlines() if x.strip()]
    except:
        return []

# --- Startinstellingen ---
if not st.session_state.spelgestart:
    spelers = get_spelers()
    aantal_vragen = st.selectbox("📋 Aantal vragen", [20, 30, 50])
    st.caption("Mix van vaste vragen, random gegenereerde vragen en specials (virussen, quiz, opdrachten...)")

    if st.button("🎬 Start het spel"):
        if len(spelers) < 2:
            st.warning("Voer minstens twee spelers in om te beginnen.")
        else:
            st.session_state.spelgestart = True
            st.session_state.spelers = spelers

            n_specials = max(1, aantal_vragen // 5)
            n_random = aantal_vragen // 2
            n_standaard = aantal_vragen - n_specials - n_random

            vragen = []
            vragen += random.sample(load_standaard_vragen(), min(n_standaard, len(load_standaard_vragen())))
            vragen += [genereer_random_vraag(spelers) for _ in range(n_random)]
            new_specials = [genereer_special(spelers) for _ in range(n_specials)]
            vragen += new_specials
            st.session_state.actieve_specials = []  # reset
            # Voor specials met duur > 1, voeg ze toe aan actieve lijst (maar zet 'actief' nog op False)
            for s in new_specials:
                if isinstance(s, dict) and s.get("rondes", 0) >= 1:
                    s["actief"] = False
                    st.session_state.actieve_specials.append(s)

   #         vragen += [genereer_special(spelers) for _ in range(n_specials)]

            random.shuffle(vragen)
            st.session_state.vragenlijst = vragen
            st.session_state.vraag_index = 0
            st.session_state.actieve_specials = []
            st.rerun()

# --- Spelronde ---
elif st.session_state.vraag_index < len(st.session_state.vragenlijst):
    vraag = st.session_state.vragenlijst[st.session_state.vraag_index]
    spelers = st.session_state.spelers

    # ❗ Specials bijwerken (aftellen)
    # Aftellen bestaande specials (maar sla eerste ronde over)
    for s in st.session_state.actieve_specials:
        if s.get("actief", False):  # alleen aftellen als al actief
            s["rondes"] -= 1
        else:
            s["actief"] = True  # activeer hem vanaf nu
    
    # Verwijder specials met 0 rondes
    st.session_state.actieve_specials = [s for s in st.session_state.actieve_specials if s["rondes"] > 0]


    # ⚠️ Toon actieve specials
    if st.session_state.actieve_specials:
        st.markdown("### ⚠️ Actieve specials:")
        for s in st.session_state.actieve_specials:
            st.markdown(f"- {s['tekst']} ({s['rondes']} ronde{'s' if s['rondes'] != 1 else ''} over)")

    # 🎲 Slokkenberekening
    slok = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    mult = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
    totaal = slok * mult

    # 🎨 Stijl op basis van zwaarte
    kleur = "#d9ead3"  # lichtgroen
    if totaal >= 7:
        kleur = "#ffcccc"  # rood
    elif totaal >= 4:
        kleur = "#fff2cc"  # geel

    is_special = isinstance(vraag, dict)
    if is_special:
        if vraag.get("type") in ["virus", "quiz", "opdracht", "stem", "actie", "stilte"]:
            kleur = "#d0c3fc"  # paarsblauw

    # 🧠 Is dit een quizspecial?
    is_quiz = is_special and vraag.get("type") == "quiz"

    # ✅ Vraag tonen
    st.markdown(f"### ❓ Vraag {st.session_state.vraag_index + 1} van {len(st.session_state.vragenlijst)}")
    tekst = vraag["tekst"] if is_special else vraag

    st.markdown(
        f"<div style='background-color: {kleur}; padding: 20px; border-radius: 12px;'>"
        f"<strong>{tekst}</strong><br><br>"
        f"💧 <strong>{totaal} slokken!</strong>"
        f"</div>",
        unsafe_allow_html=True
    )

    # ℹ️ Toon extra info over active special
    if is_special and vraag.get("rondes", 0) >= 1 and vraag not in st.session_state.actieve_specials:
        st.session_state.actieve_specials.append(vraag)
        if vraag["rondes"] > 1:
            st.caption(f"🕒 Deze opdracht blijft nog {vraag['rondes']} rondes actief.")

    # 🧠 Toon quizvraag als type 'quiz'
    if is_quiz:
        st.markdown("#### 🎓 Moeilijke vraag:")
        st.info(get_quizvraag())

    if st.button("➡️ Volgende vraag"):
        st.session_state.vraag_index += 1
        st.rerun()

# --- Einde spel ---
else:
    st.success("🎉 Het spel is afgelopen! Vergeet niet wat water te drinken 😉")
    st.balloons()
    if st.button("🔁 Opnieuw beginnen"):
        st.session_state.spelgestart = False
        st.session_state.vraag_index = 0
        st.session_state.vragenlijst = []
        st.session_state.actieve_specials = []
        st.rerun()
