import requests
from datetime import datetime
import json

def get_todays_articles():
    """Fetch and display today's articles from NewsAPI"""

    # API configuration
    api_key = "7b0a6d7450aa4fa9b8af0632a4e1b827"
    base_url = "https://newsapi.org/v2/everything"

    # Get today's date in YYYY-MM-DD format
    today = datetime.now().strftime("%Y-%m-%d")

    # Parameters for the API request
    params = {
        'apiKey': api_key,
        'from': today,
        'to': today,
        'sortBy': 'publishedAt',
        'language': 'en',
        'pageSize': 100  # Maximum articles per request
    }

    try:
        # Make API request
        print(f"Fetching articles for {today}...")
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse JSON response
        data = response.json()

        if data['status'] == 'ok':
            articles = data['articles']
            total_results = data['totalResults']

            print(f"\nFound {total_results} articles for today ({len(articles)} displayed)")
            print("=" * 80)

            # Display each article
            for i, article in enumerate(articles, 1):
                print(f"\n--- Article {i} ---")
                print(f"Title: {article.get('title', 'N/A')}")
                print(f"Description: {article.get('description', 'N/A')}")
                print(f"URL: {article.get('url', 'N/A')}")
                print(f"Author: {article.get('author', 'N/A')}")
                print(f"Source: {article.get('source', {}).get('name', 'N/A')}")
                print(f"Published: {article.get('publishedAt', 'N/A')}")
                print("-" * 40)
        else:
            print(f"Error: {data.get('message', 'Unknown error occurred')}")

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
    except KeyError as e:
        print(f"Unexpected response format: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def get_top_headlines_today():
    """Alternative function to get top headlines for today"""

    api_key = "7b0a6d7450aa4fa9b8af0632a4e1b827"
    base_url = "https://newsapi.org/v2/top-headlines"

    params = {
        'apiKey': api_key,
        'country': 'us',  # You can change this to other country codes
        'pageSize': 50
    }

    try:
        print("\nFetching today's top headlines...")
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        if data['status'] == 'ok':
            articles = data['articles']
            print(f"\nTop Headlines ({len(articles)} articles)")
            print("=" * 80)

            for i, article in enumerate(articles, 1):
                print(f"\n--- Headline {i} ---")
                print(f"Title: {article.get('title', 'N/A')}")
                print(f"Description: {article.get('description', 'N/A')}")
                print(f"URL: {article.get('url', 'N/A')}")
                print(f"Author: {article.get('author', 'N/A')}")
                print(f"Source: {article.get('source', {}).get('name', 'N/A')}")
                print(f"Published: {article.get('publishedAt', 'N/A')}")
                print("-" * 40)
        else:
            print(f"Error: {data.get('message', 'Unknown error occurred')}")

    except Exception as e:
        print(f"Error fetching top headlines: {e}")


if __name__ == "__main__":
    # Get today's articles
    get_todays_articles()

    # Optionally, also get top headlines
    print("\n" + "=" * 80)
    get_top_headlines_today()