import streamlit as st
import random
import time

def show_bliksem():
    st.markdown("""
    <script>
    const flash = document.createElement("div");
    flash.style.position = "fixed";
    flash.style.top = 0;
    flash.style.left = 0;
    flash.style.width = "100vw";
    flash.style.height = "100vh";
    flash.style.backgroundColor = "white";
    flash.style.zIndex = 9999;
    flash.style.opacity = 0.8;
    document.body.appendChild(flash);
    setTimeout(() => { document.body.removeChild(flash); }, 200);
    </script>
    """, unsafe_allow_html=True)

def show_vlammen():
    st.markdown("""
    <style>
    body {
        background: linear-gradient(to top, #ff6600 0%, #ffcc00 100%) !important;
    }
    </style>
    """, unsafe_allow_html=True)

def show_rook():
    st.markdown("""
    <style>
    body::before {
        content: "";
        position: fixed;
        width: 100vw; height: 100vh;
        background: url('https://i.imgur.com/8z9P6U3.gif') center center / cover no-repeat;
        opacity: 0.3;
        z-index: 1000;
        pointer-events: none;
    }
    </style>
    """, unsafe_allow_html=True)

def show_glitch():
    st.markdown("""
    <style>
    html {
        animation: glitchy 0.5s steps(2, end) infinite;
    }
    @keyframes glitchy {
        0% { transform: translate(0px, 0px); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(2px, -2px); }
        60% { transform: translate(-1px, 1px); }
        80% { transform: translate(1px, -1px); }
        100% { transform: translate(0px, 0px); }
    }
    </style>
    """, unsafe_allow_html=True)

def hacker_effect():
    st.markdown("""
    <style>
    body {
        background-color: #000000 !important;
        color: #00ff00 !important;
        font-family: monospace !important;
    }
    </style>
    """, unsafe_allow_html=True)

def rotate_warning():
    st.markdown("""
    <style>
    html {
        transform: rotate(180deg);
        transition: transform 0.5s ease-in-out;
    }
    </style>
    """, unsafe_allow_html=True)
    time.sleep(2)
    st.markdown("""
    <style>
    html {
        transform: rotate(0deg);
    }
    </style>
    """, unsafe_allow_html=True)
