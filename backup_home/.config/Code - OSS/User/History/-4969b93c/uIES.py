from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import json
from time import sleep




def initialize_driver():
    options = webdriver.FirefoxOptions()
    options.profile = "/home/owl/.mozilla/firefox/interact.profile/"
    service = webdriver.FirefoxService(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    return driver


def open_craigslist(driver):
    driver.get("https://accounts.craigslist.org/login?rp=%2Flogin%2Fhome%3Fshow_tab%3Dpostings%26lang%3Den_us&rt=L")



def login(driver, email, password):
    try:
        input_element = driver.find_element(By.NAME, "inputEmailHandle")
        input_element.send_keys(email)
        password_element = driver.find_element(By.NAME, "inputPassword")
        password_element.send_keys(password)

        login_button = driver.find_element(By.ID, "login")
        # login_button.click
    except Exception:
        print("Already logged in")


def select_area(driver,area):
    select_element = driver.find_element(By.NAME, "areaabb")
    select = Select(select_element)
    

    select.select_by_visible_text(area)

    submit_area = driver.find_element(By.XPATH, "//button[@value='go']")
    submit_area.click()

def get_options(driver):
    select_element = driver.find_element(By.NAME, "areaabb")
    select = Select(select_element)
    all_options = select.options
    return all_options




def get_country(driver,all_options):
    countries = {option.text.split(',')[-1].strip() for option in all_options}

    countries=list(countries)

    country = select_element_from_array(countries)
    return country

def filter_by_country(all_options, country):
    country_options = [option.text for option in all_options if country in option.text]
    return country_options

def select_element_from_array(array):
    array = sorted(array)
    print("Select an index from the following options:")
    for i, element in enumerate(array):
        if hasattr(element, "text"):
            print(f"{i}: {element.text}")
        else:
            print(f"{i}: {element}")
    
    while True:
        try:
            index = int(input("Enter the index: "))
            if index < 0 or index >= len(array):
                print("Invalid index. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    selection = array[index]
    print(f"Selected element: {selection}")
    return selection


def select_post_type(driver):
    post_type = driver.find_element(By.XPATH, "//input[@value='jo']")
    post_type.click()

    submit = driver.find_element(By.XPATH, "//button[@value='Continue']")
    submit.click()



def select_job_type(driver):
    post_type = driver.find_element(By.XPATH, "//input[@value='57']")
    post_type.click()

    # submit = driver.find_element(By.XPATH, "//button[@value='Continue']")
    # submit.click()

def post_ad(driver,ad):
    posting_title = driver.find_element(By.XPATH, "//input[@name='PostingTitle']")
    city = driver.find_element(By.XPATH, "//input[@name='geographic_area']")
    description = driver.find_element(By.XPATH, "//textarea[@name='PostingBody']")


    employment_type= driver.find_element(By.XPATH, "//span[@id='ui-id-1-button']")

    job_title = driver.find_element(By.XPATH, "//input[@name='job_title']")
    compensation = driver.find_element(By.XPATH, "//input[@name='remuneration']")
    company_name = driver.find_element(By.XPATH, "//input[@name='company_name']")
    
    posting_title.send_keys(ad.get('posting_title'))
    city.send_keys(ad.get('city'))
    description.send_keys(ad.get('description'))

    employment_type.click()
    employment_type = driver.find_element(By.XPATH, "//li[@id='ui-id-6']")
    employment_type.click()


    job_title.send_keys(ad.get('job_title'))
    compensation.send_keys(ad.get('compensation'))
    company_name.send_keys(ad.get('company_name'))
    
    submit = driver.find_element(By.XPATH, "//button[@value='continue']")
    submit.click()

    sleep(2)
    images_submit = driver.find_element(By.XPATH, "//button[@name='go']")
    images_submit.click()
    


def get_json_ads():
    with open("ads.json") as f:
        ads = json.load(f)
    return ads

def main():

    driver = initialize_driver()
    open_craigslist(driver)
    login(driver, "qualityinteract2@gmail.com", "InterAct2021")
    all_country_options = get_options(driver)
    country=get_country(driver,all_country_options)
    country_options = filter_by_country(all_country_options, country)
    area=select_element_from_array(country_options)

    ads=get_json_ads()

    for ad in ads:
        open_craigslist(driver)
        select_area(driver,area)
        select_post_type(driver)
        select_job_type(driver)
        post_ad(driver,ad)
        input()
    driver.quit()

main()