"""
* This script scrapes mobile phone data from the Mob4me website for a given list of mobile phone brands.
* The scraped data includes :
    the phone's name,
    brand,
    front and back camera specs,
    screen size,
    RAM,
    memory,
    battery,
    and price.

* The script uses the requests library to make HTTP requests to the Mob4me website and the BeautifulSoup library to parse the HTML content of the website.
* The scraped data is stored in a pandas DataFrame and saved to an Excel file.

TODO:
- functional programming
- unit tests
- type hints
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

from consts import (
    headers,
    URL,
    SCREEN_SIZE_SELECTOR,
    PRICE_SELECTOR,
    BATTERY_SELECTOR,
    BACK_CAM_SELECTOR,
    RAM_NAME_SELECTOR,
    FRONT_CAM_SELECTOR,
    MEMORY_NAME_SELECTOR,
    NEXT_BUTTON_SELECTOR,
    PHONE_ANCHORS_SELECTOR,
    BRANDS,
)


def get_element_text(soup, selector):
    element = soup.select_one(selector).text if soup.select_one(selector) else "Not Found"
    return element


def get_next_element_text(soup, selector):
    element = soup.select_one(selector) if soup.select_one(selector) else "Not Found"
    if element == "Not Found":
        return "Not Found"

    return element.find_next("td").text.replace("\n", "").strip()


def get_data_of_phone(phone_url):
    response = requests.get(phone_url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")

    name = phone_url.split(".com/")[-1].replace("-", " ")
    back_cam = get_element_text(soup, BACK_CAM_SELECTOR).replace("ميجا بكسل", "").strip()
    screen_size = get_element_text(soup, SCREEN_SIZE_SELECTOR)
    battery = get_element_text(soup, BATTERY_SELECTOR)
    price = get_element_text(soup, PRICE_SELECTOR)

    memory = get_next_element_text(soup, MEMORY_NAME_SELECTOR)
    ram = get_next_element_text(soup, RAM_NAME_SELECTOR)
    front_cam = get_next_element_text(soup, FRONT_CAM_SELECTOR)

    return {
        "name": name,
        "brand": name.split(" ")[0],
        "front_camera": front_cam,
        "back_camera": back_cam,
        "screen_size": screen_size,
        "RAM": ram,
        "Memory": memory,
        "Battery": battery,
        "URL": phone_url,
        "price": price,
    }


def get_data_of_page(brand, page):
    page_data = pd.DataFrame()
    page_url = f"{URL}{brand}/{page}"
    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    phone_anchors = soup.select(PHONE_ANCHORS_SELECTOR)
    for anchor in phone_anchors:
        print(anchor.get("href"))
        phone_data = get_data_of_phone(anchor.get("href"))
        phone_df = pd.DataFrame(phone_data, index=[phone_data["name"]])
        page_data = pd.concat([page_data, phone_df])
    next_button = soup.select(NEXT_BUTTON_SELECTOR)
    next_button_is_active = True if next_button else False
    return page_data, next_button_is_active


def scrap(brand: str) -> pd.DataFrame:
    page: int = 1

    phones_data: pd.DataFrame
    next_button_is_active: bool
    phones_data, next_button_is_active = get_data_of_page(brand, page)

    while next_button_is_active:
        page += 1
        print(brand, page)
        page_data, next_button_is_active = get_data_of_page(brand, page)
        phones_data = pd.concat([phones_data, page_data])
        if page == 5:
            break  # the latest 5 pages will contain latest 100 mobile of each brand
    return phones_data


def save_data_to_excel(dataframe, file_name):
    dataframe.to_excel(file_name, index=False)


def main():
    all_brands_data: pd.DataFrame = pd.DataFrame()
    for brand in BRANDS:
        brand_data = scrap(brand)
        all_brands_data = pd.concat([all_brands_data, brand_data])
        save_data_to_excel(all_brands_data, "mob4me.xlsx")


if __name__ == "__main__":
    main()
