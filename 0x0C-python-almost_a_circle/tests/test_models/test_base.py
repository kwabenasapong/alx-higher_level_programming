#!/usr/bin/python3
import unittest

from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        a = Base()
        b = Base()
        c = Base(12)
        d = Base()
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)
        self.assertEqual(c.id, 12)
        self.assertEqual(d.id, 3)

if __name__ == '__main__':
    unittest.main()
