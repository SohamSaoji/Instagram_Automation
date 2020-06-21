from selenium import webdriver
from credentials import username, password
import time

# install chromedriver
chromepath = 'path on you pc'

driver = webdriver.Chrome(executable_path=chromepath)

driver.get("https://www.instagram.com/")

time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(username)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(password)
driver.find_element_by_css_selector('button[type=submit]').click()
