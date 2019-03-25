import json
import requests
import selenium
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import numpy as np

'''Scraping text from wikipedia or medium article'''
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
website_link = str(input("Enter the link of your article"))

driver = webdriver.Chrome(executable_path = "chromedriver.exe", options = option)
driver.get(website_link)

timeout = 5
wiki_xpath = "//div[@class= 'mw-parser-output']"
medium_article_xpath = "//div[@class= 'section-content']"

try:
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, wiki_xpath)))
except TimeoutException:
    pass
    #print("Sorry, the page took too long to load.")
    #driver.quit()

article_text = driver.find_element_by_xpath(wiki_xpath).text
'''Pinging deepquiz API'''
url = "https://gs4ossx7yj.execute-api.us-east-1.amazonaws.com/dev/text"
headers = {
    'Content-Type': "text/plain",
    'cache-control': "no-cache",
    'Postman-Token': "7063f14d-46ba-4715-a4b2-9932a6e16685"
    }

article_text = article_text.encode('utf-8')
article_text = article_text.split()
article_chunks = [[]]
for count, word in enumerate(article_text):
    article_chunks.append(word)
    if count % 5800 == 0:
        
        
'''headers = {k: str(v).encode("utf-8") for k,v in headers.items()}

if len(article_text) > 5800: 
    for i in

response = requests.request("POST", url, data = article_text, headers = headers) 

response_text = json.loads(response.text)

#Processing response text
def get_q_and_a(deepquiz_response): 
    questions = []
    answers = []
    for i in range(0, len(deepquiz_response)):
        if deepquiz_response[i]["QuestionType"] != "TRUE_FALSE":
           questions.append(deepquiz_response[i]["QuestionPrompt"])
           answers.append(deepquiz_response[i]["CorrectAnswer"])

    return questions, answers

print(get_q_and_a(response_text))'''