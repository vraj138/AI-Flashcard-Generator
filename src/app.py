import streamlit as st
from flashcard_generator import generate_flashcards, AUDIO_DIR, DATA_DIR
from tts_converter import text_to_speech
import os

st.set_page_config(page_title="AI Flashcard Generator", layout="wide")

st.title("AI Flashcard Generator")
st.write("Generate study flashcards with audio from your text input.")

# Input: text or file
input_option = st.radio("Choose input method:", ["Enter text", "Upload .txt file"])

text_input = ""
if input_option == "Enter text":
    text_input = st.text_area("Enter your study text here:", height=200)
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file:
        text_input = uploaded_file.read().decode("utf-8")

# Number of flashcards
num_questions = st.slider("Number of flashcards to generate:", 1, 10, 3)

# Generate Button
if st.button("Generate Flashcards"):
    if not text_input.strip():
        st.warning("Please provide some text input.")
    else:
        with st.spinner("Generating flashcards..."):
            flashcards = generate_flashcards(text_input, num_questions=num_questions)

        st.success(f"Generated {len(flashcards)} flashcards!")

        # Display flashcards
        for i, card in enumerate(flashcards):
            with st.expander(f"Flashcard {i+1}"):
                st.markdown(f"**Q:** {card['question']}")
                st.markdown(f"**A:** {card['answer']}")

                # Play audio if file exists
                audio_path = os.path.join(AUDIO_DIR, f"flashcard_{i+1}.mp3")
                if os.path.exists(audio_path):
                    with open(audio_path, "rb") as audio_file:
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format="audio/mp3")

        # Show download links for data
        json_file = os.path.join(DATA_DIR, "flashcards.json")
        csv_file = os.path.join(DATA_DIR, "flashcards.csv")

        st.download_button("⬇️ Download Flashcards (JSON)", open(json_file, "rb"), "flashcards.json")
        st.download_button("⬇️ Download Flashcards (CSV)", open(csv_file, "rb"), "flashcards.csv")
