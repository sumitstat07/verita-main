import streamlit as st
from src.database.db import create_student

@st.dialog("Share Class Link")

def share_subject_dialog(subject_name,subject_code):
    app_domain=""
