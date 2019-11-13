import unittest
from duplicate_hunter_two import DuplicateHunter

class TestDuplicateHunter(unittest.TestCase):
    def create_hunter(self):
        hunter = DuplicateHunter()
        return hunter

    def get_total_items(self, hunter):
        total_items = 0
        for u in hunter.unique:
            total_items += len(hunter.unique[u])
        for d in hunter.duplicates:
            total_items += len(hunter.duplicates[d])

        return total_items

    def list_codes(self, data):
        codes = []
        
        for d in data:
            codes += d
            print(codes)
            break

        return codes

    def test_find_duplicates(self):
        hunter = self.create_hunter()
        hunter.find_duplicates()
        total_items = self.get_total_items(hunter)
        
        self.assertTrue(total_items == len(hunter.data))

    def test_acquire_targets(self):
        hunter = self.create_hunter()
        hunter.find_duplicates()
        initial_items = self.get_total_items(hunter)
        
        hunter.flag_or_resolve()
        hunter.eliminate_hardcodes()
        final_items = self.get_total_items(hunter)

        print(initial_items, final_items)
        self.assertTrue(initial_items == final_items)

    def test_results(self):
        hunter = self.create_hunter()
        hunter.acquire_targets()
        final = hunter.get_final_data()

        self.assertTrue(len(final) == len(hunter.data))
        self.assertTrue(self.list_codes(final) == self.list_codes(hunter.data))

        
        
if __name__ == '__main__':
    unittest.main()

