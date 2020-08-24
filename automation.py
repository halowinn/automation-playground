from selenium import webdriver
import time

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

time.sleep(3)
close_popup = chrome_browser.find_element_by_id('at-cv-lightbox-close')
close_popup.click()

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am a valorant player')

show_message_button.click()

time.sleep(5)
chrome_browser.quit()
