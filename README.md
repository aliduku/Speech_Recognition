# Speech Recognition App using Streamlit

This repository contains a simple Speech Recognition App developed using Streamlit, which allows users to transcribe spoken audio into text using various speech recognition APIs.

## Overview

The Speech Recognition App is built using Python and Streamlit, utilizing the `speech_recognition` library to interface with different speech recognition APIs. The app provides the following functionalities:

- User can select a speech recognition API from Google, Whisper, and Sphinx.
- User can choose the language for transcription from a list of supported languages.
- User can start recording audio through the microphone for transcription.
- Transcribed text is displayed on the app interface.
- User can clear the transcription history.
- User can download the transcription as a text file.

## Prerequisites

- Python 3.x
- Streamlit
- `speech_recognition` library
- `whisper` library (for Whisper ASR, if using)
- Active internet connection (for API-based speech recognition)

## How to Run

1. Install the required libraries using the following command:
   
2. Clone this repository:

3. Run the Streamlit app:

4. The app will open in your browser. Select the desired API and language, then click "Start Recording" to transcribe your speech.

## Access the Web App

Access the Speech Recognition App through this link: [Speech Recognition App](https://speechrecognition-sehtel9fwvhk75n3c5hcxk.streamlit.app/)

## Notes

- The app uses Google, Whisper, and Sphinx APIs for speech recognition.
- Whisper requires additional configuration for the languages.
- The Sphinx API supports only English (en-US).
- The app uses the Streamlit session state to maintain the transcription history.

Feel free to customize the app and its features according to your requirements.
