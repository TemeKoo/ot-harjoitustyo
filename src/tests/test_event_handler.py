import unittest

import pygame
from logic.event_handler import EventHandler


class DummyEvent():
    def __init__(self, event_type):
        self.type = event_type


class DummyEventQueue():
    def __init__(self):
        self.events = []

    def post(self, event):
        self.events.append(DummyEvent(event))

    def get(self):
        return self.events
    
    class Event():
        def __init__(self, *args, **kwargs):
            pass


class DummyField():
    def update(self, **kwargs):
        pass


class TestEventHandler(unittest.TestCase):
    def setUp(self):
        self.event_queue = DummyEventQueue()
        pygame.event = self.event_queue
        self.scene_data = {
            "field": DummyField()
        }
        self.event_handler = EventHandler()

    def test_event_handler_is_created(self):
        self.assertNotEqual(self.event_handler, None)

    def test_handler_returns_true(self):
        self.assertEqual(self.event_handler.handle_events(self.scene_data), True)

    def test_quit_works(self):
        self.event_queue.post(pygame.QUIT)
        self.assertEqual(self.event_handler.handle_events(self.scene_data), False)
