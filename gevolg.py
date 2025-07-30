import random
import streamlit as st
import time

# Voorbeelden van gevolgvragen met opvolgende acties
GEVOLG_VRAGEN = [
    {
        "vraag": "Kies kop of munt, verliezers drinken",
        "type": "actie",
        "gevolg": lambda speler=None, andere=None: st.button("🎲 Doe de worp!") and st.success(f"🎲 Muntstuk valt op: {random.choice(['Kop', 'Munt'])}!")
    },
    {
        "vraag": "Wie heeft het meeste geld op zak (contant)?",
        "type": "actie",
        "gevolg": lambda speler=None, andere=None: st.button("💰 Bekijk resultaat") and st.warning("💸 De rijkste geeft een rondje! Alle anderen drinken.")
    },
    {
        "vraag": "De kleinste speler neemt de slokken",
        "type": "uitgesteld",
        "rondes_later": 2,
        "gevolg_tekst": "ACTIE: Kleintjes worden groot! De kleinste speler mag 1x dubbele slokken uitdelen bij de volgende ronde."
    }
]

# Gevolg direct tonen

def toon_gevolg(vraag_item, speler=None, andere=None):
    if callable(vraag_item.get("gevolg")):
        vraag_item["gevolg"](speler, andere)

# Voeg uitgesteld gevolg toe met rondeteller
def plan_gevolg(vraag_item):
    if vraag_item.get("type") == "uitgesteld":
        gevolg = {
            "rondes": vraag_item.get("rondes_later", 2),
            "tekst": vraag_item.get("gevolg_tekst")
        }
        st.session_state.actieve_gevolgen.append(gevolg)

# Tel actieve gevolgen af en toon indien nodig
def verwerk_gevolgen():
    nieuwe = []
    for g in st.session_state.actieve_gevolgen:
        g["rondes"] -= 1
        if g["rondes"] == 0:
            st.markdown(f"### ⚡ {g['tekst']}")
        else:
            nieuwe.append(g)
    st.session_state.actieve_gevolgen = nieuwe

# Losse functie om random gevolgvraag op te halen
def genereer_gevolg_vraag(spelers):
    vraag_item = random.choice(GEVOLG_VRAGEN)
    speler = random.choice(spelers)
    andere = random.choice([s for s in spelers if s != speler]) if len(spelers) > 1 else "iemand anders"
    if "{speler}" in vraag_item["vraag"]:
        vraag_item = vraag_item.copy()
        vraag_item["vraag"] = vraag_item["vraag"].format(speler=speler, andere=andere)
    vraag_item["tekst"] = vraag_item["vraag"]  # voor uniform gebruik in main
    vraag_item["speler"] = speler
    vraag_item["andere"] = andere
    return vraag_item
