from typing import List, TypeVar, Any, Optional
from models.event import Event, Concert, Festival

T = TypeVar('T', bound=Event)

class EventService:
    @staticmethod
    def find_event(events: List[T], name: str) -> Optional[T]:
        for event in events:
            if event.name == name:
                return event
        return None

    @staticmethod
    def search_events(events: List[T], **criteria: Any) -> List[T]:
        results = events
        for key, value in criteria.items():
            if key == "artists":
                results = [event for event in results if isinstance(event, Concert) and value in event.artists]
            else:
                results = [event for event in results if getattr(event, key, None) == value]
        return results

    @staticmethod
    def sort_events(events: List[T], attribute: str) -> List[T]:
        return sorted(events, key=lambda event: getattr(event, attribute, None))

    @staticmethod
    def create_event(event_type: str, *args, **kwargs) -> T:
        if event_type.lower() == 'concert':
            return Concert(*args, **kwargs)
        elif event_type.lower() == 'festival':
            return Festival(*args, **kwargs)
        else:
            return Event(*args, **kwargs)

    @staticmethod
    def update_event(event: T, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(event, key, value)

    @staticmethod
    def delete_event(events: List[T], event: T) -> None:
        events.remove(event)
