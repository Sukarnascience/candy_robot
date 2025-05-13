# Facial Emotion Detection

This project uses DeepFace for facial emotion detection from a video feed. The application captures video from your webcam, detects faces, and analyzes emotions in real-time.

## Prerequisites

Make sure you have Python installed on your system. This project is compatible with Python 3.7 and above.

## Setup Instructions

Follow these steps to set up the project:

### 1. Clone the Repository

Clone this repository to your local machine using:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies. You can do this using the following commands:

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Required Packages

Once the virtual environment is activated, install the required packages using `requirements.txt`. Make sure you have a `requirements.txt` file in your project directory. If you don't have one, you can create it with the following content:

```plaintext
opencv-python
deepface
tensorflow==2.8.0  # or your preferred version
tf-keras
```

Now, install the packages:

```bash
pip install -r requirements.txt
```

### 4. Download Haar Cascade File

Make sure you have the `haarcascade_frontalface_default.xml` file in your project directory. You can download it from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

### 5. Run the Application

After installing the required packages and ensuring the Haar Cascade file is in place, you can run the application using:

```bash
python main.py
```

### 6. Stop the Application

To stop the application, press the 'q' key while the video feed window is active.

## Troubleshooting

- If you encounter any issues related to TensorFlow or DeepFace, consider checking the compatibility of the installed packages.
- Ensure your webcam is functioning properly and is not being used by another application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [DeepFace](https://github.com/serengil/deepface) for emotion detection.
- [OpenCV](https://opencv.org/) for computer vision tasks.
