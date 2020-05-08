
#!/usr/bin/python3
"""# subs of subreddit"""
import requests
import sys


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot posts"""
    try:
        head = {"User-Agent": "Sergioq7777"}
        redit_req = requests.get(
            'https://api.reddit.com/r/{}/hot?sort=hot&limit=10'.format(
                subreddit), headers=head)
        if redit_req.status_code == 404:
            print(None)
            return
        info = redit_req.json()
        num_hot = info['data']['children']
        for out in num_hot:
            print(out['data']['title'])
    except:
        print()
