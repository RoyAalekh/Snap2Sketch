# components/image_processor.py
from io import BytesIO
from utils import process_image_step_by_step, adjust_sketch_darkness


class ImageProcessor:
    """
    ImageProcessor class is responsible for processing the image and adjusting the darkness of the sketch.
    """

    @staticmethod
    def process_image(uploaded_file, quality):
        """
        This method processes the image step by step and returns the steps.
        """
        steps = process_image_step_by_step(uploaded_file, quality.lower())
        return steps

    @staticmethod
    def adjust_sketch(sketch, darkness):
        """
        This method adjusts the darkness of the sketch.
        """
        return adjust_sketch_darkness(sketch, darkness)

    @staticmethod
    def prepare_download(sketch):
        """
        This method prepares the sketch for download.
        """
        buffer = BytesIO()
        sketch.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer
