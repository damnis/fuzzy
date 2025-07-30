import random
import time
import streamlit as st

quizvragen = [
    {
        "vraag": "Wat is de tweede wet van de thermodynamica?",
        "antwoord": "De entropie van een geïsoleerd systeem neemt altijd toe."
    },
    {
        "vraag": "Wat is het verschil tussen DNA en RNA?",
        "antwoord": "DNA bevat de genetische code, RNA helpt bij de eiwitsynthese."
    },
    {
        "vraag": "Noem drie toepassingen van de kwantummechanica.",
        "antwoord": "Transistors, lasers en MRI-scanners."
    },
    {
        "vraag": "Wat doet een mitochondrion in een cel?",
        "antwoord": "Het produceert energie in de vorm van ATP."
    },
    {
        "vraag": "Wat is de formule van de relativiteitstheorie van Einstein?",
        "antwoord": "E = mc²"
    },
    {
        "vraag": "Welke taal heeft de meeste moedertaalsprekers wereldwijd?",
        "antwoord": "Mandarijn Chinees."
    },
    {
        "vraag": "Wat is de hoofdstad van Mongolië?",
        "antwoord": "Ulaanbaatar."
    },
    {
        "vraag": "Hoeveel liter water bevat het menselijk lichaam gemiddeld?",
        "antwoord": "Ongeveer 40 tot 50 liter."
    },
    {
        "vraag": "Wat is het verschil tussen magma en lava?",
        "antwoord": "Magma is ondergronds, lava is magma dat aan het oppervlak is."
    },
    {
        "vraag": "Wat is het Planck-constante?",
        "antwoord": "6.626 × 10⁻³⁴ Js."
    }
]

def get_quizvraag():
    return random.choice(quizvragen)

def toon_quiz_met_antwoord():
    item = get_quizvraag()
    st.markdown("#### 🎓 Moeilijke vraag:")
    st.info(item["vraag"])
    time.sleep(10)
    st.success(f"✅ Antwoord: {item['antwoord']}")
