#!/usr/bin/python3
"""A module to query subscribers on Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid
        or if an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code != 200:
            return 0
        try:
            results = response.json().get("data")
        except ValueError:
            return 0

        if results:
            return results.get("subscribers", 0)

        return 0

    except requests.RequestException:
        return 0

