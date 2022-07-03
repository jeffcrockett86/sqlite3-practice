class Cell:

    def __init__(self, parent):
        self.tables = []
        self.name = ''
        self.html = "<td> </td>"
        self.parent = parent
        # return self

    def add_content(self, content):
        self.content.append(content)
        return self
