from models.event import Event, Concert, Festival
from services.event_service import EventService

def main():
    # Create some events
    concert = Concert("Classic Night", "2023-06-15", "City Hall", 80.0, "Classical", ["Orchestra"])
    festival = Festival("Summer Fest", "2023-07-20", "Beachside", 50.0, "Mixed", ["DJ Max", "Pop Stars"])

    # Manage events
    concert.book_seat(50)
    festival.add_concert(concert)
    print(f"Events after booking and adding: {Event.events}")

    # Search and sort
    events_sorted = EventService.sort_events(Event.events, 'name')
    print(f"Sorted Events: {events_sorted}")

if __name__ == '__main__':
    main()
