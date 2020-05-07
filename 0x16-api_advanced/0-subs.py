#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers """
import requests
import sys


def number_of_subscribers(subreddit):
    """Return the number og subcribers"""
    try:
        head = {"User-Agent": "sergioq7777"}
        redit_req = requests.get(
            'https://api.reddit.com/r/{}/about'.format(subreddit),
            headers=head)
        if redit_req.status_code == 404:
            return 0
        info = redit_req.json()
        num_subs = info['data']['subscribers']
        return num_subs
    except:
        return 
