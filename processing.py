from nltk.tokenize import sent_tokenize
import requests
import nltk
from bs4 import BeautifulSoup
nltk.download('punkt')

def isolate(text_content, text_url):
  # Get only the sentence containing <strong>
  # first split it into sentences
  sentences = sent_tokenize(text_content)
  # Get the sentence containing <strong>
  strongSentence = ""
  for sentence in sentences:
    if (("<strong>" in sentence)):
      strongSentence = sentence
  if ((strongSentence == "") or (strongSentence == " ")):
    strongSentence = text_content + " - " + text_url
  # Now remove the <strong> and </strong> tags
  return strongSentence.replace("<strong>", "").replace("</strong>", "")

def processMath(combined_tokens):
  math_processed_output = combined_tokens + "[TempEndToken]"
  soup = BeautifulSoup(combined_tokens, "html.parser")
  mathTags = soup.find_all("kgmath")
  for mathTag in mathTags:
    mathTag_contents = mathTag.get_text()
    try:
      answer = eval(mathTag_contents)
    except:
      answer = "\nI tried solving this math equation, but I couldn't work it out."
    math_processed_output = math_processed_output.replace(str(mathTag), str(answer))
  return math_processed_output[:math_processed_output.index("[TempEndToken]")]

def searchkg(kgquery):
  url = "https://api.search.brave.com/res/v1/web/search"
  headers = {
      "Accept": "application/json",
      "Accept-Encoding": "gzip",
      "X-Subscription-Token": "BSA351aNNqhOZWBH13KaxqUooWpNLFi"
  }
  params = {
      "q": kgquery.replace(" ", "+")
  }
  response = requests.get(url, params=params, headers=headers)
  data = response.json()
  # Extracting the first description from the web results
  first_description = None
  if 'web' in data and 'results' in data['web'] and data['web']['results']:
      first_description_url = data['web']['results'][0]['url']
      first_description = data['web']['results'][0]['description']
  return isolate(first_description, first_description_url)

def processWeb(kgquery):
  web_processed_output = kgquery + "[TempEndToken]"
  soup = BeautifulSoup(kgquery, "html.parser")
  webTags = soup.find_all("kgweb")
  for webTag in webTags:
    webTag_contents = webTag.get_text()
    answer = searchkg(webTag_contents)
    web_processed_output = web_processed_output.replace(str(webTag), str(answer))
  return web_processed_output[:web_processed_output.index("[TempEndToken]")]

def fullProcess(text):
  mathProcessed = processMath(text)
  webProcessed = processWeb(mathProcessed)
  return webProcessed
