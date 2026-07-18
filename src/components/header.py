import streamlit as st
import base64
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGO_PATH = os.path.join(BASE_DIR, "verita_logo.png")


def get_logo_base64():
    with open(LOGO_PATH, "rb") as f:
        return base64.b64encode(f.read()).decode()


def header_home():
    logo_base64 = get_logo_base64()

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center;margin-bottom:30px; margin-top:30px;">
            <img src="data:image/png;base64,{logo_base64}" style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF; padding-left:12px; letter-spacing:1px;'> Verita </h1>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_base64 = get_logo_base64()

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px;">
            <img src="data:image/png;base64,{logo_base64}" style='height:85px;' />
            <h1 style='text-align:left; color:#E0E3FF;'> Verita </h1>
        </div>
    """, unsafe_allow_html=True)

