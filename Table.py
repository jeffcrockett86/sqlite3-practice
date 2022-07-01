#from Table import Table
#>>> from Table import Table as t
# from Cell import Cell
# from Row import Row

class Table:
    def __init__():
        # self.name = name
        self.rows = []
        # self.content = []
        self.cols = []
        self.cells = []
        self.parent = []
        self.children = []
        # self.html = f'<table>{self.__repr__()}</table>'



    def rows(self):
        return self.rows

    def cols(self):
        return self.cols

    def add_row(self, row):
        self.rows.append(row)
        return self

    def add_col(self, col):
        self.cols.append(col)
        return self
