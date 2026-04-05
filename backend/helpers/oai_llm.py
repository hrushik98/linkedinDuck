from openai import OpenAI
from .config import settings

class OAI_LLM:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def generate_chat_response(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

