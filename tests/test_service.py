import unittest
import datetime
from models.event import Event, Concert, Festival
from services.event_service import EventService

class TestEventService(unittest.TestCase):

    def setUp(self):
        Event.events = []

        self.concert1 = Concert("Rock Night", datetime.date(2024, 6, 20), "Main Hall", 50, "Rock", ["Band A"])
        self.concert2 = Concert("Jazz Evening", datetime.date(2024, 6, 21), "Open Ground", 70, "Jazz", ["Artist B"])
        self.festival = Festival("Summer Fest", datetime.date(2024, 7, 1), "Open Ground", 100, "Various", ["Band C", "Artist D"])

    def test_create_event(self):
        new_event = EventService.create_event('concert', "Pop Concert", datetime.date(2024, 8, 1), "Main Hall", 60, "Pop", ["Singer E"])
        self.assertIsInstance(new_event, Concert)
        self.assertEqual(new_event.name, "Pop Concert")

    def test_update_event(self):
        EventService.update_event(self.concert1, name="Rock and Roll Night")
        self.assertEqual(self.concert1.name, "Rock and Roll Night")

    def test_delete_event(self):
        EventService.delete_event(Event.events, self.concert1)
        self.assertNotIn(self.concert1, Event.events)

    def test_find_event(self):
        event = EventService.find_event(Event.events, "Jazz Evening")
        self.assertEqual(event, self.concert2)

    def test_search_events(self):
        results = EventService.search_events(Event.events, genre="Jazz")
        self.assertIn(self.concert2, results)
        self.assertNotIn(self.concert1, results)

    def test_sort_events(self):
        sorted_events = EventService.sort_events(Event.events, "price")
        self.assertEqual(sorted_events[0], self.concert1)
        self.assertEqual(sorted_events[1], self.concert2)
        self.assertEqual(sorted_events[2], self.festival)

    def test_book_seat(self):
        self.concert1.book_seat(50)
        self.assertEqual(self.concert1.reservations, 50)

    def test_book_seat_over_capacity(self):
        self.concert1.book_seat(150)
        self.assertNotEqual(self.concert1.reservations, 150)

if __name__ == '__main__':
    unittest.main(verbosity=2)
