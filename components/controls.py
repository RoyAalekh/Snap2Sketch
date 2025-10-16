# components/controls.py
import streamlit as st


class ControlPanel:
    def __init__(self, image_processor):
        self.image_processor = image_processor

    def render(self):
        """
        Render the control panel for user inputs.
        """
        with st.container():
            uploaded_file = st.file_uploader(
                "Upload Image",
                type=["jpg", "jpeg", "png"],
                label_visibility="collapsed",
            )

        if uploaded_file:
            self.render_controls(uploaded_file)

        return uploaded_file

    def render_controls(self, uploaded_file):
        """
        Render the controls for quality selection, sketch generation, and darkness adjustment.
        """
        st.markdown("### Customize Your Sketch")

        # Quality Selection with Description
        st.markdown("#### Step 1: Select Quality")
        st.write(
            "Choose the quality level for your pencil sketch. Higher quality provides finer details but may take longer to process."
        )
        quality = st.radio(
            "Quality",
            ["Low", "Medium", "High"],
            index=2,
            horizontal=True,
            label_visibility="collapsed",
            help="Select the desired quality for the pencil sketch.",
        )

        # Generate Sketch Button
        st.markdown("#### Step 2: Generate Your Sketch")
        st.write("Click the button below to transform your image into a pencil sketch.")
        generate_button = st.button(
            "Generate Sketch",
            use_container_width=True,
            help="Click to generate the pencil sketch based on your quality selection.",
        )

        if generate_button:
            self.process_image(uploaded_file, quality)

        # Darkness Adjustment Controls
        if "original_sketch" in st.session_state:
            self.render_adjustment_controls()

    def render_adjustment_controls(self):
        """
        Render controls to adjust darkness of the generated sketch.
        """
        st.markdown("#### Step 3: Fine-Tune Your Sketch")
        st.write(
            "Adjust the darkness of the sketch to your preference using the slider below."
        )

        # Darkness Slider
        darkness = st.slider(
            "Adjust Darkness",
            1,
            5,
            3,
            step=1,
            label_visibility="collapsed",
            help="Fine-tune the darkness level of your sketch. Higher values make it darker.",
        )
        adjusted_sketch = self.image_processor.adjust_sketch(
            st.session_state["original_sketch"], darkness
        )
        st.session_state.adjusted_sketch = adjusted_sketch

        # Download Button
        self.render_download_button()

    def render_download_button(self):
        """
        Render the download button for the adjusted sketch.
        """
        st.markdown("#### Step 4: Download Your Sketch")
        st.write(
            "Save your sketch as an image file by clicking the download button below."
        )
        if st.session_state.adjusted_sketch is not None:
            buffer = self.image_processor.prepare_download(
                st.session_state.adjusted_sketch
            )
            st.download_button(
                "Download Sketch",
                data=buffer,
                file_name="sketch.png",
                mime="image/png",
                use_container_width=True,
            )

    def process_image(self, uploaded_file, quality):
        """
        Process the uploaded image and save the resulting sketch and steps in session state.
        """
        with st.spinner("Creating your masterpiece..."):
            steps = self.image_processor.process_image(uploaded_file, quality)
            st.session_state["original_sketch"] = steps[-1][1]  # Final sketch
            st.session_state["steps"] = steps  # Transformation steps
            st.session_state.adjusted_sketch = None  # Reset any adjustments
