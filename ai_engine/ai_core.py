import openai
from config import OPENAI_API_KEY

class AICore:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def analyze_command(self, command):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"حلل الأمر التالي: {command}",
            max_tokens=50
        )
        return response.choices[0].text.strip()
