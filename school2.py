class School:

    def __init__(self, name):
        self.name = name
        self._roster = {}

    def roster(self):
        return self._roster