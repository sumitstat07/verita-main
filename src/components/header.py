import streamlit as st
import base64


def header_home():
    # Use a raw string so backslashes aren't treated as escape sequences
    logo_path = r"C:\Users\DELL\OneDrive\Desktop\verita\logo2.jpg"

    # Browsers can't load local file paths directly, so encode the image as base64
    with open(logo_path, "rb") as f:
        logo_base64 = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center;margin-bottom:30px; margin-top:30px;">
            <img src="data:image/png;base64,{logo_base64}" style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF;'> Verita </h1>
        </div>
    """, unsafe_allow_html=True)


