# FaceBook Positivity Reader

This project will fetch data from a FaceBook Page and use its information to determine
how positive the page is. The information considered are messages, comments, and reactions.
A trained OpenAI Python API performs a sentiment anaylsis on the comments and messages
to assign them a positivity score.

A GUI displays the page photo, page name, overall positivity score, the most positive post,
the most positive comment, and the total reactions of the page.

## General Usage

To start the program, run **main.py**. The UI should appear with the page name and photo. Click the button at the bottom of the UI to receive the positivity data of the page.

## Libraries

```
requests
json
openai
tkinter
Pillow
FaceBook Graph API
```

### OpenAI

#### Installation

```bash
pip install openai
```

#### Usage

An API Key is required to use **ChatGPT 3.5** (the current version we are using for the program). To generate a key, go this [link](https://platform.openai.com/api-keys) and click API Keys. Then create a new secret key. Deposit a desired balance into an openai account to receive ai-generated responses.

### FaceBook Graph API

To fetch data using [FaceBook Graph API](https://developers.facebook.com/docs/graph-api/), the user must generate an **access token** using the [Graph API Explorer](https://developers.facebook.com/tools/explorer/). To receive a positivity rating from your desired page, generate a **User Access Token** and **Page Access Token** with the following permissions:

```
pages_show_list
pages_read_engagement
pages_read_user_content
pages_manage_posts
pages_manage_engagement
```

## Authors

[Caio DaSilva](https://www.linkedin.com/in/caio-dasilva-1018b228b/)
<br>
[Jack Sweeney](https://www.linkedin.com/in/jack-sweeney-5145002a3/)
