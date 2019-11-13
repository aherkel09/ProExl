import unittest, csv
from writer import Writer

class TestWriter(unittest.TestCase):
    def test_create(self):
        writer = Writer()
        print(writer.out_file)
        self.assertTrue(len(writer.out_file) > 0)

    def test_write(self):
        data = [['Success', 'Failure'], [1, 0]]
        writer = Writer()
        writer.write_to_file(data)
        self.assertTrue(self.check_contents(writer.out_file, 0) == data[0])

    def check_contents(self, out_file, row_num):
        with open(out_file, 'r') as csv_out:
            reader = csv.reader(csv_out)
            contents = None
            reader_row = 0
            while (reader_row <= row_num):
                contents = next(reader)
                reader_row += 1
            print(contents)
            return contents

if __name__ == '__main__':
    unittest.main()
