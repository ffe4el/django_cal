import openai
import requests
from pprint import pprint
import json

openai.api_key = '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'

# messages = [
#     {"role": "system", "content": "You are a kind helpful assistant."},
# ]
#
# while True:
#     message = input("User : ")
#     if message:
#         messages.append(
#             {"role": "user", "content": message},
#         )
#         chat = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo", messages=messages
#         )
#
#     reply = chat.choices[0].message.content
#     print(f"ChatGPT: {reply}")
#     messages.append({"role": "assistant", "content": reply})
#     print(chat.choices[0].message.content)

URL = "https://api.openai.com/v1/chat/completions"

message = input("User : ")
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f"{message}"}],
    "temperature": 1.0,
    "top_p": 1.0,
    "n": 1,
    "stream": False,
    "presence_penalty": 0,
    "frequency_penalty": 0,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
}

response = requests.post(URL, headers=headers, json=payload, stream=False)

response.content

resp = json.loads(response.content)
# pprint(resp)

file_path = 'purchase_list.json'
with open(file_path,'w') as f:
    json.dump(resp,f, ensure_ascii=False)


print(resp['choices'][0]['message']['content'])
