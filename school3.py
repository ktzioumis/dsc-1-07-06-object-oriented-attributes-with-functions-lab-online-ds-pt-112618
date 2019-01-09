class School:
    
    def __init__(self, name):
        self.name = name
        self._roster = {}
        
    def roster(self):
        return self._roster

    def add_student(self,name,grade):
        self.roster[grade].append(name)