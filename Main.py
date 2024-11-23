import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.add_argument("--detach")
#options.page_load_strategy = 'none'

extension_path = os.path.join(os.getcwd(), "cookie.block.extension@gmail.com.xpi")

profile = webdriver.FirefoxProfile()
options.profile = profile

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)


#driver.set_page_load_timeout(30)

driver.install_addon(extension_path, temporary=True)
driver.maximize_window()
time.sleep(10)


#Add csv link manually

def commerce():
    sheet_id = "1Osf6ryRJyAbV1qlSoGQ8lbJlLuh3OqcXIiSiCNO5pgA"

    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

    for url in df["URL"]:

        try:
            print(url)
            driver.get(url)
            time.sleep(3)

        except Exception as e:
            print(f"Error occurred for URL: {url}. Error: {str(e)}")
            continue


def gov():
    sheet_id = "1aht9oOanM1SeiZABuaLCb7079ZnynICzqGxpKIW6_Kc"

    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

    cn = 1
    for url in df["URL"]:
        try:
            cn+=1
            print(url+" "+str(cn))
            driver.get(url)
            time.sleep(10)
        except Exception as e:
            print(f"Error occurred for URL: {url}. Error: {str(e)}")
            continue


def news():
    sheet_id = "1UQ1kn4FqZuhE3FUrjwR3NvUl9ohcFgBqet3jnG9esYg"

    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

    for url in df["URL"]:
        try:
            print(url)
            driver.get(url)
            time.sleep(3)
        except Exception as e:
            print(f"Error occurred for URL: {url}. Error: {str(e)}")
            continue


def uni():
    sheet_id = "1v6OB4X9tnR3weTHOdK3KIqmTRYd1UJGP2BlD4o2945c"

    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

    for url in df["URL"]:
        try:
            print(url)
            driver.get(url)
            time.sleep(3)
        except Exception as e:
            print(f"Error occurred for URL: {url}. Error: {str(e)}")
            continue

def software():
    sheet_id = "1J_MVbdrMgfB-RH-TubHlgE19J5tEXTZ19NaXa0m5_vo"

    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

    cn = 1
    for url in df["URL"]:
        try:
            cn+=1
            print(url+" "+str(cn))
            driver.get(url)
            time.sleep(10)
        except Exception as e:
            print(f"Error occurred for URL: {url}. Error: {str(e)}")
            continue


'''        
commerce()
gov()
news()
uni()
software()
'''
commerce()
