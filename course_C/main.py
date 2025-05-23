import requests
from send_email import send_email

api_key = "7b0a6d7450aa4fa9b8af0632a4e1b827"
url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2025-04-23&sortBy=publishedAt&"\
    "apiKey=7b0a6d7450aa4fa9b8af0632a4e1b827"

request = requests.get(url)
#content = request.text
#print(type(content)) # provides string

content_json = request.json() # provides json as dict
# print(type(content_json))

message = []

for article in content_json["articles"]:
    if article["title"].find("Trump") >= 0:
        # print(article["title"])
        message.append(article["title"]+"\n")
        # print("- " + article["description"])
        message.append("- " + article["description"]+2*"\n")

message_out = "".join(message).encode("utf-8")
send_email(message_out)
