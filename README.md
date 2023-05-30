# Mob4me Mobile Phone Scraper
* This script scrapes mobile phone data from the Mob4me website for a given list of mobile phone brands. The scraped data includes the phone's name, brand, front and back camera specs, screen size, RAM, memory, battery, and price.

# Getting Started
## Prerequisites
To run this script, you will need to have Python 3.x installed on your system. You will also need to install the following Python libraries:

* requests
* BeautifulSoup4
* pandas <br>
You can install these libraries by running the following command:

```python
pip install requests beautifulsoup4 pandas
```
## Usage
To run the script, open a terminal in the directory where the script is located and run the following command:

```python
main.py
```

The scraped data will be saved to an Excel file named "mob4me.xlsx" in the same directory.

## Customization
You can customize the script by modifying the following constants in the consts.py file:

* BRANDS: A list of mobile phone brands to scrape from the Mob4me website.
* NEXT_BUTTON_SELECTOR: A CSS selector for the "Next" button element on the Mob4me website.
* PHONE_ANCHORS_SELECTOR: A CSS selector for the phone anchor elements on the Mob4me website.
* SCREEN_SIZE_SELECTOR: A CSSselector for the screen size element on the Mob4me website.
* PRICE_SELECTOR: A CSS selector for the price element on the Mob4me website.
* BATTERY_SELECTOR: A CSS selector for the battery element on the Mob4me website.
* BACK_CAM_SELECTOR: A CSS selector for the back camera element on the Mob4me website.
* RAM_NAME_SELECTOR: A CSS selector for the RAM name element on the Mob4me website.
* FRONT_CAM_SELECTOR: A CSS selector for the front camera element on the Mob4me website.
* MEMORY_NAME_SELECTOR: A CSS selector for the memory name element on the Mob4me website.
<br>

You can also modify the following values in the mob4me_scraper.py file:

* save_data_to_excel(dataframe, file_name): The function that saves the scraped data to an Excel file. You can modify this function to save the data in a different format or location.
* scrap(brand): The function that scrapes the data for a given brand. You can modify this function to scrape additional or different data, or to scrape data from a different website.