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
            
            return headers

    def list_data(self):
        with open(self.in_file, 'r') as csv_in:
            reader = csv.reader(csv_in)
            data = list(reader)
            data.pop(0) # remove headers
            
            return data

if __name__ == '__main__':
    reader = Reader()
    print(reader.headers)

    index = 0
    while index < 11:
        print(reader.data[index])
        index += 1
