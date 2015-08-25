class Product:
    def __init__(self, id, title, popularity, quantity, shop):
        self.id = id
        self.title = title
        self.popularity = popularity
        self.quantity = quantity
        self.shop = shop

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'popularity': self.popularity,
            'quantity': self.quantity,
            'shop': self.shop.serialize()
        }
