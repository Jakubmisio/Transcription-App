import streamlit as st
import whisper
import tempfile

st.title("Translator App")

# Upload the file
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

model = whisper.load_model("small")
st.text("Model Loaded")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")

        # Save uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio.write(audio_file.read())
            temp_audio_path = temp_audio.name

        # Transcribe using whisper
        transcription = model.transcribe(temp_audio_path)

        st.sidebar.success("Transcription Complete")
        st.markdown("### Transcription")
        st.markdown(transcription["text"])
    else:
        st.sidebar.error("Please upload an audio file")

# Optional: Play audio
if audio_file:
    st.sidebar.header("Play Original Audio File")
    st.sidebar.audio(audio_file)