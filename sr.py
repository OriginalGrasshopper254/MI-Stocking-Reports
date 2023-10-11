#! A simple script to check the DNR of Michigan Stocking Report on my favorited areas to fish.
# Author: 'UleMangaa'

# Importing necessary modules.

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#defining webdriver using Safari.
driver = webdriver.Safari()
url = 'https://www.dnr.state.mi.us/fishstock'

def county_selector():
    # Function will select county based on user input.

    Bay_XPATH = '//*[@id="Counties"]/option[10]'
    Clare_XPATH = '//*[@id="Counties"]/option[19]'
    Genesee_XPATH = '//*[@id="Counties"]/option[26]'
    Gladwin_XPATH = '//*[@id="Counties"]/option[27]'
    Midland_XPATH = '//*[@id="Counties"]/option[57]'
    Newaygo_XPATH = '//*[@id="Counties"]/option[63]'
    Saginaw_XPATH = '//*[@id="Counties"]/option[74]'

    # Creating a while loop incase user inputs incorrect input.
    val = True
    while val:
        place = input('''Which county would you like to see the stocking report for? \n
                  So far I offer the following counties:
                  1. Bay County.
                  2. Clare County.
                  3. Genesee County.
                  4. Gladwin County.
                  5. Midland County.
                  6. Newaygo County.
                  7. Saginaw County. \n~: ''')

        if place.lower() == 'bay':
            driver.get(url)
            print(driver.title + ' Stocking Report!')
            county_selector = driver.find_element(By.XPATH, Bay_XPATH).click()
            val = False

        elif place.lower() == 'clare':
            driver.get(url)
            print(driver.title + ' Stocking Report!')
            county_selector = driver.find_element(By.XPATH, Clare_XPATH).click()
            val = False

        elif place.lower() == 'genesee':
            driver.get(url)
            print(driver.title + ' Stocking Report!')
            county_selector = driver.find_element(By.XPATH, Genesee_XPATH).click()
            val = False

        elif place.lower() == 'gladwin':
            driver.get(url)
            print(driver.title + ' Stocking Report!')
            county_selector = driver.find_element(By.XPATH, Gladwin_XPATH).click()
            val = False

        elif place.lower() == 'midland':
            driver.get(url)
            print(driver.title + ' Stocking Report!')
            county_selector = driver.find_element(By.XPATH, Midland_XPATH).click()
            val = False

        elif place.lower() == 'newaygo':
            driver.get(url)
            print(driver.title + ' Stocking Report!')
            county_selector = driver.find_element(By.XPATH, Newaygo_XPATH).click()
            val = False

        elif place.lower() == 'saginaw':
            driver.get(url)
            county_selector = driver.find_element(By.XPATH, Saginaw_XPATH).click()
            val = False

        else:
            print(''' Wrong input. I dont recognize what your telling me. \n''')


def get_info():
    # Function will automatically select the start year and month as Jan 2021 and end as Jan 2023.

    start_month_selector = driver.find_element(By.XPATH, '//*[@id="StartMonth"]/option[1]').click()
    start_year_selector = driver.find_element(By.XPATH, '//*[@id="StartYear"]/option[3]').click()
    end_month_selector = driver.find_element(By.XPATH, '//*[@id="EndMonth"]/option[1]').click()
    end_year_selector = driver.find_element(By.XPATH, '//*[@id="EndYear"]/option[1]').click()

    # Submits request.
    submit_Button = driver.find_element(By.XPATH, '//*[@id="submitQueryBtn"]').send_keys(Keys.RETURN)

    # sleep is essential 😉
    time.sleep(1)

    # Getting table contents
    tbody = driver.find_element(By.XPATH, '//*[@id="FishGrid"]/div[2]/table/tbody');
    data = []

    # Creating for loop to iterate and cycle through the contents of the table and append to 'data' variable.
    for tr in tbody.find_elements(By.XPATH, '//tr'):
        row = [item.text for item in tr.find_elements(By.XPATH, './/td')]
        data.append(row)

    # Passing table data to Pandas DataFrame.
    df = pd.DataFrame(data)
    print(df)

    driver.quit()


county_selector()
get_info()
