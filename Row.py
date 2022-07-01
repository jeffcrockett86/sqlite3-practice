from Table import Table

class Row(Table):

    def __init__(self, rows, cols):
        super(rows, cols)
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)
        return self
