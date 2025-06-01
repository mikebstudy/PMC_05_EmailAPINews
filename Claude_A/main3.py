import requests
from datetime import datetime
import json
import smtplib
import ssl
import os
from dotenv import load_dotenv


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "mikebstudy@gmail.com"

    load_dotenv(override=True)
    password = os.getenv("PMC_02_SHOWCASE_PW")

    context = ssl.create_default_context()

    receiver = "mikebstudy@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def format_articles_for_email(articles, title="Articles"):
    """Format articles into a readable email format"""
    if not articles:
        return f"\n{title}: No articles found.\n"

    content = f"\n{title} ({len(articles)} articles):\n"
    content += "=" * 80 + "\n"

    for i, article in enumerate(articles, 1):
        content += f"\n--- Article {i} ---\n"
        content += f"Title: {article.get('title', 'N/A')}\n"
        content += f"Description: {article.get('description', 'N/A')}\n"
        content += f"URL: {article.get('url', 'N/A')}\n"
        content += f"Author: {article.get('author', 'N/A')}\n"
        content += f"Source: {article.get('source', {}).get('name', 'N/A')}\n"
        content += f"Published: {article.get('publishedAt', 'N/A')}\n"
        content += "-" * 40 + "\n"

    return content


def get_todays_articles():
    """Fetch today's articles from NewsAPI"""

    api_key = "7b0a6d7450aa4fa9b8af0632a4e1b827"
    base_url = "https://newsapi.org/v2/everything"

    today = datetime.now().strftime("%Y-%m-%d")

    params = {
        'apiKey': api_key,
        'from': today,
        'to': today,
        'q': '*',  # Search for all articles (wildcard)
        'sortBy': 'publishedAt',
        'language': 'en',
        'pageSize': 100
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        if data['status'] == 'ok':
            return data['articles'], None
        else:
            return [], f"Error: {data.get('message', 'Unknown error occurred')}"

    except Exception as e:
        return [], f"Error fetching general articles: {str(e)}"


def get_articles_by_sources():
    """Get today's articles from popular sources"""

    api_key = "7b0a6d7450aa4fa9b8af0632a4e1b827"
    base_url = "https://newsapi.org/v2/everything"

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
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        if data['status'] == 'ok':
            return data['articles'], None
        else:
            return [], f"Error: {data.get('message', 'Unknown error occurred')}"

    except Exception as e:
        return [], f"Error fetching articles by sources: {str(e)}"


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
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        if data['status'] == 'ok':
            return data['articles'], None
        else:
            return [], f"Error: {data.get('message', 'Unknown error occurred')}"

    except Exception as e:
        return [], f"Error fetching articles by keyword: {str(e)}"


def get_top_headlines_today():
    """Get top headlines for today"""

    api_key = "7b0a6d7450aa4fa9b8af0632a4e1b827"
    base_url = "https://newsapi.org/v2/top-headlines"

    params = {
        'apiKey': api_key,
        'country': 'us',
        'pageSize': 50
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        if data['status'] == 'ok':
            return data['articles'], None
        else:
            return [], f"Error: {data.get('message', 'Unknown error occurred')}"

    except Exception as e:
        return [], f"Error fetching top headlines: {str(e)}"


def create_email_message(email_content):
    """Create properly formatted email message with headers"""
    today = datetime.now().strftime("%Y-%m-%d")

    subject = f"Daily News Summary - {today}"

    message = f"""Subject: {subject}
From: mikebstudy@gmail.com
To: mikebstudy@gmail.com
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8

Daily News Summary for {today}
{email_content}

---
Generated automatically by NewsAPI Daily Summary
"""
    return message


def main():
    """Main function to collect all articles and send via email"""
    today = datetime.now().strftime("%Y-%m-%d")
    email_content = f"NewsAPI Daily Summary for {today}\n"
    email_content += "=" * 50 + "\n"

    errors = []

    # Method 1: Top headlines (most reliable)
    print("Fetching top headlines...")
    headlines, error = get_top_headlines_today()
    if error:
        errors.append(f"Top Headlines: {error}")
    email_content += format_articles_for_email(headlines, "Top Headlines")

    # Method 2: Articles from popular sources
    print("Fetching articles from popular sources...")
    source_articles, error = get_articles_by_sources()
    if error:
        errors.append(f"Popular Sources: {error}")
    email_content += format_articles_for_email(source_articles, "Articles from Popular Sources")

    # Method 3: General search with wildcard
    print("Fetching general articles...")
    general_articles, error = get_todays_articles()
    if error:
        errors.append(f"General Articles: {error}")
    email_content += format_articles_for_email(general_articles, "General Articles")

    # Method 4: Technology articles (example keyword search)
    print("Fetching technology articles...")
    tech_articles, error = get_articles_by_keyword("technology")
    if error:
        errors.append(f"Technology Articles: {error}")
    email_content += format_articles_for_email(tech_articles, "Technology Articles")

    # Add errors to email if any occurred
    if errors:
        email_content += "\nErrors encountered:\n"
        email_content += "=" * 30 + "\n"
        for error in errors:
            email_content += f"- {error}\n"

    # Create and send email
    try:
        print("Preparing email...")
        email_message = create_email_message(email_content)
        email_message = email_message.encode("utf-8")

        print("Sending email...")
        send_email(email_message)
        print(f"✅ Daily news summary sent successfully to mikebstudy@gmail.com")

        # Print summary statistics
        total_headlines = len(headlines) if headlines else 0
        total_sources = len(source_articles) if source_articles else 0
        total_general = len(general_articles) if general_articles else 0
        total_tech = len(tech_articles) if tech_articles else 0

        print(f"\nSummary:")
        print(f"- Top Headlines: {total_headlines} articles")
        print(f"- Popular Sources: {total_sources} articles")
        print(f"- General Articles: {total_general} articles")
        print(f"- Technology Articles: {total_tech} articles")
        print(f"- Total Articles: {total_headlines + total_sources + total_general + total_tech}")

    except Exception as e:
        print(f"❌ Failed to send email: {str(e)}")


if __name__ == "__main__":
    main()