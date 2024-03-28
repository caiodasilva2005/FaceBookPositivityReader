import requests
import json
import io

PAGE_ID = "229568753577594"
USER_TOKEN = "EAAfJUHChi8UBO0bxM2GZBWDrPSn1ExNzsBYvNXlJgW7PgnZC4jufJUjQ4M9ALZAU96H8bZAU6ZBHH6qwfUEJCIYR5XUFGtmnitevzLiws2ygzZCry75R7nsCtEYXEZAFvEvpPcMQ1D6wd5LDpvZBj9D6rkZAZB0Ll5Nl5Q0c3FuY20NnuDhsX8TOicKPB4"
PAGE_TOKEN = "EAAfJUHChi8UBO3smPYYVp3k4aI1nln7NcxtDYDZAacANtE0bQu2ua8eai8GI3jZCmNBVHIFfJ7zULGAIPgK04vmKgzwX527fsohoOWLZBVjhl2VHNsnY8ChZCvIq3FxV2vfqw8eK5bmjviTQM2rGAm0ycXT1EuCCDJ6ccNaKhK0PnPZAQhHrjooLZCWFoUcA0ZD"

def getUser():
    
    url = f"https://graph.facebook.com/v19.0/me?fields=id,name&access_token={USER_TOKEN}"
    
    response = requests.request("GET", url)
    
    data = json.loads(response.text)

    return data["id"]

    
def getPostsFromPage(page):
    
    url = f"https://graph.facebook.com/v19.0/{page.id}/feed?access_token={PAGE_TOKEN}"

    response = requests.request("GET", url)

    data = json.loads(response.text)

    posts = data['data']
    
    return posts
        

def getCommentsFromPost(post):
    
    url = f"https://graph.facebook.com/v19.0/{post.id}/comments?access_token={PAGE_TOKEN}"

    response = requests.request("GET", url);

    data = json.loads(response.text)

    comment_data = data['data']
    comments = []
    for comment in comment_data:
        comments.append(comment['message'])

    return comments

def getReactions(object):

    url_love = f"https://graph.facebook.com/{object.id}?fields=reactions.type(LOVE).limit(0).summary(total_count)&access_token={PAGE_TOKEN}"
    url_like = f"https://graph.facebook.com/{object.id}?fields=reactions.type(LIKE).limit(0).summary(total_count)&access_token={PAGE_TOKEN}"
    url_wow = f"https://graph.facebook.com/{object.id}?fields=reactions.type(WOW).limit(0).summary(total_count)&access_token={PAGE_TOKEN}"
    url_haha = f"https://graph.facebook.com/{object.id}?fields=reactions.type(HAHA).limit(0).summary(total_count)&access_token={PAGE_TOKEN}"
    url_haha = f"https://graph.facebook.com/{object.id}?fields=reactions.type(SAD).limit(0).summary(total_count)&access_token={PAGE_TOKEN}"
    url_angry = f"https://graph.facebook.com/{object.id}?fields=reactions.type(ANGRY).limit(0).summary(total_count)&access_token={PAGE_TOKEN}"

    urls = [url_love, url_like, url_wow, url_haha, url_angry]
    reaction_dict = {"love": 0, "like": 0, "wow": 0, "haha": 0, "sad": 0, "angry": 0}

    for url in urls:
        response = requests.request("GET", url);
        data = json.loads(response.text)
        count = data['reactions']['summary']['total_count']

        if "LOVE" in url:
            reaction_dict["love"] = count
        elif "LIKE" in url:
            reaction_dict["like"] = count
        elif "WOW" in url:
            reaction_dict["wow"] = count
        elif "HAHA" in url:
            reaction_dict["haha"] = count
        elif "SAD" in url:
            reaction_dict["sad"] = count
        elif "ANGRY" in url:
            reaction_dict["angry"] = count
    
    return reaction_dict

def getPagePhoto(page):

    page_photo_url = f"https://graph.facebook.com/v19.0/{page.id}/photos?access_token={PAGE_TOKEN}"  

    response = requests.request("GET", page_photo_url);

    page_photo_data = json.loads(response.text)
    photo_id = page_photo_data['data'][0]['id']

    photo_url = f"https://graph.facebook.com/v19.0/{photo_id}/picture?access_token={PAGE_TOKEN}"
    response = requests.request("GET", photo_url);

    with open('./photos/photo.jpg', 'wb') as f:
        f.write(response.content)


