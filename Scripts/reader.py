import csv

class Reader():
    def __init__(self):
        self.in_file = "Data/db_items.csv"
        self.data = self.list_data()
        self.headers = self.get_headers()

    def get_headers(self):
        with open(self.in_file, 'r') as csv_in:
            reader = csv.reader(csv_in)
            headers = next(reader)
            headers.pop(0) # remove item code
            return headers

    def list_data(self):
        with open(self.in_file, 'r') as csv_in:
            reader = csv.reader(csv_in)
            data = list(reader)
            data.pop(0) # remove item code
            return data

    def sort_by_description(self, i):
        return i[1]

    def sort_data(self):
        sorted_data = self.data.sort(key=self.sort_by_description)
        self.data = sorted_data

if __name__ == '__main__':
    reader = Reader()
    print(reader.headers)
    print(reader.data[0])
