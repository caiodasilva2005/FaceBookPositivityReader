import requests
import json
import openai

page_id = "229568753577594"
user_access_token = "EAAfJUHChi8UBO0bxM2GZBWDrPSn1ExNzsBYvNXlJgW7PgnZC4jufJUjQ4M9ALZAU96H8bZAU6ZBHH6qwfUEJCIYR5XUFGtmnitevzLiws2ygzZCry75R7nsCtEYXEZAFvEvpPcMQ1D6wd5LDpvZBj9D6rkZAZB0Ll5Nl5Q0c3FuY20NnuDhsX8TOicKPB4"
page_access_token = "EAAfJUHChi8UBO3smPYYVp3k4aI1nln7NcxtDYDZAacANtE0bQu2ua8eai8GI3jZCmNBVHIFfJ7zULGAIPgK04vmKgzwX527fsohoOWLZBVjhl2VHNsnY8ChZCvIq3FxV2vfqw8eK5bmjviTQM2rGAm0ycXT1EuCCDJ6ccNaKhK0PnPZAQhHrjooLZCWFoUcA0ZD"
key="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"

openai.api_key = key

def ChatAI(comment):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Rate this message on a scale of 1 to 10 on how positive it is: {}".format(comment)}
        ],
        max_tokens = 50)
    
    #print(chat_completion.choices[0].message["content"])
    return chat_completion.choices[0].message["content"]
    

    

def getUser(user_access_token):
    url = f"https://graph.facebook.com/v19.0/me?fields=id,name&access_token={user_access_token}"
    
    response = requests.request("GET", url)
    
    data = json.loads(response.text)

    return data["id"]

#def getPages(user_id):
#    url = f"https://graph.facebook.com/v19.0/{user_id}/accounts?access_token={user_access_token}"
#    response = requests.request("GET", url)
#    data = json.loads(response.text)
#    pages = data["data"]
#    for page in pages:
#        page_id = page["id"]
#        return page_id

    
def getPostsFromPage(page_id):
    
    url = f"https://graph.facebook.com/v19.0/{page_id}/feed?access_token={page_access_token}"

    response = requests.request("GET", url)

    data = json.loads(response.text)

    posts = data['data']
    for post in posts:
        post_id = post['id']
        getCommentsFromPost(post_id)
        

def getCommentsFromPost(post_id):
    
    url = f"https://graph.facebook.com/v19.0/{post_id}/comments?access_token={page_access_token}"

    response = requests.request("GET", url);

    data = json.loads(response.text)

    comments = data['data']
    for comment in comments:
        message = comment["message"]
        print("Message:", message, "\nResponse:", ChatAI(message))
        

getPostsFromPage(page_id)