import unittest
from drop_duplicates import DuplicateHunter

class TestDropDuplicates(unittest.TestCase):
    def create_hunter(self):
        hunter = DuplicateHunter()
        return hunter

    def test_find_duplicates(self):
        hunter = self.create_hunter()
        hunter.find_duplicates()
        self.assertTrue(len(hunter.item_descriptions) > 0)
        self.assertTrue(len(hunter.duplicate_descriptions) > 0)
        self.assertTrue(list(hunter.duplicate_descriptions.keys())[0] in hunter.item_descriptions)

    def test_match_values(self):
        hunter = self.create_hunter()
        hunter.find_duplicates()
        hunter.match_values()
        self.assertTrue(len(hunter.flagged) > 0)
        self.assertTrue(len(hunter.safe_to_remove) > 0)

if __name__ == '__main__':
    unittest.main()

