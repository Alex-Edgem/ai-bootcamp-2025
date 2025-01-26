class Country:
    def __init__(self, name):
        self.name = name
        self.regions = []

    def add(self, regionobject):
        self.regions.append(regionobject)

    # @property
    # def pop(self):
    #     """The total population of this country"""
    #     countpop = 0
    #     for region in self.regions:
    #         for city in region:
    #             countpop += city.pop
    #     return countpop

    #@property
    def most_populuous_city(self):
        """The most_populuous_city name"""
        most_populous = None
        max_population = 0

        for region in self.regions:
            for city in region.citys:
                if city.pop > max_population:
                    most_populous = city
                    max_population = city.pop

        if  most_populous:
            return most_populous.name
        else:
            return None


class Region:
    def __init__(self, name):
        self.name = name
        self.citys = []

    def add(self, cityobject):
        self.citys.append(cityobject)

    def __str__(self):
        pass

    @property
    def pop(self):
        """The total population of this Region"""
        countpop = 0
        for c in self.citys:
            countpop += c.pop
        return  countpop

class City:
    """A city"""
    def __init__(self, name, pop=None):
        self.name = name
        self.pop = pop

    def __str__(self):
        pass



italy = Country("Italy")

assert italy.name == "Italy"

sicily = Region("Sicily")
italy.add(sicily)

sicily.add(City("Catania", pop=300_000))
sicily.add(City("Palermo", pop=600_000))


print(italy.most_populuous_city())