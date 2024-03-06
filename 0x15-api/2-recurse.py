#!/usr/bin/python3
"""
A script that queries the Reddit API and returns a list.
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    A method that queries tge Reddit API.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'zeusgolohor360'}

    pms = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=pms)
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data['data']['children']

    for post in posts:
        hot_list.append(post['data']['title'])
    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list

