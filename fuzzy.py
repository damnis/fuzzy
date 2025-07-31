import streamlit as st
import random
import time

from spelers import get_spelers
from vragen_random import genereer_random_vraag
from specials import genereer_special
from quiz import toon_quiz_met_antwoord
from animate import play_random_effect
from gevolg import genereer_gevolg_vraag, plan_gevolg, verwerk_gevolgen, toon_gevolg

# Pagina setup
st.set_page_config(page_title="🍻 Fuzzy Drankspel", layout="centered")
st.title("🍻 Fuzzy Drankspel")

# Session state initiatie
for key, default in {
    "vraag_index": 0,
    "spelgestart": False,
    "vragenlijst": [],
    "actieve_specials": [],
    "gestarte_special_uids": [],
    "aftel_trigger": False,
    "animatie_mode": False,
    "actieve_gevolgen": [],
    "geplande_gevolgen_uids": set()
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

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

    st.session_state.animatie_mode = st.checkbox("🎆 Zet animatie-modus aan voor extra chaos")

    if st.button("🎮 Start het spel"):
        if len(spelers) < 2:
            st.warning("Voer minstens twee spelers in om te beginnen.")
        else:
            standaard = load_standaard_vragen()
            vragen = []
            st.session_state.spelers = spelers

            while len(vragen) < aantal_vragen:
                keuze = random.choice(["standaard", "random", "special", "gevolg"])
                if keuze == "standaard" and standaard:
                    vraag = random.choice(standaard)
                    standaard.remove(vraag)
                    vragen.append(vraag)
                elif keuze == "random":
                    vragen.append(genereer_random_vraag(spelers))
                elif keuze == "special":
                    vragen.append(genereer_special(spelers))
                elif keuze == "gevolg":
                    vragen.append(genereer_gevolg_vraag(spelers))

            random.shuffle(vragen)
            st.session_state.vragenlijst = vragen
            st.session_state.vraag_index = 0
            st.session_state.actieve_specials = []
            st.session_state.gestarte_special_uids = []
            st.session_state.aftel_trigger = True
            st.session_state.actieve_gevolgen = []
            st.session_state.geplande_gevolgen_uids = set()
            st.session_state.spelgestart = True
            st.rerun()

# Spelbeurt
elif st.session_state.vraag_index < len(st.session_state.vragenlijst):
    vraag = st.session_state.vragenlijst[st.session_state.vraag_index]
    is_special = isinstance(vraag, dict)
    uid = vraag.get("uid") if is_special else None
    is_meermaals = is_special and vraag.get("rondes", 0) > 0

    if isinstance(vraag, str) and ("{speler}" in vraag or "{andere}" in vraag):
        spelers = st.session_state.spelers
        speler = random.choice(spelers)
        andere = random.choice([s for s in spelers if s != speler]) if len(spelers) > 1 else "iemand anders"
        vraag = vraag.format(speler=speler, andere=andere)

    # Specials aftellen, 1x per beurt
    if st.session_state.aftel_trigger:
        nieuwe_specials = []
        for special in st.session_state.actieve_specials:
            if special.get("actief", False):
                special["rondes"] -= 1
            else:
                special["actief"] = True
            if special["rondes"] > 0:
                nieuwe_specials.append(special)
        st.session_state.actieve_specials = nieuwe_specials
        st.session_state.aftel_trigger = False

    # Gevolgen verwerken
    verwerk_gevolgen()

    # Vraaginfo
    tekst = vraag["tekst"] if is_special else vraag

    # Toon directe gevolgvraag
    if is_special and vraag.get("type") == "actie":
        toon_gevolg(vraag, speler=vraag.get("speler"), andere=vraag.get("andere"))

    # Plan uitgestelde gevolgen
    if is_special and vraag.get("type_uitgesteld"):
        plan_gevolg(vraag)

    if is_special and is_meermaals and uid and uid not in st.session_state.gestarte_special_uids:
        nieuwe_special = vraag.copy()
        nieuwe_special["actief"] = False
        st.session_state.actieve_specials.append(nieuwe_special)
        st.session_state.gestarte_special_uids.append(uid)

    # Slokkenlogica
    slok = random.choices([1, 2, 3], weights=[0.4, 0.4, 0.2])[0]
    mult = random.choices([1, 2, 3], weights=[0.5, 0.4, 0.1])[0]
    totaal = slok * mult

    kleur = "#d9ead3"
    if totaal >= 7:
        kleur = "#ffcccc"
    elif totaal >= 4:
        kleur = "#fff2cc"
    if is_special:
        kleur = "#d0c3fc"

    st.markdown(f"### ❓ Vraag {st.session_state.vraag_index + 1} van {len(st.session_state.vragenlijst)}")
    st.markdown(
        f"<div style='background-color: {kleur}; padding: 20px; border-radius: 12px;'>"
        f"<strong>{tekst}</strong><br><br>"
        f"💧 <strong>{totaal} slokken!</strong>"
        f"</div>", unsafe_allow_html=True
    )

    # Actieve specials tonen
    if st.session_state.actieve_specials:
        st.markdown("### ⚠️ Actieve specials:")
        for s in st.session_state.actieve_specials:
            st.markdown(f"- {s['tekst']} ({s['rondes']} ronde{'s' if s['rondes'] != 1 else ''} over)")

    if is_special and vraag.get("type") == "quiz":
        toon_quiz_met_antwoord()

    if st.session_state.animatie_mode and random.randint(1, 3) == 1:
        play_random_effect(st.session_state.spelers)

    if st.button("➡️ Volgende vraag"):
        st.session_state.vraag_index += 1
        st.session_state.aftel_trigger = True
        st.rerun()

# Einde
else:
    st.success("🎉 Het spel is afgelopen! Vergeet niet wat water te drinken 🙂")
    st.balloons()
    if st.button("🔁 Opnieuw beginnen"):
        for key in [
            "vraag_index", "spelgestart", "vragenlijst", "actieve_specials",
            "gestarte_special_uids", "aftel_trigger", "animatie_mode", "actieve_gevolgen", "geplande_gevolgen_uids"
        ]:
            st.session_state[key] = 0 if key == "vraag_index" else False if key == "spelgestart" else [] if isinstance(st.session_state[key], list) else set()
        st.rerun()
