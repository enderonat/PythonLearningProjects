import unittest
from cities import place_name


class CitiesTestCase(unittest.TestCase):
    """ Test for this.py """

    def test_city_country_name(self):
        formatted_city = place_name('istanbul', 'türkiye')
        self.assertEqual(formatted_city, 'Istanbul,Türkiye')

    def test_city_country_name_population(self):
        formatted_population = place_name('mardin', 'türkiye', '3000000')
        self.assertEqual(formatted_population, 'Mardin,Türkiye - Population 3000000')

    if __name__ == '__main__':
        unittest.main()
