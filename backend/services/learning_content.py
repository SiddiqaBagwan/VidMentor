import json
import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_learning_content(transcript):

    prompt = f"""
    Analyze the following YouTube transcript.

    Return ONLY valid JSON.

    Format:

    {{
        "summary": "...",
        "key_concepts": [
            "...",
            "..."
        ],
        "important_terms": [
            "...",
            "..."
        ]
    }}

    Transcript:
    {transcript}
    """

    response = model.generate_content(prompt)

    text = response.text

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)