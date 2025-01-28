class Country:
    def __init__(self, name):
        self.name = name
        self.regions = []

    def add(self, region):
        self.regions.append(region)

    def __iter__(self):
        return iter(self.regions)



    # usiamo list comprehension
    @property
    def pop(self):
        return sum(city.pop for region in self for city in region)


    @property
    def most_populuous_city(self):
        most_populus = 0
        current_most_city = None
        for region in self:
            for city in region:
                if city.pop > most_populus:
                    most_populus = city.pop
                    current_most_city = city
        return current_most_city


class Region:
    def __init__(self,name):
        self.name = name
        self.cities = []

    def add(self, city):
        self.cities.append(city)

    def __iter__(self):
        return iter(self.cities)

    @property
    def pop(self):
        return sum(city.pop for city in self if city.pop is not None)



class City:
    def __init__(self, name, pop=None):
        self.name = name
        self.pop = pop

italy = Country("Italy")
sicily = Region("Sicily")
calabria = Region("Calabria")
puglia = Region("Puglia")

palermo = City("Palermo", 600_000)
catania = City("Catania", 300_000)
reggio = City("Reggio", 170_000)
gallipoli = City("Gallipoli", 1_000_000)


italy.add(sicily)
italy.add(calabria)
italy.add(puglia)

sicily.add(palermo)
sicily.add(catania)
calabria.add(reggio)
puglia.add(gallipoli)

print(italy.pop)
