from unittest import TestCase


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:

    __id_count = -1

    def __get_next_id(self):
        PersonFactory.__id_count += 1
        return PersonFactory.__id_count

    def create_person(self, name):
        return Person(PersonFactory.__get_next_id(self), name)


class Evaluate(TestCase):
    def test_exercise(self):
        pf = PersonFactory()

        p1 = pf.create_person('Chris')
        self.assertEqual(p1.name, 'Chris')
        self.assertEqual(p1.id, 0)

        p2 = pf.create_person('Sarah')
        self.assertEqual(p2.id, 1)
