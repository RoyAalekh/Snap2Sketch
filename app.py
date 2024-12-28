# app.py
import streamlit as st

from components.controls import ControlPanel
from components.display import DisplayPanel
from components.footer import render_footer
from components.header import render_header
from components.help import render_help
from components.image_processor import ImageProcessor
from components.styles import load_css


class Snap2SketchApp:
    """
    Snap2SketchApp class is responsible for running the Snap2Sketch app.
    """

    def __init__(self):
        self.setup_page()
        self.initialize_session_state()
        self.image_processor = ImageProcessor()

    @staticmethod
    def setup_page():
        """
        This method sets up the page configuration.
        """
        st.set_page_config(
            page_title="Snap2Sketch",
            page_icon="✏️",
            layout="wide",
            initial_sidebar_state="collapsed",
        )
        load_css()

    @staticmethod
    def initialize_session_state():
        """
        This method initializes the session state.
        """
        defaults = {
            "show_how_to_run": False,
            "current_display": None,
            "animation_running": False,
            "adjusted_sketch": None,
        }
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    def run(self):
        """
        This method runs the Snap2Sketch app.
        """
        # Render header
        render_header()

        # Render help section
        render_help()

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        # Main content layout
        content_col, control_col = st.columns([2, 1])

        # Initialize control panel
        with control_col:
            control_panel = ControlPanel(self.image_processor)
            uploaded_file = control_panel.render()

        # Initialize display panel
        with content_col:
            display_panel = DisplayPanel()
            display_panel.render(uploaded_file)

        # Render footer
        render_footer()


if __name__ == "__main__":
    app = Snap2SketchApp()
    app.run()
