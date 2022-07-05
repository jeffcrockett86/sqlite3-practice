# in this file i will be using find and replace to make all this shit hard to read lmao
# maybe i'll get rid of the original if i'm feeling extra devilish muahahaha

#from Table import M as FUCK
#from Table import Table as t
# from Cell import Cell as SHIT
# from Row import Row as GODDAMMIT
from Col import Col

class M:
    def __init__(self, name):
        self.name = name
        self.rows = []
        self.words = []
        # self.content = []
        self.cols = []
        self.guess = []
        # self.cells = []
        # self.parent = []
        # self.children = []
        self.html = '<m> </m>'

    def __getitem__(self, item):
        return self.rows[item]

    # def rows(self):
    #     return self.rows
    @property
    def cells(self):
        return [cell for row in self.rows for cell in row]


    def make_cols(self):
        self.cols = [Col(name = self.rows[0][i], parent=self) for i in range(len(self.rows))]
        return self


    @property
    def length(self):
        return len(self.rows)

    def contains(self, el):
        return self.cell




    # def cols(self):
    #     return self.cols

    def add_row(self, row):
        self.rows.append(row)
        return self

    def add_col(self, col):
        self.cols.append(col)
        return self
