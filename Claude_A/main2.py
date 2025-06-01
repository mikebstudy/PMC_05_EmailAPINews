import requests
from datetime import datetime
import json

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



def get_todays_articles():
    """Fetch and display today's articles from NewsAPI"""

    # API configuration
    api_key = "7b0a6d7450aa4fa9b8af0632a4e1b827"
    base_url = "https://newsapi.org/v2/everything"

    # Get today's date in YYYY-MM-DD format
    today = datetime.now().strftime("%Y-%m-%d")

    # Parameters for the API request
    # NewsAPI requires at least one of: q, qInTitle, sources, domains
    params = {
        'apiKey': api_key,
        'from': today,
        'to': today,
        'q': '*',  # Search for all articles (wildcard)
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


def get_articles_by_sources():
    """Get today's articles from popular sources"""

    api_key = "7b0a6d7450aa4fa9b8af0632a4e1b827"
    base_url = "https://newsapi.org/v2/everything"

    # Popular news sources (you can modify this list)
    sources = "bbc-news,cnn,reuters,associated-press,the-wall-street-journal,abc-news"
    today = datetime.now().strftime("%Y-%m-%d")

    params = {
        'apiKey': api_key,
        'sources': sources,
        'from': today,
        'to': today,
        'sortBy': 'publishedAt',
        'pageSize': 100
    }

    try:
        print(f"\nFetching articles from popular sources for {today}...")
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        if data['status'] == 'ok':
            articles = data['articles']
            print(f"\nFound {len(articles)} articles from popular sources")
            print("=" * 80)

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

    except Exception as e:
        print(f"Error fetching articles by sources: {e}")


def get_articles_by_keyword(keyword="news"):
    """Get today's articles by keyword search"""

    api_key = "7b0a6d7450aa4fa9b8af0632a4e1b827"
    base_url = "https://newsapi.org/v2/everything"
    today = datetime.now().strftime("%Y-%m-%d")

    params = {
        'apiKey': api_key,
        'q': keyword,
        'from': today,
        'to': today,
        'sortBy': 'publishedAt',
        'language': 'en',
        'pageSize': 50
    }

    try:
        print(f"\nFetching articles with keyword '{keyword}' for {today}...")
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        if data['status'] == 'ok':
            articles = data['articles']
            print(f"\nFound {len(articles)} articles with keyword '{keyword}'")
            print("=" * 80)

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

    except Exception as e:
        print(f"Error fetching articles by keyword: {e}")
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
    print("NewsAPI Today's Articles")
    print("=" * 50)

    # Method 1: Top headlines (most reliable)
    get_top_headlines_today()

    # Method 2: Articles from popular sources
    print("\n" + "=" * 80)
    #get_articles_by_sources()

    # Method 3: General search with wildcard (may be limited)
    print("\n" + "=" * 80)
    #get_todays_articles()

    # Method 4: Search by keyword (optional - uncomment to use)
    print("\n" + "="*80)
    #get_articles_by_keyword("technology")  # Change keyword as needed