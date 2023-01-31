#!/usr/bin/python3
"""
Queries the reddit api and prints the titles of the
first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit
        Args:
            subreddit(string): subreddit name
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "alx_advanced api"
    }
    params = {
        "limit": 10
    }
    response = requests.get(
        url, headers=headers, params=params,
        allow_redirects=False
    )
    if response.status_code == 404:
        print("None")
        return
    res = response.json().get('data').get('children')

    for children in res:
        print(children.get('data').get('title'))
