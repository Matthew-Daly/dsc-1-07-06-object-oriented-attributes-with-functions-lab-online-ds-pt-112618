class School:
    def __init__(self, name=None, roster={}):
        self.name = name
        self.roster = roster
        
    def add_student(self, name, grade):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = [name]
        return self.roster

    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        sorted_dict = self.roster.copy()
        for key in sorted_dict:
            sorted_dict[key].sort()
        return sorted_dict    
        
                
        
        
        
