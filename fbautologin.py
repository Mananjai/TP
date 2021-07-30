from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:\\Users/Mananjai_B/Downloads/chromedriver")
driver.get('https://en-gb.facebook.com/r.php?locale=en_GB&display=page')
searchBar = driver.find_element_by_name("firstname")
searchBar.send_keys("Tom")

time.sleep(2)
lastName = driver.find_element_by_name("lastname")
lastName.send_keys("Jerry")

time.sleep(2)
emailMobile = driver.find_element_by_name('reg_email__')
emailMobile.send_keys("Tom_and_Jerry@gmail.com")

time.sleep(2)
emailMobile2 = driver.find_element_by_name('reg_email_confirmation__')
emailMobile2.send_keys("Tom_and_Jerry@gmail.com")

time.sleep(2)
password = driver.find_element_by_name('reg_passwd__')
password.send_keys("12345")

monthSelect = Select(driver.find_element_by_name('birthday_month'))
monthSelect.select_by_value('13')
time.sleep(2)

daySelect = Select(driver.find_element_by_name('birthday_day'))
daySelect.select_by_visible_text('2')
time.sleep(2)

yearSelect = Select(driver.find_element_by_name("birthday_year"))
yearSelect.select_by_visible_text('2002')
time.sleep(2)

ac = ActionChains(driver)
genderSelect = driver.find_element_by_id('u_0_5')
ac.click(genderSelect).perform()
time.sleep(2)
ac.send_keys(Keys.ENTER).perform()
time.sleep(2)
