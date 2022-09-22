#!/usr/bin/python3
""""Write a recursive function that queries the
Reddit API and returns a list containing the titles
of all hot articles for a given subreddit."""

from requests import request


def recurse(subreddit, hot_list=[], after=""):
    """returns a list containing the titles of all
    hot articles for a given subreddit. No result
    found, the function should return None"""
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        current = response['data']['children']
        next = response['data']['after']
        for item in current:
            hot_list.append(item['data']['title'])
        if next is not None:
            recurse(subreddit, hot_list, next)
        return hot_list
    except Exception:
        return None
