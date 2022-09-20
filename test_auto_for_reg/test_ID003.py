import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_for_reg():
    browser = webdriver.Chrome()
    link = "http://qa.noveogroup.com/"
    browser.get(link)
    try:
        input_name = browser.find_element(By.ID, 'name')
        input_name.send_keys('Georgii')

        button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
        button.click()
        time.sleep(1)

        answer_test = browser.find_element(By.CLASS_NAME, 'alert.alert-danger').text
        

        assert answer_test == 'Some data is incorrect. Please check it.', 'test failed'
    finally:
        browser.quit()