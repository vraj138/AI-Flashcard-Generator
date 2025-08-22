# AI Flashcard Generator  

An AI-powered tool that transforms raw text into **question–answer flashcards** using **NLP techniques** like summarization, rephrasing, and question generation.  
It also integrates **Text-to-Speech (TTS)** to create **audio flashcards**, making learning more **accessible, multimodal, and hands-free**.  

---

## Features  
- **Automatic Flashcard Creation** – Convert raw text into structured Q&A pairs.  
- **NLP-Powered** – Uses OpenAI API for summarization, rephrasing, and question generation.  
- **Text-to-Speech (TTS)** – Generates audio flashcards for auditory learners.  
- **Multi-format Output** – Export flashcards as JSON, CSV, or audio files.  
- **Interactive UI (Optional)** – Built with Streamlit for a simple web interface.  

---

## Project Structure  
```
ai-flashcard-generator/
│── README.md                # Project overview, setup, usage
│── requirements.txt         # Dependencies
│
├── src/                     # Source code
│   ├── flashcard_generator.py   # Core NLP logic with OpenAI API
│   ├── tts_converter.py         # Text-to-Speech module
│   ├── utils.py                 # Helper functions
│   └── app.py                   # Streamlit web app
│
├── data/                    # Input & output data
│   ├── sample_text.txt          # Example input
│   ├── flashcards.json          # Output (JSON)
│   └── flashcards.csv           # Output (CSV)
│
├── audio/                   # Audio flashcards
│   ├── flashcard1.mp3
│   └── flashcard2.mp3
│
└── notebooks/               # Experimentation
    └── demo.ipynb
```
---

## Installation  

1. Clone the repository  
```bash
git clone https://github.com/your-username/ai-flashcard-generator.git
cd ai-flashcard-generator
Create and activate a virtual environment
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set your OpenAI API key
```bash
export OPENAI_API_KEY="your_api_key_here"   # Linux/Mac
setx OPENAI_API_KEY "your_api_key_here"     # Windows
```
---
## Usage

1. Generate Flashcards (CLI)

```bash
python src/flashcard_generator.py --input data/sample_text.txt --output data/flashcards.json
```

2. Convert Flashcards to Audio
```bash
python src/tts_converter.py --input data/flashcards.json --output audio/
```

3. Run Web App (Optional with Streamlit)
```bash
streamlit run src/app.py
```
---
## Example
Input (sample_text.txt):

```csharp
The mitochondria is the powerhouse of the cell. It generates ATP through cellular respiration.
```
Generated Flashcard (JSON):

```json
{
  "question": "What is the powerhouse of the cell?",
  "answer": "Mitochondria"
}
```

Audio Output: 🎧 flashcard1.mp3

---

## Future Improvements
- Add speech-to-text so users can speak notes and auto-generate flashcards.
- Integrate spaced repetition algorithm for smarter studying.
- Export flashcards to Anki or other learning platforms.

### Tech Stack
- **Programming Language:** Python  
- **AI/NLP:** OpenAI API  
- **Text-to-Speech (TTS):** gTTS, pyttsx3  
- **Frontend/UI:** Streamlit  
- **Data Handling:** Pandas, NumPy  

---

## Contributing
Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a PR.

---

## License
This project is licensed under the MIT License.


