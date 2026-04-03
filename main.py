import requests
from send_email import send_email
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
load_dotenv()





GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
url = ("https://newsapi.org/v2/top-headlines?"
       "category=business&"
       "language=en&"
       "apiKey=" + NEWS_API_KEY)


request = requests.get(url)

content = request.json()
articles = content["articles"]
print(articles)

model = init_chat_model(model="gemini-2.5-flash",
                        model_provider="google-genai",
                        api_key=GOOGLE_API_KEY
                        )
prompt = f"""
you're a news summarizer.
write a short paragraph analyzing those new.
add another second paragraph to tell me
how they affect the stock market.
here are the articles:
{articles}
"""
response = model.invoke(prompt)
response_str = response.content

body = response_str+"\n\n"

sender_email = "srikarch285@gmail.com"
receiver_email = "sreekarseshasaichunduru@gmail.com"

message = f"subject: News summary\n\nFrom:{sender_email}\nTo:{receiver_email}\n\n{body}"
encoded_message = message.encode("utf-8")
send_email(encoded_message)