import pytest

from exercise.exercise_4_guest_list.guest_list import GuestList


class TestGuestList:

    def setup_method(self):
        self.empty_list = GuestList()
        self.full_list = GuestList()
        self.full_list.guest_list = ['Leonardo DiCario', 'Tadeusz Waluga', 'Peter Parker', 'Harry Potter']


    def test_get_guest_list_is_empty(self):  # przypadek gdy lista jest pusta
        actual = self.empty_list.get_guest_list()
        expected = 'The list is empty'

        assert actual == expected

    def test_add_list_adds_person(self):
        self.empty_list.add_guest('Leonardo DiCaprio')
        actual = self.empty_list.get_guest_list()
        expected = ['Leonardo DiCaprio']

        assert actual == expected

    def test_added_person_is_invited(self):  # test dla is_person_invited() równego True
        actual = self.full_list.is_person_invited('Peter Parker')
        expected = True

        assert actual == expected

    def test_added_person_is_not_invited(self):  # test dla is_person_invited() równego False
        actual = self.full_list.is_person_invited('Czerwony Kapturek')
        expected = False

        assert actual == expected
