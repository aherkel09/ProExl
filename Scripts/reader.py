import csv

class Reader():
    def __init__(self):
        self.data = "Data/db_items.csv"

    def get_headers(self):
        with open(self.data, 'r') as csv_in:
            reader = csv.reader(csv_in)
            return next(reader)

if __name__ == '__main__':
    reader = Reader()
    print(reader.get_headers())
