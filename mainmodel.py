from processing import *

system_prompt = "You are a friendly AI language model named Matilda, made by a company called Kendasi. Whenever you are asked to do math, reply with <kgmath>PUT EQUATION HERE</kgmath> and it will automatically format for the user to show the answer, for example <kgmath>2 * 4</kgmath> will replace with 8. Do this EVERY time you are doing math. The text inside should be in python format, meaning don't put LaTeX inside, don't put X or the actual divided symbol, put * and / instead. When you are asked about a recent event or news from after 2021, reply with <kgweb>PUT QUESTION HERE</kgweb> and it will automatically format for the user with an answer found on the web. For example, <kgweb>What is the meaning of life?</kgweb> can be done. ONLY look up things with <kgweb> that the user asks about thats from after 2021 that is recent news or events.. ALWAYS use kgmath when doing math. Never work it out yourself, even when doing larger equations and using kgmath to work out smaller parts, step by step. Include the <kgmath> tags. ONLY use <kgweb> for difficult questions that you don't know the answer to or recent events, do NOT use it in general conversation. <kgweb> should not be used for poems, essays, or anything that you write for the user, only for actual questions."

import requests
import re

def get_gpt_response(data):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
  }
  response = requests.post(url, headers=headers, json=data)
  response_json = response.json()
  if 'choices' in response_json and len(response_json['choices']) > 0:
      completion = response_json['choices'][0]['message']['content']
      return fullProcess(completion)
  else:
      raise Exception('There was an error, and the model could not generate a response.')

data = {
  "model": "gpt-3.5-turbo",
  "messages": [
      {"role": "system", "content": system_prompt}
    ],
    "temperature": 0.7
}
"""
for i in range(10):
  user_input = input("You: ").replace("'", "").replace('"', "")
  told_input = user_input + " \n The previous text was the user's query, which you should response to. The following text is not part of the conversation, just a reminder: Remember to use <kgmath> and <kgweb> IF you have been asked a question. It should say EXACTLY those tags, DON'T change it or do any typos, otherwise it won't work. ONLY use <kgweb> if you don't know the answer or if it's about an event that's recent. ALWAYS use <kgmath> when it's a math question."
  data["messages"].append({"role": "user", "content": told_input})
  model_response = get_gpt_response(data)
  if (model_response == " " or model_response == ""):
    model_response = "Sorry, I couldn't find any information about that on the internet. If you need anything else, feel free to let me know!"
  print("AI:", model_response)
  data["messages"].append({"role": "assistant", "content": model_response})
print("To save on computing power, you can only send a maximum of 10 messages to the AI in one conversation. Please start a new conversation.")
"""
