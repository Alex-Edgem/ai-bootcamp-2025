class Country:
    def __init__(self, name):
        self.name=name
        self.region={}

    def add(self, obj):
        self.region[obj]

    @property
    def pop(self):
        """The total population of this country"""


class Region:
    def __init__(self, name):
        self.name = name


class City:
    """A city"""

    def __init__(self, name, pop=None):
        ...


