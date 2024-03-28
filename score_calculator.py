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

def getScoreFromMessages(messages):

    scores = []
    for message in messages:
        score = ai.getAiScore(message)
        try:
            score = int(score)
            scores.append(score)
        except ValueError:
            scores.append(0)
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

def page_init(page):

    rd.getPagePhoto(page)

    page_posts = rd.getPostsFromPage(page)
    posts = []
    for i in range(0 , len(page_posts)):
        post = page_posts[i]
        try:
            posts.append(mo.Post(post['id'], post['message']))
        except KeyError:
            continue

    for post in posts:
        post_comments = rd.getCommentsFromPost(post)
        comments = []
        for i in range(0, len(post_comments)):
            comment = post_comments[i]
            comments.append(mo.Comment(comment['id'], comment['message']))
        
        post.comments = comments
        for comment in post.comments:
            post.comments.reaction = rd.getReactions(comment)
        
            
        post.reactions = rd.getReactions(post)
