import random

# 🔒 Vooraf gedefinieerde specials
vaste_specials = [
    "🦠 VIRUS: Het laten van een boer of scheet is verboden voor 5 rondes of neem de slokken",
    "🦠 VIRUS: Doe een mondkapje (of iets dat er op lijkt) op voor 3 rondes of neem de slokken",
    "🦠 VIRUS: {speler} en {andere} ruilen hun slokken voor 4 rondes",
    "🎭 OPDRACHT: Lees de volgende 2 rondes de vragen in een raar accent voor of neem de slokken",
    "🎭 KIES: Heb je liever € 1.000.000 maar geen voeten of € 10.000 en 6 tenen per voet. De minste stemmen nemen de slokken",
    "🎭 KIES: Is {speler} sterker dan {andere} of niet. De minste stemmen nemen de slokken (eigen stem telt niet, gelijkspel iedereen drinkt)",
    "👯‍♀️ Iedereen doet mee aan een groepsknuffel of drinkt de slokken",
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
        f"🔄 {speler} en {andere} ruilen hun slokken voor de rest van het spel (of drinken)",
        f"🎵 {speler} zingt een refrein van een lied naar keuze of neemt 3 slokken",
        f"😈 {speler} geeft een opdracht aan iemand anders — weigeren = slokken",
        f"🧠 QUIZ: {speler} moet een moeilijke vraag beantwoorden (bedenk er eentje!) of drinkt",
        f"📸 Neem een groepsfoto met gekke pose! Wie weigert, drinkt 2x"
    ]
    return random.choice(specials)







