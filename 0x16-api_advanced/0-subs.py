#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit"""

from requests import request


def number_of_subscribers(subreddit):
    """function thar queries the Reddit API and returns the number
    of suscribers"""
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        subscribers = response['data']['subscribers']
        return subscribers
    except Exception:
        return 0
