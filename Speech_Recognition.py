import streamlit as st
import speech_recognition as sr

def transcribe_audio(api, audio, language):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Speak now...")
        audio = r.listen(source)
        st.info("Transcribing...")

        try:
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
    st.write("Click on the microphone to start speaking:")

    api_choice = st.selectbox("Select Speech Recognition API", ("Google", "WHISPER", "Sphinx"))
    language_choice = st.selectbox("Select Language", ("en-US", "de-DE", "ar-EG"))

    record_button = st.button("Start Recording")
    clear_button = st.button("Clear Transcription")

    if record_button:
        audio = None
        transcribed_text = transcribe_audio(api_choice, audio, language=language_choice)
        if "transcription" not in st.session_state:
            st.session_state.transcription = ""
        st.session_state.transcription += f" {transcribed_text}"
        st.write("Transcription:", st.session_state.transcription)

    if clear_button:
        st.session_state.transcription = ""
        st.write("Transcription cleared.")

    if hasattr(st.session_state, "transcription") and st.session_state.transcription and st.download_button(label="Download Transcription!", data=st.session_state.transcription, file_name="transcription.txt", mime="text/plain"):
        st.success("Downloaded Successfuly.")

if __name__ == "__main__":
    main()
