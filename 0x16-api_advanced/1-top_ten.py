#!/usr/bin/python3
"""
A script that queries the Reddit API and returns the number of subscribers
"""
import requests


def top_ten(subreddit):
    """
    A method  that queries the Reddit API
    and returns the number of subscribers.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    set_headers = {"User-Agent": "My User Agent 1.0"}
    params = {
        "limit": 10
    }

    """
    making the request.
    """
    res = requests.get(url, headers=set_headers, params=params,
                       allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        data = data.get("data")
        [print(req.get("data")
               .get("title")) for req in results.get("children")]

    else:
        print("None")
        return
