import requests
import json
page_id = "229568753577594"
user_access_token = "EAAfJUHChi8UBO0bxM2GZBWDrPSn1ExNzsBYvNXlJgW7PgnZC4jufJUjQ4M9ALZAU96H8bZAU6ZBHH6qwfUEJCIYR5XUFGtmnitevzLiws2ygzZCry75R7nsCtEYXEZAFvEvpPcMQ1D6wd5LDpvZBj9D6rkZAZB0Ll5Nl5Q0c3FuY20NnuDhsX8TOicKPB4"
page_access_token = "EAAfJUHChi8UBOwWmuuEc8AhOaRC1BNZAiQlZBRYufmv1Cj81kcj9ABAKmr71eDW33lEjkvH7Ai2WWbEmWF3vY73mKxtIcOrUUiaiKqGZB97SiOolMAV7im5HKEZADzwJfpZAXYQUmqJRgp1KBjaUFtmqRiHQZAj8QpjZBNJBOcS8edNo70uTNNCVjG4mURDDpYZD"

def getUser(user_access_token):
    url = f"https://graph.facebook.com/v19.0/me?fields=id,name&access_token={user_access_token}"
    
    response = requests.request("GET", url)
    
    data = json.loads(response.text)

    return data["id"]

def getPages(user_id):
    url = f"https://graph.facebook.com/v19.0/{user_id}/accounts?access_token={user_access_token}"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    pages = data["data"]
    for page in pages:
        page_id = page["id"]
        return page_id

    
def getPostsFromPage(page_id):
    
    url = f"https://graph.facebook.com/v19.0/{page_id}/feed?access_token={page_access_token}"

    response = requests.request("GET", url)

    data = json.loads(response.text)

    posts = data['data']
    for post in posts:
        post_id = post['id']
        getCommentsFromPost(page_id)
        

def getCommentsFromPost(post_id):
    
    url = f"https://graph.facebook.com/v19.0/{post_id}/comments?access_token={page_id}"

    response = requests.request("GET", url);

    data = json.loads(response.text)
    print(response.text)

    comments = data['data']
    for comment in comments:
        message = comment["message"]
        print(message)

user_id = getUser(user_access_token)
getPages(user_id)
