class Cell:

    def __init__(self, name, parent):
        self.tables = []
        self.name = name
        self.html = "<td> </td>"
        self.parent = parent
        self.content = []
        self.is_yellow = None
        self.is_green = None
        self.is_black = None
        self.pos = None
        # return self

    def add_content(self, content):
        self.content.append(content)
        return self


    def __getitem__(self, item):
        return self.tables[item]
