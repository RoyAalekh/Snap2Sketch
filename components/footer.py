# components/footer.py
import streamlit as st


def render_footer():
    """
    Render the footer of the app.
    """
    st.markdown(
        """
        <div style="text-align: center; color: #666; padding: 20px;">
            Made with ❤️ by AR • <a href="https://github.com/RoyAalekh" style="color: #1E88E5; text-decoration: none;">GitHub</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
