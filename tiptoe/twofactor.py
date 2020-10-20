import requests
import time
import json

def check_2factor_submit(browser):
    try:
        otp_submit = browser.find_element_by_id("auth-send-code")
    except NoSuchElementException:
        return ""
    otp_submit.click()


def check_2factor_field(browser):
    try:
        otp_field = browser.find_element_by_id("auth-mfa-otpcode")
    except NoSuchElementException:
        return ""
    otp = get_2factor()
    time.sleep(8)
    otp_field.send_keys(otp)
    time.sleep(3)
    otp_field.submit()


def check_2factor(browser):
    check_2factor_submit(browser)
    time.sleep(15)
    check_2factor_field(browser)
    return ""


def get_2factor():
    
    msgs = json.loads(response.content)
    latest_msg = msgs["messages"][0]["body"]
    otp_code = latest_msg.split(" ")[0]
    loggit("2factor code: {}".format(otp_code))
    return otp_code
