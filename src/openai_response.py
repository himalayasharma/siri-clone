import openai
import os
from api_secrets import OPEN_AI_API_KEY
import logging

openai.api_key = OPEN_AI_API_KEY
logging.basicConfig(filename='data/logs/conversation.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

def get_answer(question: str) -> str:

    logging.info("Sending transcription prompt to OpenAI API")
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=question,
        max_tokens=100,
        )
    logging.info("Received answer to prompt from OpenAI API")
    text_response = response['choices'][0]['text'].strip()
    return text_response

def main():
    pass

if __name__ == "__main__":
    main()

