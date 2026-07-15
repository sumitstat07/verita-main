import streamlit as st


def footer_home():
    st.markdown("""
        <div style="display:flex; align-items:center; justify-content:center; margin-top:60px; padding:20px 0; border-top:1px solid rgba(255,255,255,0.1);">
            <p style='text-align:center; color:#8A8FA3; font-size:13px; margin:0;'>Designed & Developed by Sumit Sana</p>
        </div>
    """, unsafe_allow_html=True)