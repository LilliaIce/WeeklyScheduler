""" Module with the Project class """

class Project():
    def __init__(self, name):
        """When a Project object is created, creates a task list and
        sets the object's name """
        self.tasks = []
        self.name = name


    def __str__(self):
        """ Names the Project object """
        return self.name
    

    def testString(self, task):
        """Tests strings"""
        i = 0
        while i < len(self.tasks):
            if task.lower().strip() in self.tasks[i].lower().strip():
                return self.tasks[i]
            i = i + 1


    def getTasks(self):
        """Returns a list of tasks"""
        list = []
        for item in self.tasks:
            list.append(item)
        return list


    def addTask(self, task):
        """Adds a task to the task list."""
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
        """Removes a task from the task list."""
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


    def moveTask(self, task, newProject):
        """ Moves a task to another Project's task list """
        if task in newProject.tasks:
            raise NameError("Task must not be in the new Project's task list")
        else:
            try:
                task = self.testString(task)
            except:
                raise NameError("Task must be in the Project's task list")
        newProject.tasks.append(task)
        self.tasks.remove(task)


    def toggleTask(self, task):
        """ Toggles a task as complete or uncomplete depending on which
        it was prior """
        if task.isspace():
            raise NameError("Task can't be whitespace")
        else:
            try:
                task = self.testString(task)
            except:
                raise NameError("Task must be in the day's task list.")
            # removes the first two letters (- ) from the task
            if task[0] == "-":
                self.tasks[self.tasks.index(task)] = task[2:] 
            # adds two letters (- ) to the beginning of the task
            else:
                self.tasks[self.tasks.index(task)] = "- " + task
                