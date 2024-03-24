import openai
from Key1 import mysk


openai.api_key = mysk
AI_TOKENS = 5

def getAiScore(message):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Rate this message on a scale of 1 to 100 on how positive it is (respond with only a number): {}".format(message)}
        ],
        max_tokens = AI_TOKENS)
    
    return chat_completion.choices[0].message["content"]

def getScoreFromMessages(messages):
    scores = []
    for message in messages:
        score = getAiScore(message)
        try:
            score = int(score)
            scores.append(score)
        except ValueError:
            print("invalid score")
            continue
    
    score_sum = 0
    for score in scores:
        score_sum += score

    return score_sum
    