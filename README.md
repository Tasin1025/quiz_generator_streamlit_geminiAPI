# Quiz Generator Streamlit App

A Streamlit-based web app that generates notes, audio transcription, and quizzes from uploaded images.

Live URL: https://quiz-generator-tasin.streamlit.app/

## Features

- Upload up to 3 images
- Generate a summarized note from the images
- Convert the note into audio transcription
- Generate quiz questions at selected difficulty levels: Easy, Medium, Hard

## Files

- `app.py` – Main Streamlit application entry point
- `api_calling.py` – Contains core image processing, note generation, audio generation, text cleaning, and quiz generation logic
- `requirements.txt` – Python dependencies needed for the project

## Prerequisites

- Python 3.11+ recommended
- A virtual environment is strongly recommended

## Setup

1. Open a terminal in the project directory.
2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Usage

1. Upload 1 to 3 image files (`jpg`, `jpeg`, or `png`).
2. Select a quiz difficulty level.
3. Click the button to generate:
   - Generated note
   - Audio transcription
   - Quiz content

## Notes

- The app UI is built with Streamlit.
- Image processing and AI/API functionality is handled in `api_calling.py`.
- If you add or change dependencies, update `requirements.txt` accordingly.

## Dependencies

The project depends on packages including but not limited to:

- `streamlit`
- `Pillow`
- `google-genai`
- `gTTS`
- `httpx`
- `numpy`
- `pandas`

See `requirements.txt` for the full dependency list.
