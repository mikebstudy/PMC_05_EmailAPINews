import requests
from send_email import send_email

topic = "tesla"
from_date = "2025-05-30"
api_key = "7b0a6d7450aa4fa9b8af0632a4e1b827"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    f"from={from_date}&" \
    "sortBy=publishedAt&" \
    "language=en&" \
    f"apiKey={api_key}"


request = requests.get(url)
#content = request.text
#print(type(content)) # provides string

content_json = request.json() # provides json as dict
# print(type(content_json))

message = []
message.append("Subject: Today's news\n")

for article in content_json["articles"]:
    #if article["title"].find("Trump") >= 0:
    if "Trump" in article["title"]:
        # print(article["title"])
        message.append(article["title"]+"\n")
        # print("- " + article["description"])
        message.append("- " + article["description"]+"\n")
        # print("- " + article["url"])
        message.append("- " + article["url"]+2*"\n")

message_out = "".join(message).encode("utf-8")
send_email(message_out)
