from selenium import webdriver


def getProductInfo(product):
    image = product.find_element_by_tag_name('meta')
    thumbnail = image.get_attribute('content')
    prices = []
    priceList = product.find_elements_by_class_name('price')
    for price in priceList:
        num = price.find_elements_by_class_name('num')
        prices.append(num.text)
    print(prices)
    # thumbnail = product.find_element_by_tag_name('img').get_attribute('src')
    # originalPrice = info.find_elements_by_xpath('')
    # originalPrice = product.find_elements_by_class_name('price-sty1').find_elements_by_class_name('num').text
    # discountPrice = product.find_elements_by_class_name('price').find_elements_by_class_name('num').text
    # name = product.find_elements_by_class_name('goods-name ellipsis').text
    return


storeURL = "https://jentestore.com/goods/list?gender=0003&category[]=00030004&brand[]=0026&per=20&page=1&sort=regist"

driver = webdriver.Chrome(executable_path='./chromedriver_88')
driver.get(storeURL)
driver.implicitly_wait(time_to_wait=5)

productList = driver.find_elements_by_xpath(
    '//li[@class="jt-goods-list-elem"]')

for product in productList:
    getProductInfo(product)

driver.close()
