class City:
    def __init__(self, name, infected=0, recovered=0, deaths=0):
        self.__name = name
        self.__infected = infected
        self.__recovered = recovered
        self.__deaths = deaths

    @property
    def name(self):
        return self.__name

    @property
    def infected(self):
        return self.__infected

    @infected.setter
    def infected(self, value):
        if value is None or not isinstance(value, int):
            raise TypeError("Please input an integer.")
        self.__infected = value

    @property
    def recovered(self):
        return self.__recovered

    @recovered.setter
    def recovered(self, value):
        if value is None or not isinstance(value, int):
            raise TypeError("Please input an integer.")
        self.__recovered = value

    @property
    def deaths(self):
        return self.__deaths

    @deaths.setter
    def deaths(self, value):
        if value is None or not isinstance(value, int):
            raise TypeError("Please input an integer.")
        self.__deaths = value

    def __eq__(self, other):
        if other is None or not isinstance(other, City):
            return False
        return self.__name == other.__name

    def __str__(self):
        return f"Name: {self.__name}\nInfected: {self.__infected}, Recovered: {self.__recovered}, Deaths: {self.__deaths}"


from operator import attrgetter

class Pandemic:
    def __init__(self):
        self.cities = []

    def add_city(self, city_name: str):
        for city in self.cities:
            if city.name == city_name:
                raise ValueError("City already added")

        new_city = City(city_name)
        self.cities.append(new_city)

    def edit_city(self, city_name: str, infected: int, recovered: int, deaths: int):
        for city in self.cities:
            if city.name == city_name:
                city.infected = infected
                city.recovered = recovered
                city.deaths = deaths
                return

        raise ValueError("City not in list")

    def display_city(self, city_name: str):
        for city in self.cities:
            if city.name == city_name:
                print(city)
                return

        print("City not in list")

    def display_all_city_stats(self, attribute_name: str):
        try:
            sorted_cities = sorted(self.cities, key=attrgetter(attribute_name))
            for city in sorted_cities:
                print(city)
        except AttributeError:
            print(f"Invalid attribute: {attribute_name}")