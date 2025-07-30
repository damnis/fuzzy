import streamlit as st
import time

# 🎆 Bliksemflits
def show_bliksem():
    for _ in range(3):
        st.markdown("""
        <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
             background: white; opacity: 0.7; z-index: 9999;'>
        </div>""", unsafe_allow_html=True)
        time.sleep(0.1)
        st.markdown("""
        <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
             background: none; z-index: 9999;'>
        </div>""", unsafe_allow_html=True)
        time.sleep(0.1)

# 👾 Hacker Mode
def hacker_effect():
    st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: black !important;
        color: lime !important;
    }
    </style>
    <div style='color: lime;'>👾 Hacker attack... alles is gehackt!</div>
    """, unsafe_allow_html=True)

# 🔁 Rotatie-effect (alleen waarschuwing)
def rotate_warning():
    st.warning("⚠️ App-rotatie niet ondersteund. Draai je hoofd even om voor de grap!")

# ⏳ Timer
def run_timer(seconds=30):
    timer_placeholder = st.empty()
    for i in range(seconds, 0, -1):
        timer_placeholder.markdown(f"⏳ Tijd over: **{i}** seconden")
        time.sleep(1)
    timer_placeholder.markdown("⏰ Tijd is om!")
