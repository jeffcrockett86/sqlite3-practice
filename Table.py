#from Table import Table
#>>> from Table import Table as t
# from Cell import Cell
# from Row import Row
from Col import Col

class Table:
    def __init__(self):
        # self.name = name
        self.rows = []
        # self.content = []
        self.cols = []
        # self.cells = []
        # self.parent = []
        # self.children = []
        self.html = '<table> </table>'

    def __getitem__(self, item):
        return self.rows[item]

    # def rows(self):
    #     return self.rows
    @property
    def cells(self):
        return [cell for row in self.rows for cell in row]


    def make_cols(self):
        self.cols = [Col(name = self.rows[0][i], parent=self.rows[i]) for i in range(len(self.rows))]
        return self


    @property
    def length(self):
        return len(self.rows)




    # def cols(self):
    #     return self.cols

    def add_row(self, row):
        self.rows.append(row)
        return self

    def add_col(self, col):
        self.cols.append(col)
        return self
