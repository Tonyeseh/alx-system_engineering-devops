#!/usr/bin/python3
"""Query subscribers on a given reddit subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-agent": "alx_advanced_api"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get('data')
    return results.get('subscribers')
