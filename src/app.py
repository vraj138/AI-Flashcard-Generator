import streamlit as st
from flashcard_generator import generate_flashcards
from tts_converter import text_to_speech
import os

st.set_page_config(page_title="AI Flashcard Generator", page_icon="📚", layout="wide")

st.title("📚 AI Flashcard Generator")
st.markdown("Generate study flashcards with **text + audio playback** for efficient learning.")

# User input
text_input = st.text_area("✍️ Enter your text:", height=200)
num_questions = st.slider("🔢 Number of flashcards", min_value=1, max_value=10, value=3)

if st.button("🚀 Generate Flashcards"):
    if not text_input.strip():
        st.warning("Please enter some text to generate flashcards.")
    else:
        with st.spinner("Generating flashcards..."):
            flashcards = generate_flashcards(text_input, num_questions)

        st.success("✅ Flashcards generated!")

        for i, card in enumerate(flashcards):
            with st.container():
                st.markdown(f"### 📝 Flashcard {i+1}")
                st.markdown(f"**Q:** {card['question']}")
                st.markdown(f"**A:** {card['answer']}")

                # Generate single audio file for Q + A
                audio_text = f"Question: {card['question']}. Answer: {card['answer']}."
                filename = f"flashcard_{i+1}.mp3"
                text_to_speech(audio_text, filename)

                # Show speaker player
                with open(filename, "rb") as audio_file:
                    st.audio(audio_file.read(), format="audio/mp3")

                st.divider()
