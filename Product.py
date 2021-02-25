class Product:
    def __init__(self, name, thumbnail, price, discountPrice, number):
        self.name = name
        self.thumbnail = thumbnail
        self.price = price
        self.discountPrice = discountPrice
        self.number = number

    def getDictionary(self):
        return {
            'name': self.name,
            'thumbnail': self.thumbnail,
            'price': self.price,
            'discountPrice': self.discountPrice,
            'number': self.number
        }
