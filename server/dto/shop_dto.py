class Shop:
    def __init__(self, id, lat, long):
        self.id = id
        self.lat = lat
        self.long = long

    def serialize(self):
        return {
            'id': self.id,
            'lat': self.lat,
            'lng': self.long,
        }
