from unittest import TestCase
from city_data.city import City


class TestCity(TestCase):

    # init function tests
    def setUp(self):
        self.city = City("Chicago")

    def test_mangled_attributes(self):
        self.assertEqual("Chicago", self.city._City__name)
        self.assertEqual(0, self.city._City__infected)
        self.assertEqual(0, self.city._City__recovered)
        self.assertEqual(0, self.city._City__deaths)

    # name property test
    def test_name(self):
        self.assertEqual("Chicago", self.city.name)

    # infected property and setter tests
    def test_infected_init(self):
        self.assertEqual(0, self.city.infected)

    def test_infected_setter(self):
        self.city.infected = 100
        self.assertEqual(100, self.city.infected)

    def test_infected_setter_fail(self):
        with self.assertRaises(TypeError):
             self.city.infected = '100'

    # recovered property and setter tests
    def test_recovered_init(self):
        self.assertEqual(0, self.city.recovered)

    def test_recovered_setter(self):
        self.city.recovered = 85
        self.assertEqual(85, self.city.recovered)

    def test_recovered_fail(self):
        with self.assertRaises(TypeError):
             self.city.recovered = 98.5

    # deaths property and setter tests
    def test_deaths_init(self):
       self.assertEqual(0, self.city.deaths)

    def test_deaths_setter(self):
        self.city.deaths = 3
        self.assertEqual(3, self.city.deaths)

    def test_deaths_fail(self):
        with self.assertRaises(TypeError):
             self.city.deaths = []

    # __eq__ tests
    def test_equals(self):
        city1 = City("Chicago")
        self.assertTrue(city1 == self.city)

    def test_equals_none(self):
        self.assertFalse(self.city is None)

    def test_equals_diff_objs(self):
        self.assertFalse(self.city == 'Chicago')

    # __str__ tests
    def test_str(self):
        self.assertEqual('Name: Chicago\nInfected: 0, Recovered: 0, Deaths: 0', self.city.__str__())
