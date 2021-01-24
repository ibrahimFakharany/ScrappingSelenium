from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 


PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.techwithtim.net")

print("Title of the page :",  driver.title)

searchInput = driver.find_element_by_name('s')
searchInput.send_keys('test')
searchInput.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main'))
    )
    articles = main.find_elements_by_tag_name('article')
    for article in articles: 
        summary= article.find_element_by_class_name('entry-summary')
        print(summary.text)
except Exception as e:
    print(e)
   