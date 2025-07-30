import random

# 🔒 Vooraf gedefinieerde specials met duur en optionele speler
def init_specials(speler=None, andere=None):
    return [

        # --- VIRUSSEN ---
        {
            "type": "virus",
            "tekst": "🦠 VIRUS: Het laten van een boer of scheet is verboden 🤐",
            "rondes": 5,
            "speler": None
        },
        {
            "type": "virus",
            "tekst": "🦠 VIRUS: Doe een mondkapje op (of iets dat erop lijkt) 😷",
            "rondes": 3,
            "speler": speler
        },
        {
            "type": "virus",
            "tekst": f"🦠 VIRUS: {speler} en {andere} ruilen hun slokken voor 4 rondes 🔄",
            "rondes": 4,
            "speler": speler
        },

        # --- OPDRACHTEN ---
        {
            "type": "opdracht",
            "tekst": "🎭 OPDRACHT: Lees de volgende 2 rondes de vragen in een raar accent 🗣️",
            "rondes": 2,
            "speler": None
        },

        # --- KIEZERSDILEMMA'S ---
        {
            "type": "stem",
            "tekst": "🎭 KIES: Heb je liever €1.000.000 maar geen voeten of €10.000 en 6 tenen per voet? De minste stemmen nemen de slokken 👣💸",
            "rondes": 1,
            "speler": None
        },
        {
            "type": "stem",
            "tekst": f"🎭 KIES: Is {speler} sterker dan {andere}? Minste stemmen drinken (gelijkspel = iedereen drinkt) 💪",
            "rondes": 1,
            "speler": None
        },

        # --- GROEPSACTIES ---
        {
            "type": "actie",
            "tekst": "👯‍♀️ GROEPSOPDRACHT: Iedereen doet een groepsknuffel of drinkt 🤗",
            "rondes": 1,
            "speler": None
        },
        {
            "type": "actie",
            "tekst": "🎬 OPDRACHT: Speel een scène uit een bekende film 🎥 (anderen raden), anders drinken",
            "rondes": 1,
            "speler": None
        },
        {
            "type": "stilte",
            "tekst": "🙊 STILTE: Wie het eerst praat, drinkt! 30 seconden stilte vanaf nu 🤫",
            "rondes": 1,
            "speler": None
        },

        # --- QUIZ ---
        {
            "type": "quiz",
            "tekst": f"🧠 QUIZ: {speler}beantwoordt een moeilijke vraag correct 🎓 of drinkt",
            "rondes": 1,
            "speler": speler
        }
    ]

# 🌀 Willekeurig gegenereerde specials met variabele inhoud
def genereer_special(spelers):
    speler = random.choice(spelers)
    andere = random.choice([s for s in spelers if s != speler]) if len(spelers) > 1 else speler

    dynamic_specials = [
        {
            "type": "wisselplek",
            "tekst": f"🔄 {speler} en {andere} ruilen van plek voor de rest van het spel (of drinken) 🪑",
            "rondes": 1,
            "speler": None
        },
        {
            "type": "wisselslok",
            "tekst": f"🔁 {speler} en {andere} ruilen elkaars slokken de komende 3 rondes 🍺↔️🍺",
            "rondes": 3,
            "speler": None
        },
        {
            "type": "muziek",
            "tekst": f"🎵 {speler} zingt een refrein van een bekend lied of neemt 3 slokken 🎤",
            "rondes": 1,
            "speler": speler
        },
        {
            "type": "power",
            "tekst": f"😈 {speler} mag een opdracht geven aan iemand anders — weigeren = slokken 👑",
            "rondes": 1,
            "speler": speler
        },
        {
            "type": "quiz",
            "tekst": f"🧠 QUIZ: {speler} beantwoordt een moeilijke vraag correct 🎓 of drinkt",
            "rondes": 1,
            "speler": speler
        },
        {
            "type": "foto",
            "tekst": "📸 Neem een groepsfoto met een gekke pose 🤪! Wie weigert, drinkt 2x",
            "rondes": 1,
            "speler": None
        }
    ]

    alle_specials = init_specials(speler, andere) + dynamic_specials
    return random.choice(alle_specials)













#w
