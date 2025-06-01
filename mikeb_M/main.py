import requests
from datetime import datetime, timedelta
from send_email import send_email
from collections import Counter

topic = "trump"
from_date = (datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d")
#from_date = datetime.now().strftime("%Y-%m-%d")
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

subject_line = f"Subject: Today's news ({from_date})\n\n"

message = [subject_line]
title_filter = ""
article_count_limit = 100
publishers = []
article_count = 0
for article in content_json["articles"]:
    if not title_filter or (title_filter and title_filter in article["title"]):
         article_count += 1
         if article_count > article_count_limit:
             break
         print(article["title"])
         message.append(article["title"]+"\n")
         if desc := article["description"]:
            #print("--- " + desc)
            message.append("--- " + desc+"\n")
         if url := article["url"]:
            #print("URL: " + url)
            message.append("URL: " + url+"\n")
         if author := article["author"]:
            #print("BY: " + author)
            message.append("BY: " + author+"\n")
         if source := article["source"]["name"]:
            #print("SRC: " + source)
            message.append("SRC: " + source+"\n")
            publishers.append(source)
         if published_at := article["publishedAt"]:
            #print(" AT: " + published_at)
            message.append(" AT: " + published_at+"\n")
         content = article["content"]
         if content and desc and content[0:len(desc)] != desc:
             #print(">>> " + content)
             message.append(">>> " + content+"\n")
         #print("\n")
         message.append("\n")

counter = Counter(publishers)
print(counter)
print(article_count)
message.append("\n")
message.append(str(counter)+'\n')
message.append(str(article_count)+"\n")
message_out = "".join(message).encode("utf-8")
send_email(message_out)
