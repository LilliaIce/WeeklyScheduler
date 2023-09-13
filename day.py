"""Module with the Day class"""

class Day:
    def __init__(self, name):
        """When a Day object is created, creates uncomplete and complete
        task lists and gets the object's name."""
        self.tasks = []
        self.name = name


    def __str__(self):
        """Names the Day object a title-cased phrase."""
        return self.name
    

    def testString(self, task):
        """Tests strings"""
        i = 0
        while i < len(self.tasks):
            if task in self.tasks[i]:
                return self.tasks[i]
            i = i + 1


    def addProject():
        pass


    def removeProject():
        pass


    def getTasks(self):
        list = []
        for item in self.tasks:
            list.append(item)
        return list


    def addTask(self, task):
        """Adds a task to the uncomplete list."""
        if task.isspace():
            raise NameError("Task can't be whitespace")
        elif "-" in task:
            raise NameError("Task can't contain '-'")
        elif task == False:
            raise NameError("Task can't be empty")
        elif task in self.tasks:
            raise NameError("Task can't be in the task list")
        self.tasks.append(task)


    def removeTask(self, task):
        """Removes a task from the uncomplete list."""
        if task.isspace():
            raise NameError("Task can't be whitespace")
        elif task == False:
            raise NameError("Task can't be empty")
        else:
            try:
                task = self.testString(task)
            except:
                raise NameError("Task must be in the task list")
        self.tasks.remove(task)


    def moveTask(self, task, newDay):
        """Moves a task to another Day's uncomplete list"""
        if task.isspace():
            raise NameError("Task can't be whitespace")
        elif task in newDay.tasks:
            raise NameError("Task can't be in the new day's task list")
        else:
            try:
                task = self.testString(task)
            except:
                raise NameError("Task must be in the day's task list")
        newDay.tasks.append(task)
        self.tasks.remove(task)


    def toggleTask(self, task):
        """Toggles a task as complete or uncomplete depending on which
        it was in prior"""
        if task.isspace():
            raise NameError("Task can't be whitespace")
        else:
            try:
                task = self.testString(task)
            except:
                raise NameError("Task must be in the day's task list.")
            if task[0] == "-":
                self.tasks[self.tasks.index(task)] = task[2:] 
            else:
                self.tasks[self.tasks.index(task)] = "- " + task