import random

quizvragen = [
    "Wat is de tweede wet van de thermodynamica?",
    "Wat is het verschil tussen DNA en RNA?",
    "Noem drie toepassingen van de kwantummechanica.",
    "Wat doet een mitochondrion in een cel?",
    "Wat is de formule van de relativiteitstheorie van Einstein?",
    "Welke taal heeft de meeste moedertaalsprekers wereldwijd?",
    "Wat is de hoofdstad van Mongolië?",
    "Hoeveel liter water bevat het menselijk lichaam gemiddeld?",
    "Wat is het verschil tussen magma en lava?",
    "Wat is het Planck-constante?"
]

def get_quizvraag():
    return random.choice(quizvragen)
