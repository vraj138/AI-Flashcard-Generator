from openai import OpenAI
import json
import csv
from dotenv import load_dotenv
import os
from tts_converter import text_to_speech

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

AUDIO_DIR = "audio"
DATA_DIR = "data"
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

def generate_flashcards(text, num_questions):
    prompt = f"""
    Generate {num_questions} study flashcards in JSON format 
    from the following text. 
    The response must be either:
    1. A JSON array of flashcards, OR
    2. A JSON object with a "flashcards" key containing the list.
    
    Each flashcard should have a 'question' and an 'answer'.
    Keep them concise and useful for studying.

    Text: {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that creates flashcards."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        response_format={"type": "json_object"}
    )

    try:
        raw = response.choices[0].message.content
        flashcards = json.loads(raw)

        # If response is wrapped in {"flashcards": [...]}, extract the list
        if isinstance(flashcards, dict) and "flashcards" in flashcards:
            flashcards = flashcards["flashcards"]

    except Exception as e:
        flashcards = [{"question": "Error parsing", "answer": str(e)}]

    # Clean + save audio
    cleaned_flashcards = []
    for i, card in enumerate(flashcards):
        if isinstance(card, dict) and "question" in card and "answer" in card:
            cleaned_flashcards.append(card)

            combined_filename = os.path.join(AUDIO_DIR, f"flashcard_{i+1}.mp3")

            # Combine question and answer into one string
            combined_text = f"Question: {card['question']}. Answer: {card['answer']}."

            text_to_speech(combined_text, combined_filename)

        else:
            cleaned_flashcards.append({
                "question": "Error parsing",
                "answer": str(card)
            })
    
    json_path = os.path.join(DATA_DIR, "flashcards.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(cleaned_flashcards, f, ensure_ascii=False, indent=4)

    # --- Save to CSV file ---
    csv_path = os.path.join(DATA_DIR, "flashcards.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["question", "answer"])
        writer.writeheader()
        writer.writerows(cleaned_flashcards)

    return cleaned_flashcards


# Example
if __name__ == "__main__":
    with open("data/sample_text.txt", "r", encoding="utf-8") as f:
        text_input = f.read()

    flashcards = generate_flashcards(text_input, num_questions=1)
    print(flashcards)
