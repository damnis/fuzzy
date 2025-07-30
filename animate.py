import streamlit as st
import random
import time

# 🎈 Simpele werkende animaties

def show_balloons():
    st.balloons()

def show_sneeuw():
    st.snow()

def show_popup(message="Chaos incoming!", icon="🎉"):
    st.toast(f"{icon} {message}")

# 😱 Korte scare afbeelding (heel even zichtbaar)
def show_scare():
    scares = [
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
        background: url('https://images.app.goo.gl/gH84SVpCwgpqiTT46') center center / cover no-repeat;
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
        show_popup,
        show_scare,
        show_fun
    ]
    effect = random.choice(opties)
    effect()
