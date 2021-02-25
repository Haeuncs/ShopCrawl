# Product 객체를 excel 로 write
import pandas as pd
import numpy as np


class FileManager:
    def __init__(self, storeName, products):
        npProduct = np.array(products)
        self.productDataFrame = pd.DataFrame(npProduct)
        self.storeName = storeName

    def save(self):
        filePath = './CrawlData/{}.csv'.format(self.storeName)
        self.productDataFrame.to_csv(filePath, index=False)
