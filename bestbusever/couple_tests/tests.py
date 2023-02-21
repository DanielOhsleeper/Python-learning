import unittest
from bestbusever.backend.bus_route import BusRoute
from bestbusever.frontend.menu import Menu
class TestingBusInput(unittest.TestCase):
    def setUp(self):
        self.busroute = BusRoute(line_number=11, origin="Hadera", destination="Gedera",
                                 list_of_stops=["Afula", "Eilat", "Mamila"])
        self.menu = Menu()

    def test_method1(self):
        result = self.busroute.get_ride()
        self.assertEqual(result, {})

    def test_method2(self):
        self.busroute.search_by_stops()
        self.assertNotIn("Hadera", self.busroute.search_by_stops())

    def test_method3(self):
        self.menu.main_menu()
        self.assertRaises(Exception)


if __name__ == '__main__':
    unittest.main()
