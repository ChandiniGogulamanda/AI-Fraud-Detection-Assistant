import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def explain(text, score):

    prompt = f"""
You are a fraud detection expert.

Transaction:
{text}

Fraud Score: {score}

Analyze:
1. Risk level
2. Fraud indicators
3. Recommended action

Keep the answer under 100 words.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=150
    )

    return response.choices[0].message.content