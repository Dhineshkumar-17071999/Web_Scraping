from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import os

web_site = 'https://www.adamchoi.co.uk/overs/detailed'


driver_location = 'chromedriver'
driver = webdriver.Chrome()

driver.get(web_site)

all_matches_button = driver.find_element(By.XPATH,'//label[@analytics-event = "All matches"]')
all_matches_button.click()

drop_down = Select(driver.find_element(By.ID,'country'))
drop_down.select_by_visible_text("Spain")
time.sleep(10)
matches = driver.find_elements(By.XPATH,'//tr')

date = []
home_team = []
score = []
away_team = []

print(len(matches))
for match in matches:
    print(match.text)
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home_team.append(match.find_element(By.XPATH,'./td[2]').text)
    score.append(match.find_element(By.XPATH,'./td[3]').text)
    away_team.append(match.find_element(By.XPATH,'./td[4]').text)

df = pd.DataFrame({'date':date,'home_team':home_team,'score':score,'away_team':away_team})
df.to_csv('football_spain_data.csv',index = False)

driver.quit()
