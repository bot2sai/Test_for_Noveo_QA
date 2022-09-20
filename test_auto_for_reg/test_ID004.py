import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_for_reg():
    browser = webdriver.Chrome()
    link = "http://qa.noveogroup.com/"
    browser.get(link)
    try:
        input_name = browser.find_element(By.ID, 'name')
        input_name.send_keys('G')
        input_email = browser.find_element(By.ID, 'email')
        input_email.send_keys('bot2sai@mail.ru')
        input_password = browser.find_element(By.ID, 'password')
        input_password.send_keys('12345678')
        input_repeat_password = browser.find_element(By.ID, 'repeat_password')
        input_repeat_password.send_keys('12345678')
        input_birthday = browser.find_element(By.ID, 'birthday')
        input_birthday.send_keys('18/01/1993')

        button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
        button.click()
        time.sleep(1)
        answer_test = browser.find_element(By.CLASS_NAME, 'invalid-feedback').text

        assert answer_test == 'Name is too short. It have 2 characters or more.', 'test failed'
    finally:
        browser.quit()