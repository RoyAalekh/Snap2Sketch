import streamlit as st
import time


class DisplayPanel:
    """
    DisplayPanel class is responsible for rendering the uploaded image and the processed image.
    """

    def render(self, uploaded_file):
        """
        Render the uploaded image and the processed image.
        """
        if uploaded_file:
            self.render_tabs_with_content(uploaded_file)
        else:
            self.render_welcome_message()

    def render_tabs_with_content(self, uploaded_file):
        """
        Render tabs for "Original," "Sketch," and "Animation."
        """
        tabs = st.tabs(["Original", "Sketch", "Animation"])
        with tabs[0]:
            self.display_original(uploaded_file)
        with tabs[1]:
            self.display_sketch()
        with tabs[2]:
            self.display_animation()

    @staticmethod
    def display_original(uploaded_file):
        """
        Display the original image.
        """
        st.image(uploaded_file, caption="Original Image", use_container_width=True)

    @staticmethod
    def display_sketch():
        """
        Display the processed sketch.
        """
        if st.session_state.get("adjusted_sketch") is not None:
            st.image(
                st.session_state.adjusted_sketch,
                caption="Sketch Image",
                use_container_width=True,
            )
        else:
            st.warning("No sketch available. Please generate a sketch.")

    @staticmethod
    def display_animation():
        """
        Display the animation of the sketching process with Play/Pause controls.
        """
        if "steps" in st.session_state:
            st.markdown("### Animation Controls")

            # Play/Pause Controls
            col1, col2 = st.columns(2)
            with col1:
                play_animation = st.button("Play Animation")
            with col2:
                stop_animation = st.button("Stop Animation")

            if play_animation:
                st.session_state.animation_running = True
            if stop_animation:
                st.session_state.animation_running = False

            # Display Animation
            animation_container = st.empty()
            if st.session_state.animation_running:
                st.info("Playing animation... Click 'Stop Animation' to pause.")
                for step_name, step_image in st.session_state["steps"]:
                    if not st.session_state.animation_running:
                        break
                    animation_container.image(
                        step_image, caption=step_name, use_container_width=True
                    )
                    time.sleep(0.9)  # Adjust timing for smooth animation
                st.session_state.animation_running = False
            elif not st.session_state.animation_running and not play_animation:
                st.info("Animation is paused. Click 'Play Animation' to continue.")
        else:
            st.warning("No animation steps available. Please generate a sketch.")

    @staticmethod
    def render_welcome_message():
        """
        Render a welcome message when no image is uploaded.
        """
        st.markdown(
            """
            <div style="text-align: center; padding: 50px; color: #666;">
                <h2>Welcome to Snap2Sketch</h2>
                <p>Upload an image using the control panel on the right to get started.</p>
                <p>Your transformed sketch will appear here once processing is complete.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
