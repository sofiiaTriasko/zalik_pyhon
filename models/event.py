import datetime
from typing import List, Any

class Event:
    events = []

    def __init__(self, name: str, date: datetime.date, venue: str, price: float):
        self.name = name
        self.date = date
        self.venue = venue
        self.price = price
        self.reservations = 0
        self.capacity = 100  # Default capacity for all events
        Event.events.append(self)

    def book_seat(self, number_of_seats: int):
        if self.reservations + number_of_seats <= self.capacity:
            self.reservations += number_of_seats
            print(f"Reserved {number_of_seats} seats for {self.name}")
        else:
            print(f"Cannot reserve {number_of_seats} seats for {self.name}. Not enough available seats.")

    def update_event(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def delete_event(cls, event):
        cls.events.remove(event)

    @staticmethod
    def find_event(name: str):
        for event in Event.events:
            if event.name == name:
                return event
        return None

    @classmethod
    def search_events(cls, **criteria: Any):
        results = cls.events
        for key, value in criteria.items():
            if key == "artists":
                results = [event for event in results if isinstance(event, Concert) and value in event.artists]
            else:
                results = [event for event in results if getattr(event, key, None) == value]
        return results

    @classmethod
    def sort_events(cls, attribute: str):
        return sorted(cls.events, key=lambda x: getattr(x, attribute))

    def __eq__(self, other):
        if isinstance(other, Event):
            return self.name == other.name and self.date == other.date and self.venue == other.venue and self.price == other.price
        return False

    def __hash__(self):
        return hash((self.name, self.date, self.venue, self.price))

    def __repr__(self):
        return f"Event({self.name}, {self.date}, {self.venue}, {self.price})"

class Concert(Event):
    def __init__(self, name: str, date: datetime.date, venue: str, price: float, genre: str, artists: List[str]):
        super().__init__(name, date, venue, price)
        self.genre = genre
        self.artists = artists

    def __eq__(self, other):
        if isinstance(other, Concert) and super().__eq__(other):
            return self.genre == other.genre and self.artists == other.artists
        return False

    def __hash__(self):
        return hash((super().__hash__(), self.genre, tuple(self.artists)))

    def __repr__(self):
        return f"Concert({self.name}, {self.genre}, {self.artists})"

class Festival(Event):
    def __init__(self, name: str, date: datetime.date, venue: str, price: float, genre: str, artists: List[str]):
        super().__init__(name, date, venue, price)
        self.genre = genre
        self.artists = artists
        self.concerts = []

    def add_concert(self, concert: Concert):
        self.concerts.append(concert)
        print(f"Added concert {concert.name} to festival {self.name}")

    def __eq__(self, other):
        if isinstance(other, Festival) and super().__eq__(other):
            return self.genre == other.genre and self.artists == other.artists and self.concerts == other.concerts
        return False

    def __hash__(self):
        return hash((super().__hash__(), self.genre, tuple(self.artists), tuple(self.concerts)))

    def __repr__(self):
        return f"Festival({self.name}, {self.genre}, Concerts: {[concert.name for concert in self.concerts]})"
