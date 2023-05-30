import httpx
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
    brands
)

def get_data_of_phone(phone_url):
    response = httpx.get(phone_url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    name = phone_url.split('.com/')[-1].replace('-',' ')
    back_cam = soup.select_one(BACK_CAM_SELECTOR).text.replace('ميجا بكسل','').strip()
    screen_size = soup.select_one(SCREEN_SIZE_SELECTOR)
    battery = soup.select_one(BATTERY_SELECTOR).text
    price = soup.select_one(PRICE_SELECTOR).text

    memory_name = soup.select_one(MEMORY_NAME_SELECTOR)
    if memory_name:
        memory = memory_name.find_next('td').text.replace('\n','').strip()
    else:
        memory = "Not Found"
    ram_name = soup.select_one(RAM_NAME_SELECTOR)
    if ram_name:
        ram = ram_name.find_next('td').text.replace('\n','').strip()
    else:
        ram = "Not Found"
    front_cam_name = soup.select_one(FRONT_CAM_SELECTOR)
    if front_cam_name:
        front_cam = front_cam_name.find_next('td').text.replace('\n','').strip()
    else:
        front_cam = "Not Found"

    return {
        'name':name,
        'brand':name.split(' ')[0],
        'front_camera':front_cam,
        'back_camera':back_cam,
        'screen_size':screen_size,
        'RAM':ram,
        'Memory':memory,
        'Battery':battery,
        'URL':phone_url,
        'price':price
    }

def get_data_of_page(brand , page):
    page_data = pd.DataFrame()
    page_url = f"{URL}{brand}/{page}"
    response = httpx.get(page_url,headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    phone_anchors = soup.select(PHONE_ANCHORS_SELECTOR)
    for a in phone_anchors:
        print(a.get('href'))
        phone_data = get_data_of_phone(a.get('href'))
        phone_df = pd.DataFrame(phone_data,index =[phone_data['name']] )
        page_data = pd.concat([page_data, phone_df])
    next_button = soup.select(NEXT_BUTTON_SELECTOR)
    next_button_is_active = True if next_button else False 
    return page_data , next_button_is_active
        


def scrap(brand):
    page = 1
    phones_data,next_button_is_active = get_data_of_page(brand, page)
    while next_button_is_active:
        page+=1
        page_data,next_button_is_active = get_data_of_page(brand, page)
        phones_data = pd.concat([phones_data, page_data])
    return phones_data   

def save_data_to_csv(dataframe, file_name):
    dataframe.to_csv(file_name, index=False)

def main():
    all_brands_data = pd.DataFrame()
    for brand in brands:
        brand_data = scrap(brand)
        all_brands_data = pd.concat([all_brands_data,brand_data])
        save_data_to_csv(all_brands_data,"mob4me.csv")

if __name__ == '__main__':
    main()
