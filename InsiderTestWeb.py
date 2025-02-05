import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

service = Service("C:\\Users\\damnb\\OneDrive\\Masaüstü\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://useinsider.com/")

def login(driver,email,password):
    actions = ActionChains(driver)


    mail_box = driver.find_element(By.XPATH, '//input[@id="email"]')
    mail_box.click()


    actions.send_keys(email) \
        .send_keys(Keys.TAB) \
        .send_keys(password) \
        .send_keys(Keys.TAB) \
        .perform()


    driver.find_element(By.XPATH, '//button[@id="login-button"]').click()

LoginButton = driver.find_element(By.XPATH,'//li[@class="nav-item"][1]')
LoginButton.click()

window_before = driver.window_handles[0]
window_after = driver.window_handles[1]  # Açılan yeni sekmeyi al
driver.switch_to.window(window_after)   # Yeni sekmeye geç

VerificationPage = driver.find_element(By.XPATH,"//p[text()='Log In to']")

if VerificationPage.is_displayed():
    print("RIGHT PAGE!")
else:
    print("WRONG PAGE!")
    driver.save_screenshot("./screenshotlogin.png")

login(driver, "test@examasdple.com","123123")

Message = driver.find_element(By.CLASS_NAME,"clearfix").text
if Message in "Complete the reCAPTCHA verification to continue.":
    print("CAPTCHA appeared!")
else:
    print("Check your email address and password.!")
print("Test is successful")

driver.switch_to.window(window_before)

url = driver.current_url
if "insider" in url:
    print("Returned to home page!")
else:
    print("Could not return to home page!")
    driver.save_screenshot("./screenshothome.png")

driver.quit()