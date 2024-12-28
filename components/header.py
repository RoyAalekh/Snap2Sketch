# components/header.py
import streamlit as st


def render_header():
    """
    Render the header of the app
    """

    st.markdown('<h1 class="big-title">Snap2Sketch</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle" style="margin-top: 10px;">Transform your photos into artistic pencil sketches ✨</p>',
        unsafe_allow_html=True,
    )
