
from dotenv import load_dotenv, dotenv_values
from datetime import datetime
from imessage_tools import read_messages, print_messages, send_message
import os
import re
import time
import google.generativeai as genai
from imessage_reader import fetch_data

load_dotenv()

gemini_key = (os.getenv("gemini_key"))
genai.configure(api_key=gemini_key)
model = genai.GenerativeModel("gemini-pro")
chat_history = [
    {"role": "system", "content": "You are a 18 year old texting a friend. Be nice and keep the conversation going. You are responding to text in a short manner and use some abrivations such as LOL. No paragraphs just a sentence. I just want the sentence/message with no explanation/reasoning. Never admit you're AI if asked because you are Noah."}
]
formatted_chat_history = [
    {
        "parts": [
            {
                "text": entry["content"]
            }
        ]
    }
    for entry in chat_history
]

imessages = ''
last_imessages = ''
chat_db = "/Users/noahwolk/Library/Messages/chat.db"
#self_number = 'your number'
#receiving_number = 'target number'
n = 1

while True:
    time.sleep(10)
    imessages = read_messages(chat_db, n=n, self_number=self_number, human_readable_date=True)
 
    number = (imessages[-1]["phone_number"])
    is_from_me = (imessages[-1]["is_from_me"])
    print(number)
    print (is_from_me)

    print("correct number!")
    if number != receiving_number:
     if is_from_me != 1:
      if imessages != last_imessages:
        last_imessages = imessages

        print(number)

        number = number.replace('+','')
        number = number[1:]
        print(number)

        message = (imessages[-1]["body"])
        print(message)
     
        chat_history.append({"role": "user", "content": message})
        response = model.generate_content(formatted_chat_history).text
        print(f"AI Response: {response}")
        chat_history.append({"role": "assistant", "content": response})
        
        send_message(response, imessages[-1]["phone_number"], False)