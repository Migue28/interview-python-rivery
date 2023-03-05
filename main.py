import requests
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
import rivery_cli


def get_news_data(api_key):
    """
    Connects to the NewsAPI.org news API and returns the most popular news from the previous day.

    :param api_key: The API key to use for the NewsAPI.org API.
    :return: A list of dictionaries containing the most popular news from the previous day.
    """
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    url = f"https://newsapi.org/v2/everything?q=*&sortBy=popularity&from={yesterday}"
    headers = {"Authorization": "Bearer " + api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def insert_news(news, connection):
    """
    Inserts the given news articles into the specified MySQL database.

    :param news: A list of dictionaries containing news articles.
    :param connection: The connection to the MySQL database.
    """


load_dotenv()
api_key = os.environ.get("NEWS_API_KEY")

if __name__ == '__main__':
    api_key = api_key
    get_news_data(api_key)
