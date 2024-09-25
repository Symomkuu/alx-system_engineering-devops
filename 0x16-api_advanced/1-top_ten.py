#!/usr/bin/python3
"""A module that prints the top 10 hot posts for a subreddit"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the top 10
    hot posts for a given subreddit.
    
    Args:
        subreddit (str): The subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code != 200:
            print(None)
            return
        data = response.json().get("data", {})
        children = data.get("children", [])

        for i in range(min(10, len(children))):
            print(children[i]["data"]["title"])

        if len(children) == 0:
            print(None)

    except requests.RequestException:
        print(None)

