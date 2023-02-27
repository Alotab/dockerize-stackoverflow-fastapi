import requests
from urllib.parse import urlparse

tagged_api = "https://api.stackexchange.com/2.3/search?order=desc&sort=activity&tagged=rust&site=stackoverflow"
users_api = "https://api.stackexchange.com/2.3/users?order=desc&sort=reputation&site=stackoverflow"


def search_tagged_questions(tagged):
    """Type any tagged name (python, java, rust, etc) and get all related question on stackoverflow"""

    url_parts = urlparse(tagged_api)
    query = f"order=desc&sort=activity&tagged={tagged}&site=stackoverflow"
    join_url = url_parts._replace(query=query).geturl()
    return join_url


def get_questions(tagged):
    """Get links for any stackoverflow questions by their tagged name (python, java, rust, etc)"""

    data = None
    response = requests.get(search_tagged_questions(tagged), timeout=5)
    for data in response.json()["items"]:
        if data["is_answered"] is True:
            print(data["title"])
            print(data["link"])
            print(f"Question is answered: {data['is_answered']}", "\n")

        elif data["is_answered"] is False:
            print(data["title"])
            print(data["link"])
            print(f"Question is answered: {data['is_answered']}", "\n")
    return data


def search_users(name):
    """ "Fetech all users on StackOverFlow by first/last name"""

    url_parts = urlparse(users_api)
    query = f"order=desc&sort=reputation&inname={name}&site=stackoverflow"
    join_url = url_parts._replace(query=query).geturl()
    return join_url


def fetch_users(name):
    """Fetch all users from StackOverflow by their first/last names"""

    data = None
    response = requests.get(search_users(name), timeout=5)
    for data in response.json()["items"]:
        if data["display_name"] == name:
            print(f"Username: {data['display_name']}")
            print(f"Badge Count: {data['badge_counts']}")
            print(f"website links: {data['link']}", "\n")
        else:
            print(f"Username: {data['display_name']}")
            print(f"Badge Count: {data['badge_counts']}")
            print(f"website links: {data['link']}", "\n")
    return data
