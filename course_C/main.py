import requests

api_key = "7b0a6d7450aa4fa9b8af0632a4e1b827"
url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2025-04-23&sortBy=publishedAt&"\
    "apiKey=7b0a6d7450aa4fa9b8af0632a4e1b827"

request = requests.get(url)
#content = request.text
#print(type(content)) # provides string

content_json = request.json() # provides json as dict
print(type(content_json))

for article in content_json["articles"]:
    if article["title"].find("Trump") >= 0:
        print(article["title"])