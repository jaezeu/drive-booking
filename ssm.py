from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import turtle
import boto3

ssm = boto3.client("ssm")

def get_ssm_secret(parameter_name):
    return ssm.get_parameter(
        Name=parameter_name,
        WithDecryption=True
)

def booking(loginid, password):

    driver = webdriver.Edge()
    driver.get('https://booking.bbdc.sg/#/login?redirect=%2Ftransactions%2Findex')

    # if(driver.find_element(By.CSS_SELECTOR, "button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary")): #check if logged out
    driver.find_element(By.ID, 'input-8').send_keys(loginid)
    driver.find_element(By.ID, 'input-15').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary").click()
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH, "//a[@href='#/booking']").click()
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Practical ')]").click()
    driver.implicitly_wait(30)
    driver.find_element(By.CSS_SELECTOR, "button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary").click()
    driver.implicitly_wait(30)
    time.sleep(5)
    # elif():


def main():
    loginid = get_ssm_secret("bbdc_login").get("Parameter").get("Value")
    password = get_ssm_secret("bbdc_pw").get("Parameter").get("Value")
    if len(loginid) > 1 and len(password) > 1:
        booking(loginid, password)
    

if __name__ == "__main__":
    main()