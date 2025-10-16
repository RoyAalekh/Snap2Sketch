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
        if st.button("Help"):
            st.session_state.show_how_to_run = not st.session_state.show_how_to_run

    if st.session_state.show_how_to_run:
        st.info(
            """
        **How to Use Snap2Sketch:**
        
        1. **Upload Image** - Select a JPG, JPEG, or PNG file from your device
        2. **Choose Quality** - Pick Low, Medium, or High quality for processing
        3. **Generate Sketch** - Click the button to create your pencil sketch
        4. **Adjust Darkness** - Use the slider to fine-tune the sketch intensity
        5. **Download Result** - Save your finished sketch as a PNG file
        
        **Tips:** Higher quality settings provide more detail but take longer to process.
        """
        )
