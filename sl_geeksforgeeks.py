from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://www.geeksforgeeks.org/'

# Browser [Chrome, Firefox, Edge, Safari]
driver = webdriver.Chrome()
print("start")
print("------------------")
print("\n")

# JAVA can use navigate methood but Python only uses get method

# driver.navigate().to(url)
# driver.navigate().refresh()
# driver.navigate().forward()
# driver.navigate().back()

driver.get(url)
action = ActionChains(driver)
# driver.refresh()
# driver.fullscreen_window()

# Log In
time.sleep(2)
driver.find_element(By.XPATH, '//div[@id="comp"]//div[contains(@class, "header-main__container")]//button[text()="Sign In"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//div[@class="content"]//div//input[@placeholder="Username or Email"]').send_keys('taneshka.mehta@gmail.com')
time.sleep(0.2)
driver.find_element(By.XPATH, '//div[@class="content"]//div//input[@placeholder="Enter password"]').send_keys('Taanu@1004')
driver.find_element(By.XPATH, '//label[@for="rememberMe"]/preceding::input[@id="rememberMe"]').click()
driver.find_element(By.XPATH, '//div[@class="content"]//button[@type="submit"]').click()
time.sleep(2)

# if driver.find_element(By.XPATH, '//div[contains(@class, "content")]').is_displayed():
#     time.sleep(2.555)
#     driver.find_element(By.XPATH, '//div[contains(@class, "content")]//div[@id="lower_section_text"]').click()
#     time.sleep(2)

# Website Header
if driver.find_element(By.XPATH, '//div[contains(@class, "parentContainer")]').is_displayed():
    action.move_to_element(driver.find_element(By.XPATH, '//div[contains(@class, "parentContainer")]//ul//li//div[text()="Courses"]')).perform()
    time.sleep(2)
    action.move_to_element(driver.find_element(By.XPATH, '//div[contains(@class, "parentContainer")]//ul//li//div[text()="Practice"]')).perform()
    time.sleep(2)

# Website SubHeader
if driver.find_element(By.XPATH, '//div[contains(@class, "mainContainerSub")]').is_displayed():
    # Right Slide
    driver.find_element(By.XPATH, '(//div[contains(@class, "mainContainerSub")]//i)[2]').click()
    driver.find_element(By.XPATH, '(//div[contains(@class, "mainContainerSub")]//i)[2]').click()

    # Left Slide
    driver.find_element(By.XPATH, '(//div[contains(@class, "mainContainerSub")]//i)[1]').click()

    # Accessing Random Content (C++ Course)
    driver.find_element(By.XPATH, '//div[contains(@class, "mainContainerSub")]//ul//li/a[text()="C++"]').click()

    # Data Extraction [C++] 
    que = driver.find_element(By.XPATH, '(//div[@id="main"]//div[@class="article--viewer_content"]//div[@class="text"]//span)[1]').text
    print(que)
    cont1 = driver.find_element(By.XPATH, '(//div[@id="main"]//div[@class="article--viewer_content"]//div[@class="text"]//span)[2]').text
    print(cont1)
    cont2 = driver.find_element(By.XPATH, '(//div[@id="main"]//div[@class="article--viewer_content"]//div[@class="text"]//span)[3]').text
    print(cont2)

    # Website Home Page
    if driver.find_element(By.XPATH, '//div[@class="header-main__wrapper"]//div[@class="_logo"]').is_displayed():
        action.move_to_element(driver.find_element(By.XPATH, '//div[@class="header-main__wrapper"]//div[@class="_logo"]')).perform()
        driver.find_element(By.XPATH, '//div[@class="header-main__wrapper"]//div[@class="_logo"]').click()
        time.sleep(2)

    # Browsing Website and Home Page
    action.move_to_element(driver.find_element(By.XPATH, '//h2[text()="Courses"]')).perform()
    time.sleep(0.2)

    action.move_to_element(driver.find_element(By.XPATH, '//h2[text()="Explore"]')).perform()
    time.sleep(0.2)

    action.move_to_element(driver.find_element(By.XPATH, '//h2[text()="Must Explore"]')).perform()
    time.sleep(0.2)

    action.move_to_element(driver.find_element(By.XPATH, '//h2[text()="Web Development"]')).perform()
    time.sleep(0.2)

    action.move_to_element(driver.find_element(By.XPATH, '//h2[text()="Programming Languages"]')).perform()
    time.sleep(0.2)

    action.move_to_element(driver.find_element(By.XPATH, '//h2[text()="Databases"]')).perform()
    time.sleep(0.2)

    action.move_to_element(driver.find_element(By.XPATH, '//h2[text()="Tutorials"]')).perform()
    time.sleep(0.2)

    # Website Footer 
    if driver.find_element(By.XPATH, '//div[@class="footer-container"]').is_displayed():
        action.move_to_element(driver.find_element(By.XPATH, '//div[@class="footer-container"]')).perform()
        time.sleep(2.80)
        print('\n')
        print("GeeksforGeeks Address -:")
        print(driver.find_element(By.XPATH, '(//div[@class="footer-container_address_content "])[1]').text)
        print('\n')

time.sleep(2)
print("\n")
print("------------------")
print("end")
driver.quit