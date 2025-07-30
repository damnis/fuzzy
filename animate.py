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
        "https://tenor.com/nl/view/spooky's-jumpscare-mansion-ringu-explosion-ringu-specimen-4-gif-1297734078095087124",
        "https://images.app.goo.gl/DHamEivoTZKtsPww9",
        "https://images.app.goo.gl/iXiKysdqtMMc2X8D8"
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
