class Cell:

    def __init__(self, parent, name):
        self.tables = []
        self.name = name
        self.html = "<td> </td>"
        self.parent = parent
        self.content = []
        # return self

    def add_content(self, content):
        self.content.append(content)
        return self
