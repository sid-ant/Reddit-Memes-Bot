'''
journey to meme-lord is hard and disappointing, the hardest choice require the strongest wills 
'''

import requests,logging

def get_access_token():
    return null

def get_rising(limit):
    url = "https://oauth.reddit.com/r/memes/rising" # make it configurable later
    payload = {'limit':limit}
    bearer_token = "134025097543-kj4-JBtqY2Ln5mVEGXD1MFlEtzM" # get this from config 
    headers = {'Authorization': "Bearer "+bearer_token,'User-Agent':'python:com.siddhantcurious.Sprintrest:v0.0.1 (by /u/ancientspell'}
    try:
        response = requests.get(url,params=payload,headers=headers)
        print(response.url)
        print(response.headers)
    except HTTPError as httpe:
        logging.error("http errorr ",httpe)
        exit(1)
    except RequestException as e:
        logging.error("request exception ",e)
        exit(1)
    # print(response.text)
    body = response.json()
    print(body)
    return None
    
def main():
    limit = 5  
    images_urls = get_rising(limit=5)

main()