URL = 'https://mob4me.com/' 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
}

BRANDS = ['vivo','realme'] 
# selectors

BACK_CAM_SELECTOR = '#product_icons > li:nth-child(4)'

SCREEN_SIZE_SELECTOR = '#product_icons > li:nth-child(2)'

BATTERY_SELECTOR = '#product_icons > li:nth-child(6)'

PRICE_SELECTOR = 'body > div.container > div > div.col-md-8.col-12 > section:nth-child(2) > div.row.product-titlecontent > div:nth-child(3) > div:nth-child(1) > h3'

MEMORY_NAME_SELECTOR = 'td:contains("الذاكرة الداخلية")'

RAM_NAME_SELECTOR = 'td:contains("الرامات")'

FRONT_CAM_SELECTOR = 'td:contains("موصفات الكاميرة الامامية")'

PHONE_ANCHORS_SELECTOR = 'body > div.container > div > div > section > div:nth-child(2) > div > a'

NEXT_BUTTON_SELECTOR = 'a:contains("التالي")'