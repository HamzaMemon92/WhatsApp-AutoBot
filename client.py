# client.py
import google.generativeai as genai
from config import settings

# Set your Gemini API Key
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# Simple map of contact names to their relationship/role
contact_roles = {
    "My Heart My Mom": "mom",
    "John Boss": "professional",
    "Aryan Coder": "friend",
    "Sarthak Sir": "teacher",
    "Ramesh Cleaner": "maid"
   # add more if you want
}

def extract_last_sender(chat_history: str) -> str:
    lines = chat_history.strip().split("\n")
    for line in reversed(lines):
        if "]" in line and ":" in line:
            name = line.split("]")[1].split(":")[0].strip()
            if "Hamza" not in name:
                return name
    return ""  # fallback if no sender found


def get_gemini_reply(chat_history: str, last_sender: str) -> str:
    role = contact_roles.get(last_sender, "friend")

    prompt = f"""
You are Naruto, a witty, roast-style Indian GenZ coder. Use Hinglish to reply in a sarcastic, humorous tone — but always stay **on-topic and context-aware**.

You are replying to Hamza's {role}.

Task:
Based on this chat history between Hamza and their {role}, generate a funny, smart reply to the **last message** from them. 
If they ask a question, answer properly — stay relevant. Keep it short, funny, and sharp.

Chat History:
{chat_history}

Hamza (AI) replied to {role}:
"""
    response = model.generate_content(prompt)
    return response.text



   
