import unittest
from restaurant import RestaurantSystem

class TestRestaurantSystem(unittest.TestCase):

    def setUp(self):
        self.restaurant = RestaurantSystem("Test Restaurant", 10, 20)

    def test_person_enters(self):
        self.restaurant.person_entered()
        self.assertEqual(self.restaurant.occupied, 1)

    def test_capacity_limit(self):
        self.restaurant.set_occupancy(10)
        with self.assertRaises(ValueError):
            self.restaurant.person_entered()

    def test_empty_restaurant(self):
        with self.assertRaises(ValueError):
            self.restaurant.person_left()

    def test_queue(self):
        self.restaurant.add_queue_group()
        self.restaurant.add_queue_group()
        self.assertEqual(self.restaurant.queue_groups, 2)

    def test_wait_time(self):
        self.restaurant.set_queue(3)
        self.assertEqual(self.restaurant.estimated_wait(), 60)

    def test_no_wait(self):
        self.assertEqual(self.restaurant.estimated_wait(), 0)

if __name__ == "__main__":
    unittest.main()
