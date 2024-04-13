import openai
from Key1 import MYSK


openai.api_key = MYSK
AI_TOKENS = 5

# Uses ChatGPT 3.5 to repspond with positivity score for a message
def getAiScore(message):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Rate this message on a scale of 1 to 100 on how positive it is (respond with only a number): {}".format(message)}
        ],
        max_tokens = AI_TOKENS)
    
    return chat_completion.choices[0].message["content"]

    