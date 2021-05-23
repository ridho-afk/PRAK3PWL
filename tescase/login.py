from selenium import webdriver


USERNAME = 'Aku'
EMAIL='Aku@gmail.com'
PASSWORD = '123456'
PASSWORD2 = '123456'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://prak3pwl.herokuapp.com/')

user_input = driver.find_element_by_name('username')
user_input.send_keys(USERNAME)

user_input = driver.find_element_by_name('email')
user_input.send_keys(EMAIL)

user_input = driver.find_element_by_name('password')
user_input.send_keys(PASSWORD)

user_input = driver.find_element_by_name('password2')
user_input.send_keys(PASSWORD2)

register_button = driver.find_element_by_id('signup')
register_button.click()




