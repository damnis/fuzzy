import random

landen = ["Frankrijk", "Japan", "Canada", "Rusland", "Thailand", "België", "Spanje", "Duitsland"]
acties_met_landen = [
    "Wie nog nooit in {} is geweest",
    "Wie ooit in {} is verdwaald",
    "Wie ooit meer dan €100 heeft uitgegeven in {}"
]

def genereer_random_vraag(spelers):
    if not spelers:
        return "Iedereen drinkt een slok"

    speler = random.choice(spelers)
    andere = random.choice([s for s in spelers if s != speler]) if len(spelers) > 1 else speler

    try:
        land_vraag = random.choice(acties_met_landen).format(random.choice(landen))
    except:
        land_vraag = "Iedereen die ooit op vakantie is geweest drinkt"

    opties = [
        f"{speler}, geef de persoon links van je een kus of drink",
        f"{speler}, zingt een liedje of drink",
        f"{speler}, vertel een gênant verhaal of drink",
        f"{speler}, geef de persoon rechts van je een schop(je) of drink",
        f"{speler} en {andere} moeten tegelijk drinken",
        land_vraag,
        f"{speler}, wijs 2 mensen aan die moeten drinken",
        f"Wie het laatst op vakantie is geweest, drinkt",
        f"{speler} moet iedereen een bijnaam geven, of dubbele slokken drink"
    ]
    return random.choice(opties)











# w
