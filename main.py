import media_objects as mo
import read_data as rd
import ai 


def main():

    user = rd.getUser()
    page = mo.Page(rd.PAGE_ID, user) 

    page_posts = rd.getPostsFromPage(page)
    posts = []
    for i in range(0 , len(page_posts)):
        post = page_posts[i]
        posts.append(mo.Post(post['id'], post['message']))
        posts[i].comments = (rd.getCommentsFromPost(posts[i]))
        posts[i].reactions = (rd.getReactions(posts[i]))

    print(ai.getScoreFromMessages(posts[0].comments))

main()
