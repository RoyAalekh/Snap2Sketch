# components/help.py
import streamlit as st


def render_help():
    """
    Render help button

    This function renders the help button and the help message. 3 columns are used to align the help button to the right.
    col1: 6/8 width
    col2: 1/8 width
    col3: 1/8 width

    When the help button is clicked, the help message is displayed.
    """
    col1, col2, col3 = st.columns([6, 1, 1])
    with col3:
        if st.button("❓ Help"):
            st.session_state.show_how_to_run = not st.session_state.show_how_to_run

    if st.session_state.show_how_to_run:
        st.info(
            """
        🎨 **Quick Guide:**
        1. 📤 Upload image
        2. 🔍 Pick quality
        3. ✨ Generate
        4. 🎚️ Adjust
        5. 💾 Download
        """
        )
