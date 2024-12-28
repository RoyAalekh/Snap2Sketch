from io import BytesIO

from PIL import Image
import cv2
import numpy as np
from typing import List, Tuple


def process_image_step_by_step(image_file: BytesIO, quality: str) -> List[Tuple[str, Image.Image]]:
    """
    Processes the uploaded image step-by-step and returns intermediate images for animation.

    Parameters:
    ----------
    image_file : BytesIO
        The uploaded image file in binary format.
    quality : str
        The quality of the sketch, either "low", "medium", or "high".

    Returns:
    -------
    List[Tuple[str, Image.Image]]
        A list of tuples, where each tuple contains the step name and the corresponding PIL Image.
    """
    # Open the uploaded image
    image = Image.open(image_file)
    original = np.array(image)

    # Step 1: Convert to grayscale
    gray_image = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)

    # Step 2: Invert the grayscale image
    inverted_image = 255 - gray_image

    # Step 3: Apply Gaussian blur
    blur_quality = {"low": (31, 31), "medium": (21, 21), "high": (11, 11)}
    blurred_image = cv2.GaussianBlur(inverted_image, blur_quality[quality], 0)

    # Step 4: Invert the blurred image
    inverted_blur = 255 - blurred_image

    # Step 5: Generate the pencil sketch
    scale_quality = {"low": 128.0, "medium": 192.0, "high": 256.0}
    sketch_image = cv2.divide(gray_image, inverted_blur, scale=scale_quality[quality])

    # Collect steps as images for animation
    steps = [
        ("Original Image", Image.fromarray(original)),
        ("Grayscale", Image.fromarray(gray_image)),
        ("Inverted", Image.fromarray(inverted_image)),
        ("Blurred", Image.fromarray(blurred_image)),
        ("Final Sketch", Image.fromarray(sketch_image)),
    ]
    return steps


def adjust_sketch_darkness(sketch: Image.Image, darkness: int) -> Image.Image:
    """
    Adjusts the darkness level of the sketch.

    Parameters:
    ----------
    sketch : Image.Image
        The PIL Image of the final sketch.
    darkness : int
        The darkness level (1 to 5).

    Returns:
    -------
    Image.Image
        The adjusted PIL Image with modified darkness.
    """
    sketch_np = np.array(sketch)
    adjusted_sketch = Image.fromarray((sketch_np * darkness).clip(0, 255).astype(np.uint8))
    return adjusted_sketch
