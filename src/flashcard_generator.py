from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_flashcards(text, num_questions):
    prompt = f"""
    Generate {num_questions} study flashcards in JSON format 
    from the following text. Each flashcard should have a 'question' 
    and an 'answer'. Keep them concise and useful for studying.

    Text: {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that creates flashcards."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        response_format={ "type": "json_object" }
    )

    try:
        flashcards = json.loads(response.choices[0].message.content)
    except Exception:
        flashcards = [{"question": "Error parsing", "answer": response.choices[0].message.content}]

    return flashcards


# Example
text_input = "The mitochondria is the powerhouse of the cell. It generates energy through cellular respiration."
flashcards = generate_flashcards(text_input, num_questions=3)
print(flashcards)
