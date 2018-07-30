class Student():
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_scores(self):
        return self.scores

ds = Student("dongshuai",20,[71,87,90])
print(ds.get_name())
print(ds.get_age())
print(ds.get_scores())
