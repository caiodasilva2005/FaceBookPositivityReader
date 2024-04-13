import read_data as rd
import media_objects as mo
import ai 

MAX_SCORE = 1000 # max positivity score

# reaction weights
LOVE_SCORE = 10 
LIKE_SCORE = 5
WOW_SCORE = 2
HAHA_SCORE = 1
SAD_SCORE = -2
ANGRY_SCORE = -5

__all_comments__ = {} # stores every comment with its pos score
__all_posts__ = {} # stores every post message with its pos score
__all_reactions__ = {"love": 0, "like": 0, "wow": 0, "haha": 0, "sad": 0, "angry": 0} # stores all reactions

#places message into ai to receive score from a Post or Comment message
def getScoreFromMessage(message):
    
    score = ai.getAiScore(message)
    try:
        score = int(score)
    except ValueError:
        score = 0
    
    return score

#gets score from the reactions from a Post or Comment object
def getScoreFromReactions(reactions):

    score = 0
    
    score += reactions['love'] * LOVE_SCORE
    __all_reactions__['love'] += reactions['love']
    
    score += reactions['like'] * LIKE_SCORE
    __all_reactions__['like'] += reactions['like']

    score += reactions['wow'] * WOW_SCORE
    __all_reactions__['wow'] += reactions['wow']

    score += reactions['haha'] * HAHA_SCORE
    __all_reactions__['haha'] += reactions['haha']

    score += reactions['sad'] * SAD_SCORE
    __all_reactions__['sad'] += reactions['sad']

    score += reactions['angry'] * ANGRY_SCORE 
    __all_reactions__['angry'] += reactions['angry']

    return score

# gets the total scofre form a Post or Comment Object
def getScoreFromMedia(object):
    score = 0

    score += getScoreFromMessage(object.message)
    score += getScoreFromReactions(object.reactions)

    return score

# Gets total accumulated score from all media objects in page
def getPagePositivityScore(page):
    positivity_score = 0

    posts = page.posts
    for post in posts:
        if post is not None:
            post_score = getScoreFromMedia(post)
            positivity_score += positivity_score
            __all_posts__.update({post.message: post_score})
            comments = post.comments
            for comment in comments:
                comment_score = getScoreFromMedia(comment)
                positivity_score += comment_score
                __all_comments__.update({comment.message: comment_score})
    
    # averages the pos score based on the number of media objects on the page
    positivity_score /= (len(__all_posts__) + len(__all_comments__)) 
    positivity_score = round(positivity_score, 2)    
    if (positivity_score > MAX_SCORE): # pos score does not exceed max score
        positivity_score = MAX_SCORE
        
    return positivity_score

# finds the most postive media object message from a dictionary
def getMostPositiveMedia(object):
    maxMessage  = ""
    maxScore = 0
    for message, score in object.items():
        if score > maxScore:
            maxScore = score
            maxMessage = message
    
    return maxMessage

    