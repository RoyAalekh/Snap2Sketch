# components/styles.py
import streamlit as st


def load_css():
    """
    Load CSS styles.

    This function loads the CSS styles for the Streamlit app. It is used to style the app.
    """
    st.markdown(
        """
        <style>
        /* Main title styling */
        .big-title {
            font-size: 3.5rem !important;
            font-weight: 700 !important;
            color: #1E88E5 !important;
            margin-bottom: 0 !important;
            padding-bottom: 0 !important;
        }
        .subtitle {
            color: #424242 !important;
            font-size: 1.2rem !important;
            font-weight: 400 !important;
            margin-top: 0 !important;
        }

        /* Container styling */
        .stRadio > label {
            font-size: 1rem !important;
            color: #424242 !important;
        }

        /* Button styling */
        .stButton > button {
            width: 100%;
            border-radius: 8px !important;
            height: 3rem;
            font-weight: 500 !important;
        }

        /* Divider styling */
        .divider {
            margin: 2rem 0;
            border-bottom: 1px solid #EEEEEE;
        }

        /* Upload box styling */
        .uploadbox {
            border: 2px dashed #1E88E5;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            background: #F8F9FA;
        }

        /* Info box styling */
        .stAlert {
            background-color: #F3F4F6 !important;
            border: none !important;
            border-radius: 10px !important;
        }

        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """,
        unsafe_allow_html=True,
    )
