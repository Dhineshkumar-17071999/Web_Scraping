from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pandas as pd

option = Options()
option.headless = True
option.add_argument('window-size=1920x1080')

web = 'https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=678802104188&hvpos=&hvnetw=g&hvrand=11003282267470432252&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9075213&hvtargid=kwd-10573980&hydadcr=14453_2371562&gad_source=1'
driver = webdriver.Chrome(options=option)
driver.get(web)
time.sleep(10)

search_bar = driver.find_element(By.XPATH, "//input[@placeholder = 'Search Amazon.in']")
search_bar.click()
search_bar.send_keys("5G Mobiles")

login_button = driver.find_element(By.XPATH, "//input[@type = 'submit']")
login_button.click()
time.sleep(10)

mobile_name = []
rating = []
rating_count = []
discount_price = []
actual_price = []

i = 1

while True:
    time.sleep(8)
    try:
        print(i)
        results = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class = 'puisg-col puisg-col-4-of-12 puisg-col-8-of-16 puisg-col-12-of-20 puisg-col-12-of-24 puis-list-col-right']")))
        # results = driver.find_elements(By.XPATH,"//div[@class = 'puisg-col puisg-col-4-of-12 puisg-col-8-of-16 puisg-col-12-of-20 puisg-col-12-of-24 puis-list-col-right']")

        for result in results:
            # time.sleep(6)
            try:
                mobile = result.find_element(By.XPATH,'.//span[contains(@class,"a-size-medium a-color-base a-text-normal")]').text
                if mobile is not None:
                    mobile_name.append(mobile)
                else:
                    mobile_name.append("Null") 
                print(mobile)
            except Exception as e:
                print(f"Exception in mobile name : {e}")
                mobile_name.append("Null")

            try:
                rating_value = result.find_element(By.XPATH,'.//span[contains(@class,"a-icon-alt")]').text
                if rating_value is not None:
                    rating.append(rating_value)
                else:
                    rating.append("Null")
                print(rating_value)
            except Exception as e:
                print(f"Exception in rating value : {e}")
                rating.append("Null")

            try:
                rating_count_value = result.find_element(By.XPATH,'.//span[contains(@class,"a-size-base s-underline-text")]').text 
                if rating_count_value is not None:
                    rating_count.append(rating_count_value)
                else:
                    rating_count.append("Null")
                print(rating_count_value)
            except Exception as e:
                print(f"Exception in rating count : {e}")
                rating_count.append("Null")

            try:
                discount_price_value = result.find_element(By.CLASS_NAME,"a-price-whole").text
                if discount_price_value is not None:
                    discount_price.append(discount_price_value)  
                else:
                    discount_price.append("Null")  
                print(discount_price_value)
            except Exception as e:
                print(f"Exception in discount price : {e}")
                discount_price.append("Null")

            try:
                actual_price_value = result.find_element(By.XPATH, ".//span[contains(@class,'a-price a-text-price')]").text
                if actual_price_value is not None:
                    actual_price.append(actual_price_value)
                else:
                    actual_price.append("Null")
                print(actual_price_value)
            except Exception as e:
                print(f"Exception in discount price : {e}")
                actual_price.append("Null")
                
    except TimeoutException as e:
        print(f"Timeout Exception: {e}")
        break
    except Exception as e:
        print(f"Exception : {e}")

    i = i + 1
    try:
        next_page = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, './/a[contains(@class,"s-pagination-next s-pagination-button")]')))
        # next_page = driver.find_element(By.XPATH, './/a[contains(@class,"s-pagination-next s-pagination-button")]')
        next_page.click()
    except TimeoutException:
        print("Next page button not found, exiting loop.")
        break
    except Exception as e:
        print(f"Button Exception : {e}")
        break






print(f"mobile_name_length = {len(mobile_name)}")
print(f"rating_length = {len(rating)}")
print(f"rating_count_length = {len(rating_count)}")
print(f"discount_price_lenght = {len(discount_price)}")
print(f"actual_price_length = {len(actual_price)}")
        
df = pd.DataFrame({
    'mobile_name':mobile_name,
    'rating':rating,
    'rating_count':rating_count,
    'discount_price':discount_price,
    'actual_price':actual_price}
    )

df.to_csv('Amazon.csv', index = False)
time.sleep(3)
driver.quit()  