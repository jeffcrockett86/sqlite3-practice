class Col():

    def __init__(self, name, parent):
        self.name = name
        self.cells = []
        self.parent = parent

    # def get_col(col):
    #     pass

    def __getitem__(self, item):
        return self.cells[item]
