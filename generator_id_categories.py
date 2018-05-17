import csv

"""
File: generator_category.py
Author: Rafal Marguzewicz
Email: info@pceuropa.net
Github: https://github.com/pceuropa/generator-category-id-and-parent-id
Description: Get list of categories and return name, id, parent_id
"""


class CsvRead(object):

    filename_csv = ''

    def __init__(self, filename=None):
        self.filename_csv = filename

    def toList(self):
        try:
            with open(self.filename_csv, newline='') as csvfile:
                csv_list = csv.reader(csvfile, delimiter=',', quotechar='"')

                for row in csv_list:
                    yield row[0]

        except Exception as e:
            print(e)

    def save(self, cat):
        """
        save list to csv
        :cat: list
        """
        with open(self.filename_csv, 'w', newline='') as csvfile:
            csv_file = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_file.writerow(['name', 'id', 'parent_id'])
            for row in cat:
                csv_file.writerow(row)


def generatorIDCategory(list_categories):
    """name, id, parent_id"""
    x = 1
    data = []
    parent = [0, 0, 0, 0, 0, 0]

    for i in list_categories:
        lc = i.split("/")
        pointer = len(lc[:-1])
        data = [lc[-1], x]
        parent[pointer] = data[1]

        if pointer:
            data.append(parent[pointer - 1])

        x += 1
        yield data


if __name__ == "__main__":
    c = CsvRead('csv/categories_example.csv').toList()
    categories = generatorIDCategory(c)
    CsvRead('csv/export_categories.csv').save(categories)
