"""Module with the Day class"""

class Day:
    def __init__(self, name):
        """ When a Day object is created, creates a projects list. """
        self.projects = []
        self.name = name


    def __str__(self):
        """ Names the Day object """
        return self.name


    def addProject(self, project):
        """Adds a task to the task list."""
        self.projects.append(project)


    def removeProject(self, project):
        """Removes a project from the project list."""
        self.projects.remove(project)


    def getProjects(self):
        list = []
        for i in self.projects:
            list.append(i)
        return list
