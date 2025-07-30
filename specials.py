import random

# 🔒 Vooraf gedefinieerde specials
vaste_specials = [
    "🦠 VIRUS: Doe een mondkapje op (echt!) voor 3 rondes of neem de slokken",
    "🎭 OPDRACHT: Spreek de volgende 2 vragen in een raar accent of neem de slokken",
    "👯‍♀️ Iedereen doet een groepsknuffel of drinkt 2 slokken",
    "🎬 Speel een scène uit een bekende film (anderen raden), anders slokken",
    "🙊 Wie het eerst praat, drinkt! 30 seconden stilte vanaf nu",
]

# 🌀 Willekeurig gegenereerde specials
def genereer_special(spelers):
    if not spelers:
        return "🧩 Special: alle spelers doen iets raars of drinken"

    speler = random.choice(spelers)
    andere = random.choice([s for s in spelers if s != speler]) if len(spelers) > 1 else speler

    specials = [
        f"🔄 {speler} en {andere} ruilen van plek voor de rest van het spel (of drinken)",
        f"🎵 {speler} zingt een refrein naar keuze of neemt 3 slokken",
        f"😈 {speler} geeft een opdracht aan iemand anders — weigeren = slokken",
        f"🧠 QUIZ: {speler} moet een moeilijke vraag beantwoorden (bedenk er eentje!) of drinkt",
        f"📸 Neem een groepsfoto met gekke pose! Wie weigert, drinkt 2x"
    ]
    return random.choice(specials)







