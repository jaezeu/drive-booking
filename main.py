from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def booking(loginid, password):

    driver = webdriver.Edge()

    driver.get('https://booking.bbdc.sg/#/login?redirect=%2Ftransactions%2Findex')

    elementLogin = driver.find_element(By.ID, 'input-8') #login field
    elementLogin.send_keys(loginid)
    elementPw = driver.find_element(By.ID, 'input-15') #login field
    elementPw.send_keys(password)
    time.sleep(10)
    # press login
    # clickLogin = driver.find_element(By.CLASS_NAME, "div.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary")
    # clickLogin.click()
    # login=driver.find_element_by_name('submit-button')
    # driver.implicitly_wait(500)
    # login.click()
    # driver.implicitly_wait(4000)


def main():
    booking('123@mail.com', 'passcode')
    

if __name__ == "__main__":
    main()