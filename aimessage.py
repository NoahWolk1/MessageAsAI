
from datetime import datetime
from imessage_tools import read_messages, print_messages, send_message
import os
import re
import time
import openai

from imessage_reader import fetch_data


openai.api_key = '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'



imessages = ''
last_imessages = ''
chat_db = "/Users/noahwolk/Library/Messages/chat.db"
self_number = "3148138225"
n = 1

chat_log = []
chat_log.append({"role": "system", "content": "Act like a 17 year old talking to a friend named MAx. you guys are in boy scouts together. Talk normally."})
#chat_log.append({"role": "system", "content": "You are a helpful assistant."})

while True:
    time.sleep(5)
    imessages = read_messages(chat_db, n=n, self_number=self_number, human_readable_date=True)
    number = (imessages[-1]["phone_number"])
    is_from_me = (imessages[-1]["is_from_me"])
    print(number)
    print (is_from_me)
    if number == '+13145042974': #every new message pypasses this
     print("correct number!")
     if is_from_me != 1:
      if imessages != last_imessages:
        last_imessages = imessages


        print(number)

        number = number.replace('+','')
        number = number[1:]
        print(number)

        message = (imessages[-1]["body"])
        print(message)
        chat_log.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=chat_log
        )
        assistant_response = response['choices'][0]['message']['content']
        assistant_response = assistant_response.strip("\n").strip()
        print(assistant_response)
        chat_log.append({"role": "assistant", "content": assistant_response})
        time.sleep(3)
        send_message(assistant_response, imessages[-1]["phone_number"], False)
        #os.system("osascript sendMessage.applescript {} '{}'".format(number, assistant_response))