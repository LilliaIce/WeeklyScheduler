"""Module with the Day class"""

class Day:
    def __init__(self, name):
        """When a Day object is created, creates uncomplete and complete
        task lists and gets the object's name."""
        self.uncompleteTasks = []
        self.completeTasks = []
        self.name = name


    def __str__(self):
        """Names the Day object a title-cased phrase."""
        return self.name
    

    def getTasks(self):
        list = []
        for item in self.uncompleteTasks:
            list.append(item)
        return list


    def addTask(self, task):
        """Adds a task to the uncomplete list."""
        if task.isspace():
            raise NameError("Task can't be whitespace")
        elif task == False:
            raise NameError("Task can't be empty")
        elif task in self.uncompleteTasks:
            raise NameError("Task can't be in uncomplete list")
        elif task in self.completeTasks:
            raise NameError("Task can't be in complete list")
        self.uncompleteTasks.append(task)


    def removeTask(self, task):
        """Removes a task from the uncomplete list."""
        if task.isspace():
            raise NameError("Task can't be whitespace")
        elif task == False:
            raise NameError("Task can't be empty")
        elif task not in self.uncompleteTasks:
            raise NameError("Task must be in uncomplete list")
        self.uncompleteTasks.remove(task)


    def moveTask(self, task, newDay):
        """Moves a task to another Day's uncomplete list"""
        if task.isspace():
            raise NameError("Task can't be whitespace")
        # task must be in uncomplete list
        elif task not in newDay.uncompleteTasks:
            raise NameError("Task can't be in uncomplete list")
        # task must not be in newDay's uncomplete list
        elif task in newDay.uncompleteTasks:
            raise NameError("Task can't be in uncomplete list")
        newDay.uncompleteTasks.append(task)
        self.uncompleteTasks.remove(task)


    def toggleTask(self, task):
        """Toggles a task as complete or uncomplete depending on which list
        it was in prior"""
        if task.isspace():
            raise NameError("Task can't be whitespace")
        elif task in self.uncompleteTasks:
            # task must be in uncomplete list
            if task in self._completeTasks:
                raise NameError("Task can't be in complete list")
            self.completeTasks.append(task)
            self.uncompleteTasks.remove(task)
        elif task in self.completeTasks:
            if task in self.uncompleteTasks:
                raise NameError("Task can't be in uncomplete list")
            self.uncompleteTasks.append(task)
            self.completeTasks.remove(task)