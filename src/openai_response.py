import openai
import os
from api_secrets import OPEN_AI_API_KEY

openai.api_key = OPEN_AI_API_KEY

def get_answer(question: str) -> str:

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=question,
        max_tokens=100,
        )

    text_response = response['choices'][0]['text'].strip()
    return text_response

def main():
    pass

if __name__ == "__main__":
    main()

