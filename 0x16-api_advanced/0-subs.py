#!/usr/bin/python3
"""
Module to query the number of subscribers of a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers. Returns 0 if an error occurs
        or the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # Send GET request to Reddit API with no redirects allowed
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the response is OK (status code 200), get the subscriber count
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        
        # If subreddit is invalid or other issues arise, return 0
        return 0
    
    except Exception:
        return 0

