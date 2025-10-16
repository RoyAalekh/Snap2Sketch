# Snap2Sketch

A web application for converting images into pencil sketches with adjustable quality levels and step-by-step transformation features. Built with Python, OpenCV, and Streamlit for an intuitive user experience.

## Features

- Convert uploaded images to pencil sketches
- Adjustable sketch quality settings
- Step-by-step transformation visualization  
- Real-time image processing using OpenCV
- Clean, responsive web interface
- Support for common image formats (JPEG, PNG, etc.)

## Live Demo

[Snap2Sketch Web Application](https://snap2sketch.streamlit.app/)

## Technical Stack

- **Frontend**: Streamlit web framework
- **Image Processing**: OpenCV (cv2)
- **Computing**: NumPy for numerical operations
- **Image Handling**: Pillow (PIL) for image manipulation
- **Deployment**: Streamlit Cloud

## Local Installation

1. Clone the repository:
```bash
git clone https://github.com/RoyAalekh/Snap2Sketch.git
cd Snap2Sketch
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

## How It Works

The application uses computer vision techniques to convert photographs into pencil sketch-like drawings:

1. **Image Upload**: Users upload an image through the web interface
2. **Preprocessing**: Image is converted to grayscale
3. **Edge Detection**: Canny edge detection identifies prominent features
4. **Sketch Generation**: Combination of blur and edge enhancement creates sketch effect
5. **Quality Control**: Adjustable parameters for fine-tuning the output

## Project Structure

```
Snap2Sketch/
├── app.py                 # Main Streamlit application
├── utils.py               # Image processing utilities
├── requirements.txt       # Python dependencies
├── components/            # Modular UI components
│   ├── controls.py        # Control panel interface
│   ├── display.py         # Image display panel
│   ├── header.py          # Application header
│   ├── footer.py          # Application footer
│   └── image_processor.py # Core image processing logic
└── .devcontainer/         # Development container configuration
```

## Usage

1. Access the web application through the live demo link
2. Upload an image using the file upload interface
3. Adjust quality settings as desired
4. View the generated pencil sketch
5. Download the processed image

## Development

The application is built with modular components for maintainability:

- **ControlPanel**: Handles user inputs and parameter adjustments
- **DisplayPanel**: Manages image display and processing results
- **ImageProcessor**: Contains core OpenCV-based processing algorithms

## Requirements

- Python 3.7+
- Streamlit
- OpenCV (opencv-python-headless)
- NumPy
- Pillow

## License

MIT License