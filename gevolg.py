import random
import streamlit as st
import time
import streamlit.components.v1 as components

# 🎵 Speel een geluidsfragment via HTML (alleen client-side ondersteund)
def speel_geluid(sound):
    if sound == "laugh":
        components.html(
            """
            <audio autoplay>
                <source src="https://www.fesliyanstudios.com/play-mp3/387" type="audio/mpeg">
            </audio>
            """,
            height=0,
        )

# Voorbeelden van gevolgvragen met opvolgende acties
GEVOLG_VRAGEN = [
    {
        "vraag": "Kies kop of munt, verliezers drinken",
        "type": "actie",
        "gevolg": lambda speler=None, andere=None: (
            speel_geluid("laugh") if st.button("🎲 Doe de worp!") else None
        ) or (
            st.success(f"🎲 Muntstuk valt op: {random.choice(['Kop', 'Munt'])}!") if st.session_state.get("__worp_knop_ingedrukt__") else st.session_state.update({"__worp_knop_ingedrukt__": True})
        )
    },
    {
        "vraag": "Wie heeft het meeste geld op zak (contant)?",
        "type": "actie",
        "gevolg": lambda speler=None, andere=None: (
            speel_geluid("laugh") if st.button("💰 Bekijk resultaat") else None
        ) or (
            st.warning("💸 De rijkste geeft een rondje! Alle anderen drinken.") if st.session_state.get("__geld_knop_ingedrukt__") else st.session_state.update({"__geld_knop_ingedrukt__": True})
        )
    },
    {
        "vraag": "Wie is de kleinste speler?",
        "type": "uitgesteld",
        "actie_knop": "👶 De kleinste speler moet drinken!",
        "rondes_later": lambda: random.randint(2, 5),
        "gevolg_tekst": "ACTIE: Kleintjes worden groot!  De kleinste speler mag 1x dubbele slokken uitdelen bij de volgende ronde."
    }
]

# Gevolg direct tonen

def toon_gevolg(vraag_item, speler=None, andere=None):
    if callable(vraag_item.get("gevolg")):
        vraag_item["gevolg"](speler, andere)

# Voeg uitgesteld gevolg toe met rondeteller

def plan_gevolg(vraag_item):
    if vraag_item.get("type") == "uitgesteld":
        if callable(vraag_item.get("rondes_later")):
            rondes = vraag_item["rondes_later"]()
        else:
            rondes = vraag_item.get("rondes_later", 2)

        gevolg = {
            "rondes": rondes,
            "tekst": vraag_item.get("gevolg_tekst"),
            "uid": f"gevolg_{random.randint(1000, 9999)}"
        }

        if "actieve_gevolgen" not in st.session_state:
            st.session_state.actieve_gevolgen = []
        if "geplande_gevolgen_uids" not in st.session_state:
            st.session_state.geplande_gevolgen_uids = set()

        if gevolg["uid"] not in st.session_state.geplande_gevolgen_uids:
            st.session_state.actieve_gevolgen.append(gevolg)
            st.session_state.geplande_gevolgen_uids.add(gevolg["uid"])
            speel_geluid("laugh")

# Tel actieve gevolgen af en toon indien nodig

def verwerk_gevolgen():
    nieuwe = []
    for g in st.session_state.get("actieve_gevolgen", []):
        g["rondes"] -= 1
        if g["rondes"] == 0:
            st.markdown(f"### ⚡ {g['tekst']}")
            speel_geluid("laugh")
        else:
            nieuwe.append(g)
    st.session_state.actieve_gevolgen = nieuwe

# Losse functie om random gevolgvraag op te halen

def genereer_gevolg_vraag(spelers):
    vraag_item = random.choice(GEVOLG_VRAGEN)
    speler = random.choice(spelers)
    andere = random.choice([s for s in spelers if s != speler]) if len(spelers) > 1 else "iemand anders"

    vraag_item = vraag_item.copy()
    if "{speler}" in vraag_item["vraag"]:
        vraag_item["vraag"] = vraag_item["vraag"].format(speler=speler, andere=andere)
    vraag_item["tekst"] = vraag_item["vraag"]
    vraag_item["speler"] = speler
    vraag_item["andere"] = andere

    if vraag_item.get("type") == "uitgesteld" and "actie_knop" in vraag_item:
    vraag_item["toon_actie_knop"] = True

  
#    vraag_item["toon_actie_knop"] = True if vraag_item.get("type") == "uitgesteld" and "actie_knop" in vraag_item else False


    return vraag_item
