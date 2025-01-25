class Country:
    def __init__(self, name):
        self.name = name
        self.region = {}
        self.city={}


    def add(self, obj):
        self.region = obj.name

class Region:
    def __init__(self, name):
        self.name = name

class City:
    """A city"""

    def __init__(self, name, pop=None):
        self.
italy=Country("Italy")
sicily=Region("Sicily")
italy.add(sicily)
print(italy.name, sicily.name, italy.region)