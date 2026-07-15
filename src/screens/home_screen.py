import streamlit as st

from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout,style_background_home

def home_screen():
    

    header_home()
    style_base_layout()
    style_background_home()


    col1,col2=st.columns(2,gap="large")

    with col1:
        st.header("I'm Teacher")
        st.image("https://thumbs.dreamstime.com/b/teacher-school-student-communication-education-learning-concept-man-teaching-explaining-to-schoolkid-boy-sitting-desk-432993354.jpg")
        if st.button("Teacher Portal",type="primary",icon=':material/arrow_outward:',icon_position="right"):
            st.session_state["login_type"]="teacher"

            st.rerun()

    with col2:
        st.header("I'm Student")
        st.image("https://cdn.vectorstock.com/i/500p/56/64/student-boy-using-computer-vector-30255664.jpg")
        if st.button("Student portal",type="primary",icon=':material/arrow_outward:',icon_position="right"):
          st.session_state["login_type"]="student"

          st.rerun()

    footer_home()