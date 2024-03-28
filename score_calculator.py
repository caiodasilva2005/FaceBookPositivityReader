import read_data as rd
import media_objects as mo
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


def getScoreFromReactions(reactions):

    score = 0
    
    score += reactions['love'] * LOVE_SCORE
    score += reactions['like'] * LIKE_SCORE
    score += reactions['wow'] * WOW_SCORE
    score += reactions['haha'] * HAHA_SCORE
    score += reactions['sad'] * SAD_SCORE
    score += reactions['angry'] * ANGRY_SCORE

    return score

def getScoreFromMedia(object):
    score  = 0

    if object is None:
        return score
    
    score += getScoreFromMessage(object.message)
    score += getScoreFromReactions(object.reactions)

    return score
    
def getPagePositivityScore(page):
    positivity_score = 0

    posts = page.posts
    for post in posts:
        positivity_score += getScoreFromMedia(post)
        if post is not None:
            comments = post.comments
            for comment in comments:
                positivity_score += getScoreFromMedia(comment)
    
    return positivity_score