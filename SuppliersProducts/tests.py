from django.test import TestCase
import unittest
from SuppliersProducts.laskin import plus, plus_complicated

# TDD - Test Driven Development, ensin testi toiminnallisuuksille ja sitten vasta toteutus
# def pitää alkaa test sanalla. Testi ajetaan komennolla python manage.py test
class TestPlus(TestCase):
    def test_plus(self):
        self.assertEqual(plus(1, 2), 3)
        self.assertEqual(plus(0, 0), 0)
        self.assertEqual(plus(-1, -1), -2)

    def test_plus_complicated(self):
        self.assertEqual(plus_complicated(7, 2), 9)
        self.assertEqual(plus_complicated(2, 8), 8)

    @unittest.expectedFailure
    def test_plus_should_fail(self):
        self.assertEqual(plus('7', 2), 9) # stringi 7 ja int 2 ei ole sama asia
        