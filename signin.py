from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
username="sandhiya.baskar5@gmail.com"
passwords="kannakuttydiya@5"
browser=webdriver.Chrome()
browser.get(("http://www.gmail.com"))
user=browser.find_element_by_id('identifierId')
user.send_keys(username)
nextbutton=browser.find_element_by_id("identifierNext")
nextbutton.click()
#wait = ui.WebDriverWait(browser, 10)
#wait.until(page_is_loaded)
browser.implicitly_wait(30)
pswd=browser.find_element_by_name("password")
pswd.send_keys(passwords)
signinbutton=browser.find_element_by_id("passwordNext")
signinbutton.click()
