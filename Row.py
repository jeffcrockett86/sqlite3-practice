class Row:

    def __init__(self, name, parent):
        self.name = name
        self.cells = []
        self.html = '<tr> </tr>'
        self.parent = parent


    # def name(self, name):
    #     self.name = name


    def __getitem__(self, item):
        return self.cells[item]

    def add_cell(self, cell):
        self.cells.append(cell)
        return self

    @property
    def length(self):
        return len(self.cells)

    @property
    def id(self):
        return hex('0x' + str(self.split('x')))
