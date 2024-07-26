"""
2. Create  proper member variables inside the task if required and use them when necessary .
"""

class Task:
    def inite(self):
        self.Description = ""

    def set_description(self,description):
        self.Description =description

    def display(self):
        print("Complete  Task : ", self.Description)


Venkat = Task()
Venkat.set_description("Finish the Assignment")
Venkat.display()
