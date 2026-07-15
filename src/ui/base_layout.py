import streamlit as st


def style_background_home():

    st.markdown("""

      <style>
                .stApp{

                background-color: #05060f;
            background-image: radial-gradient(1px 1px at 20px 30px, #ffffff, transparent),
                               radial-gradient(1px 1px at 90px 70px, #ffffff, transparent),
                               radial-gradient(1px 1px at 150px 20px, #ffffff, transparent),
                               radial-gradient(2px 2px at 200px 90px, #ffffff, transparent),
                               radial-gradient(1px 1px at 260px 40px, #ffffff, transparent),
                               radial-gradient(1px 1px at 320px 110px, #ffffff, transparent),
                               radial-gradient(2px 2px at 380px 60px, #ffffff, transparent),
                               radial-gradient(1px 1px at 440px 130px, #ffffff, transparent),
                               radial-gradient(1px 1px at 500px 10px, #ffffff, transparent);
            background-repeat: repeat;
            background-size: 550px 550px;

                }

                .stApp div[data-testid="stColumn"]{
                background-color:#E0E3FF !important;
                padding:2.5rem !important;
                border-radius:2rem !important;
                display:flex !important;
                flex-direction:column !important;
                align-items:center !important;
                text-align:center !important;
                }

                .stApp div[data-testid="stColumn"] h2{
                color:#1E1B4B !important;
                margin-bottom:1rem !important;
                }

                .stApp div[data-testid="stColumn"] div[data-testid="stImage"] img{
                width:140px !important;
                height:140px !important;
                object-fit:contain !important;
                border-radius:1rem !important;
                margin-bottom:1.5rem !important;
                }

                .stApp div[data-testid="stColumn"] .stButton{
                display:flex !important;
                justify-content:center !important;
                width:100% !important;
                }

      </style>

""",unsafe_allow_html=True)




def style_background_dashboard():

    st.markdown("""

      <style>
                .stApp{

                background-color: #05060f;
            background-image: radial-gradient(1px 1px at 20px 30px, #ffffff, transparent),
                               radial-gradient(1px 1px at 90px 70px, #ffffff, transparent),
                               radial-gradient(1px 1px at 150px 20px, #ffffff, transparent),
                               radial-gradient(2px 2px at 200px 90px, #ffffff, transparent),
                               radial-gradient(1px 1px at 260px 40px, #ffffff, transparent),
                               radial-gradient(1px 1px at 320px 110px, #ffffff, transparent),
                               radial-gradient(2px 2px at 380px 60px, #ffffff, transparent),
                               radial-gradient(1px 1px at 440px 130px, #ffffff, transparent),
                               radial-gradient(1px 1px at 500px 10px, #ffffff, transparent);
            background-repeat: repeat;
            background-size: 550px 550px;

                }

      </style>

""",unsafe_allow_html=True)




def style_base_layout():

    st.markdown("""

      <style>
                
                @import url('https://fonts.googleapis.com/css2?family=Geist+Pixel&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap');
                
                 /* Hide Top Bar of streamlit */
                
                  #MainMenu, footer,header{

                visibility:hidden;
                }

                .block-container{
                padding-top:1.5rem !important;
                
                }

                h1{

                font-family:"Geist Pixel" !important;
                font-size:3.5rem !important;
                line-height:0.9 !important;
                margin-bottom 0rem !important;

                
                }


                h2{

                font-family:"Geist Pixel" !important;
                font-size:2rem !important;
                line-height:1.1 !important;
                margin-bottom 0rem !important;

                
                }


                h3,h4,p {

                font-family:"Outfit",sans-serif;
                
                           
                
                }



                button{

                border-radius:1.5rem !important;
                background:#5865F2 !important;
                color:white !important;
                padding: 10px,20px !important;
                border:none !important;
                transition: transform 0.25s ease-in-out !important;
                
                
                }


                button[kind="secondary"]{

                border-radius:1.5rem !important;
                background:#EB459E !important;
                color:white !important;
                padding: 10px,20px !important;
                border:none !important;
                transition: transform 0.25s ease-in-out !important;
                
                
                }

                button[kind="tertiary"]{

                border-radius:1.5rem !important;
                background:black !important;
                color:white !important;
                padding: 10px,20px !important;
                border:none !important;
                transition: transform 0.25s ease-in-out !important;
                
                
                }


                button:hover{
                transform:scale(1.05)
                
                }  

      </style>

""",unsafe_allow_html=True)