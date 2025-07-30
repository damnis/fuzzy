 # Simpele vraaggeneratoren
    landen = ["Rusland", Frankrijk", "Thailand", "Italië", "Canada"]
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
