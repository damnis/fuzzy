import random

landen = ["Frankrijk", "Japan", "Canada", "Rusland", "Thailand", "België", "Spanje"]
acties = [
    "Wie nog nooit in {} is geweest",
    "Wie ooit in {} is verdwaald",
    "Wie ooit meer dan €100 heeft uitgegeven in {}"
]

def genereer_random_vraag(spelers):
    if not spelers:
        return "Iedereen drinkt een slok"

    speler = random.choice(spelers)
    acties = random.choice([
        f"{speler}, vertel een gênant verhaal of drink",
        f"{speler} en {random.choice([s for s in spelers if s != speler])} moeten tegelijk drinken",
        random.choice(acties).format(random.choice(landen)),
    ])
    return actie





# Simpele vraaggeneratoren
    landen = ["Rusland", "Frankrijk", "Thailand", "Italië", "Canada", "België", "Spanje"]
    acties = [
        f"Wie nog nooit in {random.choice(landen)} is geweest",
        f"{speler}, geef een compliment aan iemand of drink",
        f"Alle spelers met een baard drinken",
        f"{speler}, wijs 2 mensen aan die moeten drinken",
        f"{speler}, vertel een gênant verhaal of drink",
        f"Iedereen die vandaag te laat was drinkt",
        f"De jongste in het gezelschap drinkt",
        f"{speler} en {random.choice([n for n in st.session_state.spelers if n != speler])} drinken samen"
    ]
    vraag = random.choice(acties)
