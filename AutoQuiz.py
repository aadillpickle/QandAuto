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
import re
import string


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

'''Pinging deepquiz API'''
url = "https://gs4ossx7yj.execute-api.us-east-1.amazonaws.com/dev/text"
headers = {
    'Content-Type': "text/plain",
    'cache-control': "no-cache",
    'Postman-Token': "7063f14d-46ba-4715-a4b2-9932a6e16685"
    }

article_text = driver.find_element_by_xpath(wiki_xpath).text
article_text = article_text.encode('utf-8')
article_text = article_text.split()

#remember to remove references, if it says \nReferences[edit] then take whatevers after that out

questions = []
answers = []
    
headers = {k: str(v).encode("utf-8") for k, v in headers.items()}
chunks = [article_text[x:x+5800] for x in range(0, len(article_text), 5800)] 

for word_chunk in chunks:
    #response = requests.request("POST", url, data = word_chunk, headers = headers) 
    response = requests.request("POST", url, data = word_chunk, headers = headers) 
    print(response.text)
    '''
    response_text = json.loads(response.text)
    for i in range(0, len(response_text)):
        if response_text[i]["QuestionType"] != "TRUE_FALSE":
           questions.append(response_text[i]["QuestionPrompt"])
           answers.append(response_text[i]["CorrectAnswer"])'''
