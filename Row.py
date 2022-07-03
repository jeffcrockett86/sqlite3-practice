class Row:

    def __init__(self):
        self.cells = []
        self.name = '<tr> </tr>'
        self.parent = None

    # def name(self, name):
    #     self.name = name

    def add_cell(self, cell):
        self.cells.append(cell)
        return self
