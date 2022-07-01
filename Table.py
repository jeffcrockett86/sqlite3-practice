#from Table import Table
#>>> from Table import Table as t

class Table:
    def __init__(self):
        self.rows = []
        self.cols = []
        self.cells = []
        self.html = ''

    def rows(self):
        return self.rows

    def cols(self):
        return self.cols

    def add_row(self, row):
        self.rows.append(row)
        return self.rows

    def add_col(self, col):
        self.cols.append(col)
        return self.cols
