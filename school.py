class School:
    
    def __init__(self, name):
        self.name = name
        self._roster = {}
        
    def roster(self):
        return self._roster

    def add_student(self,name,grade):
        if grade in self._roster:
            self._roster[grade].append(name)
        else:
            self._roster[grade]=[name]
        return self._roster
    
    def grade(self,grade):
        return self._roster[grade]
    
    def sort_roster(self):
        new_dict={}
        for key in self._roster:
            new_dict[key]=sorted(self._roster[key])
        return new_dict