from playwright.sync_api import Playwright, sync_playwright, expect
import multiprocessing
import pandas as pd
from time import sleep, perf_counter

url = 'https://www.geeksforgeeks.org/'

def run(playwright: Playwright) -> None:
    # Browser [Chrome, Firefox, WebKit]
    # browser = playwright.firefox.lanch(headless=False)

    # Device Control
    # dev = playwright.devices('Mac')
    browser = playwright.chromium.launch(headless=False)
    
    # Browser Screen Size
    # context = browser.new_context(viewport={ 'width': 2560, 'height': 1440 })
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    sleep(0.5)
    # print("success")

    # Browsing the website

    # Login
    # page.reload()
    page.locator('//div[@id="comp"]//div[contains(@class, "header-main__container")]//button[text()="Sign In"]').click()
    sleep(2)
    page.locator('//div[@class="content"]//div//input[@placeholder="Username or Email"]').fill("taneshka.mehta@gmail.com")
    page.locator('//div[@class="content"]//div//input[@placeholder="Enter password"]').fill("Taanu@1004")
    sleep(1)
    page.locator('//label[@for="rememberMe"]/preceding::input[@id="rememberMe"]').uncheck()
    page.locator('//div[@class="content"]//button[@type="submit"]').click()
    sleep(4)

    # if page.locator('//div[contains(@class, "content")]').is_visible():
    #     # print("skip")
    #     sleep(2.55)
    #     page.locator('//div[contains(@class, "content")]//div[@id="lower_section_text"]').click()
    #     sleep(2)

    # Website Header
    if page.locator('//div[contains(@class, "parentContainer")]').is_visible():
        page.locator('//div[contains(@class, "parentContainer")]//ul//li//div[text()="Courses"]').hover()
        sleep(2)
        page.locator('//div[contains(@class, "parentContainer")]//ul//li//div[text()="Practice"]').hover()
        sleep(2)
    
    # Website SubHeader
    if page.locator('//div[contains(@class, "mainContainerSub")]').is_visible():

        # Right Slide
        page.locator('(//div[contains(@class, "mainContainerSub")]//i)[2]').click()
        page.locator('(//div[contains(@class, "mainContainerSub")]//i)[2]').click()

        # Left Slide
        page.locator('(//div[contains(@class, "mainContainerSub")]//i)[1]').click()

        # Accessing Random Content (C++ Course)
        page.locator('//div[contains(@class, "mainContainerSub")]//ul//li/a[text()="C++"]').click()
        # page.locator('(//div[@id="main"]//div[@class="article--viewer_content"]//h2)[1]/span').scroll_into_view_if_needed()

        # Data Extraction [C++]
        que = page.locator('(//div[@id="main"]//div[@class="article--viewer_content"]//div[@class="text"]//span)[1]').inner_text()
        cont1 = page.locator('(//div[@id="main"]//div[@class="article--viewer_content"]//div[@class="text"]//span)[2]').text_content()
        cont2 = page.locator('(//div[@id="main"]//div[@class="article--viewer_content"]//div[@class="text"]//span)[3]').text_content()

        print("\n")
        print(que)
        print("\t")
        print(cont1)
        print("\n")
        sleep(2)

    # Website Home Page
    if page.locator('//div[@class="header-main__wrapper"]//div[@class="_logo"]').is_visible():
        page.locator('//div[@class="header-main__wrapper"]//div[@class="_logo"]').scroll_into_view_if_needed()
        page.locator('//div[@class="header-main__wrapper"]//div[@class="_logo"]').click()
        sleep(2)
    
    # Browsing Website Home Page
    page.locator('//h2[text()="Courses"]').scroll_into_view_if_needed()
    sleep(1)
    page.locator('//h2[text()="Explore"]').scroll_into_view_if_needed()
    sleep(1)
    page.locator('//h2[text()="Must Explore"]').scroll_into_view_if_needed()
    sleep(1)
    page.locator('//h2[text()="Web Development"]').scroll_into_view_if_needed()
    sleep(1)
    page.locator('//h2[text()="Programming Languages"]').scroll_into_view_if_needed()
    sleep(1)
    page.locator('//h2[text()="Databases"]').scroll_into_view_if_needed()
    sleep(1)
    page.locator('//h2[text()="Tutorials"]').scroll_into_view_if_needed()
    sleep(1)

    # Website Footer
    if page.locator('//div[@class="footer-container"]').is_visible():
        page.locator('//div[@class="footer-container"]').scroll_into_view_if_needed()
        sleep(2.80)
        # print("\n")
        print("GeeksforGeeks Address -:")
        print(page.locator('(//div[@class="footer-container_address_content "])[1]').all_inner_texts())
        print("\n")

    context.close()
    browser.close()


def fn_run():
    # information('function f')
    with sync_playwright() as playwright:
        run(playwright)

if __name__ == "__main__":
    start = perf_counter()
    fn_run()
    end = perf_counter()
    print(f'\n---------------\n Finished in {round(end-start, 2)} second(s)')
