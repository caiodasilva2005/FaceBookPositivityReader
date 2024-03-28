import read_data as rd
import ai 

LOVE_SCORE = 10
LIKE_SCORE = 5
WOW_SCORE = 2
HAHA_SCORE = 1
SAD_SCORE = -2
ANGRY_SCORE = -5

def getScoreFromMessage(message):
    score = ai.getAiScore(message)
    try:
        score = int(score)
    except ValueError:
        score = 0
    
    return score

def getScoreFromMessages(messages):

    scores = []
    for message in messages:
        score = ai.getAiScore(message)
        try:
            score = int(score)
            scores.append(score)
        except ValueError:
            continue
    
    score_sum = 0
    for score in scores:
        score_sum += score

    print(score_sum)

    return score_sum 

def getScoreFromReactions(reactions):

    score = 0
    
    score += reactions['love'] * LOVE_SCORE
    score += reactions['like'] * LIKE_SCORE
    score += reactions['wow'] * WOW_SCORE
    score += reactions['haha'] * HAHA_SCORE
    score += reactions['sad'] * SAD_SCORE
    score += reactions['angry'] * ANGRY_SCORE

    return score