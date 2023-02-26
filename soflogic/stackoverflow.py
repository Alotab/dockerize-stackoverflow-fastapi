import requests
import json


try:
    from urllib.parse import urlparse
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode


url = 'https://api.stackexchange.com/2.3/search?order=desc&sort=activity&tagged=rust&site=stackoverflow'


def search_tagged_questions(name):
    """Type any tagged name (python, java, rust, etc) and get all related question on stackoverflow"""

    url_parts = urlparse(url)
    query = f'order=desc&sort=activity&tagged={name}&site=stackoverflow'
    join_url = url_parts._replace(query=query).geturl()
    return join_url


def get_questions(name, answer=0):
    """Get links for any unanswered stackoverflow questions"""

    response = requests.get(search_tagged_questions(name))
    for data in response.json()['items']:
        if data['answer_count'] == answer:
            print(data['title'])
            print(data['link'], '\n')

        elif data['answer_count'] == answer & data['is_answered'] is True:
            print(data['title'])
            print(data['link'])
            print(f"Question is answered: {data['is_answered']}", '\n')
    return data
  