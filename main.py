import media_objects as mo
import read_data as rd
import ai 
import ui


def main():

    user = rd.getUser()
    page = mo.Page(rd.PAGE_ID, user) 

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
        post.comments = rd.getCommentsFromPost(post)
        post.reactions = rd.getReactions(post)
    

main()
