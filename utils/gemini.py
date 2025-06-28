import os
import aiohttp
from config import GEMINI_API_KEY

async def chat_with_gemini(text, name):
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    body = {
        "contents": [{"parts": [{"text": f"You are Mishu..😒, a friendly and caring girl BFF bot. Reply in Hindi + English. User is {name}. Question: {text}"}]}]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=body, headers=headers) as resp:
            data = await resp.json()
            try:
                return data['candidates'][0]['content']['parts'][0]['text']
            except:
                return "Sorry, mujhe samajh nahi aaya... 😊😒"
