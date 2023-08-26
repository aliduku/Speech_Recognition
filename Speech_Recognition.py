import streamlit as st
import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder
import tempfile

def transcribe_audio(api, audio_data, language):
    r = sr.Recognizer()

    try:
        # Create a temporary audio file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
            temp_audio_file.write(audio_data)
            temp_audio_file.seek(0)  # Reset file pointer
            # Use the temporary audio file as the audio source
            with sr.AudioFile(temp_audio_file.name) as source:
                audio = r.record(source)
                if api == "Google":
                    return r.recognize_google(audio, language=language)
                elif api == "WHISPER":
                    return r.recognize_whisper(audio, language=language.split('-')[0])
                elif api == "Sphinx":
                    if language == "en-US":
                        return r.recognize_sphinx(audio, language=language)
                    else:
                        raise sr.UnknownValueError("Sphinx supports only en-US")
    except sr.UnknownValueError as e:
        st.error(f"Error: Sorry, the model did not understand. {str(e)}")
    except sr.RequestError as e:
        st.error(f"Error connecting to the speech recognition service: {str(e)}")

def main():
    st.title("Multilingual Speech Recognition App")
    st.write("Click on the microphone icon to start recording and speaking:")

    api_choice = st.selectbox("Select Speech Recognition API", ("Google", "WHISPER", "Sphinx"))
    language_choice = st.selectbox("Select Language", ("en-US", "de-DE", "ar-EG"))

    # Capture audio data using the audio recorder
    audio_data = audio_recorder()

    if st.button("Start Transcription") and audio_data:
        # Transcribe the captured audio
        transcribed_text = transcribe_audio(api_choice, audio_data, language=language_choice)
        if "transcription" not in st.session_state:
            st.session_state.transcription = ""
        st.session_state.transcription += f" {transcribed_text}"
        st.write("Transcription:", st.session_state.transcription)

    if st.button("Clear Transcription"):
        # Clear the transcription and reset audio_data
        st.session_state.transcription = ""
        audio_data = None
        st.write("Transcription cleared.")

    if hasattr(st.session_state, "transcription") and st.session_state.transcription and st.download_button(label="Download Transcription!", data=st.session_state.transcription, file_name="transcription.txt", mime="text/plain"):
        st.success("Downloaded Successfully.")

if __name__ == "__main__":
    main()
