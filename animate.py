import streamlit as st
import random
import time
from spelers import get_spelers

# 🎈 Simpele werkende animaties

def show_balloons():
    st.balloons()

def show_sneeuw():
    st.snow()


def show_big_popup(spelers=None):
    berichten = [
        "Chaos incoming!",
        "Laat je drankje niet vallen!",
        "{speler} morste bijna alles...",
        "{andere} lijkt nu al zat...",
        "Iemand moet de kamer luchten!",
        "Gekke vibes incoming!",
        "{speler} en {andere} moeten elkaar aankijken zonder te lachen",
        "Er hangt onweer in de lucht...",
        "Wie gooide er met chips?!"
    ]
    iconen = ["🎉", "⚡", "😱", "😂", "🔥", "🍻", "🌀"]
    speler = random.choice(spelers) if spelers else "iemand"
    andere = random.choice([s for s in spelers if s != speler]) if spelers and len(spelers) > 1 else "een ander"

    bericht = random.choice(berichten).format(speler=speler, andere=andere)
    icoon = random.choice(iconen)

    st.markdown(f"""
    <div style='
        position: fixed;
        top: 30%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: #fff8e1;
        padding: 20px 40px;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
        z-index: 9999;
        font-size: 28px;
        text-align: center;
        animation: fadeinout 3s forwards;
    '>
        {icoon} {bericht}
    </div>

    <style>
    @keyframes fadeinout {{
        0% {{ opacity: 0; }}
        10% {{ opacity: 1; }}
        90% {{ opacity: 1; }}
        100% {{ opacity: 0; }}
    }}
    </style>
    """, unsafe_allow_html=True)



def show_popup(spelers=None):
    berichten = [
        "Chaos incoming!",
        "Laat je drankje niet vallen!",
        "{speler} morste bijna alles...",
        "{andere} lijkt nu al zat...",
        "Iemand moet de kamer luchten!",
        "Gekke vibes incoming!",
        "{speler} en {andere} moeten elkaar aankijken zonder te lachen",
        "Er hangt onweer in de lucht...",
        "Wie gooide er met chips?!"
    ]
    iconen = ["🎉", "⚡", "😱", "😂", "🔥", "🍻", "🌀"]
    speler = random.choice(spelers) if spelers else "iemand"
    andere = random.choice([s for s in spelers if s != speler]) if spelers and len(spelers) > 1 else "een ander"

    bericht = random.choice(berichten).format(speler=speler, andere=andere)
    icoon = random.choice(iconen)
    st.toast(f"{icoon} {bericht}")



# 😱 Korte scare afbeelding (heel even zichtbaar)
def show_scare():
    scares = [
        "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnAyYWkyMHpmMjBpaWN3YjNybTg2am5rMWIzbThxbnkyajV4dnVhMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/okfvUCpgArv3y/giphy.gif"
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjRzZGZtendleTVyMGtqbDN0Z3htMWJ5MG8xN21meXJsaWFubzd4NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZO7IokFpImRdMDUGq6/giphy.gif",  # bijv. donkere ogen
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3JpbzhyNXZicHhxcm5veTdkN2RoOHN2cGd1dDc4anMxcHliYjB0cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4nlLsagDaNTtRxWGkX/giphy.gif",  # mistig gezicht
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3FvOHJpc3V4OHkzNzhmNWkwZ2hpeHJwZWZoazVydnZxcXpkcTNpdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/28aGE5xerXkbK/giphy.gif"   # schaduw beweegt
    ]
    scare_url = random.choice(scares)
    st.image(scare_url, use_container_width=True)
    time.sleep(3)
    st.empty()

# 🤪 Grappige achtergrond (blijft tijdelijk zichtbaar)
def show_fun():
    st.markdown("""
    <style>
    body::before {
        content: "";
        position: fixed;
        width: 100vw; height: 100vh;
        background: url('https://i0.wp.com/simplyshocked.com/wp-content/uploads/2023/08/Scream.webp') center center / cover no-repeat;
        opacity: 0.15;
        z-index: 0;
        pointer-events: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 🔀 Random animatie kiezen

def play_random_effect():
    opties = [
        show_balloons,
        show_sneeuw,
        lambda: show_big_popup,
        show_popup,
        show_scare,
        show_fun
    ]
    effect = random.choice(opties)
    effect()
