from selenium import webdriver
from Product import Product


def getProductInfo(product):
    image = product.find_element_by_tag_name('meta')
    thumbnail = image.get_attribute('content')
    nameTag = product.find_element_by_class_name('goods-name')
    name = nameTag.text
    prices = []
    priceList = product.find_elements_by_class_name('price')
    for price in priceList:
        num = price.find_element_by_class_name('num')
        prices.append(num.text)
    return Product(name, thumbnail, prices[0], prices[1])


storeURL = "https://jentestore.com/goods/list?gender=0003&category[]=00030004&brand[]=0026&per=100000&page=1&sort=regist"

driver = webdriver.Chrome(executable_path='./chromedriver_88')
driver.get(storeURL)
driver.implicitly_wait(time_to_wait=5)

productList = driver.find_elements_by_xpath(
    '//li[@class="jt-goods-list-elem"]')

for product in productList:
    getProductInfo(product)

driver.close()
