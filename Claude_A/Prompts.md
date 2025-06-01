# Prompts

### Claude Sonnet 4 


### First try
- Using python and the newsapi.org api, generate a program that will list all the articles for today.
  - Use the apiKey=7b0a6d7450aa4fa9b8af0632a4e1b827
  - Show the title, description, url, author and name of the source
- Generated code for everything and top-headlines endpoints
  - Endpoint everything failed - 400 error
    - Had to debug to determine error
      - '{"status":"error","code":"parametersMissing","message":"Required parameters are missing, the scope of your search is too broad. Please set any of the following required parameters and try again: q, qInTitle, sources, domains."}'
  - Endpoint top-headlines succeeded

- Error for everything endpoint: '{"status":"error","code":"parametersMissing","message":"Required parameters are missing, the scope of your search is too broad. Please set any of the following required parameters and try again: q, qInTitle, sources, domains."}'
- New code generated and put in main2.py
  - Missing some code from the origial, so it crashed
    - When call was commented out, it worked
    - Put in logic that was missing from first version
  - Then everything ran fine
    - Also tried the commented out technology section call
    - It also ran fine

### Second follow-up

- Instead of printing the output, collect it and send it in an email using the following code: import smtplib, ssl
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

- almost worked. needed encoding('utf-8') to work

- How did you arrive at the popular sources list? Where did you get the sources? How did you decide on the sources you included?
- Claude responded with:
  - You caught an important detail! I made assumptions about those source names without actually verifying them. Let me search for the actual available sources in NewsAPI to give you accurate information.
  - It updated the code with info it retrieved from sources somehow
    - The list just begins in alphabetical order, and stops at 10.

### Conclusions
- Claude worked very well
- Code used structures I was not familiar with, but they are better than course and mikeb coding
- It worked well to try first to just print and then do the email part
- I also liked how it fixed the code it had trouble with
- I make one little fix that I knew to make, without asking for help.
- Claude gave me 4 different news variations, which was nice
  - It's like I could see quickly the various ways to do some of the details for different variations
- So I've learned some new coding things from Claude 
  - And I gained a lot of variation experience with the newsapi interface 
    - That would have taken much longer to do by hand
- When asking about the sources, new code was generated
  - So you have to check-up on how the AI is using the API and assumptions it makes.
    - Which takes time
- All in all, it is faster to get code using the AI
  - But like text, you have to check assumptions it makes
- I liked the output format much better than mine.
  - So it probably pays to try some simple generation with AI to get quick simple reasonable code to begin with.
