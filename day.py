"""Module with the Day class"""

class Day:
    def __init__(self, name):
        """ When a Day object is created, creates a projects list. """
        self.projects = []
        for i in name:
            self.addProject(i)
        self.name = name


    def __str__(self):
        """ Names the Day object """
        return self.name


    def testString(self, project):
        """Tests strings"""
        i = 0
        projects = self.getStrProjects()
        while i < len(projects):
            if project.lower().strip() in projects[i].lower().strip():
                return self.projects[i]
            i = i + 1


    def addProject(self, project):
        """Adds a task to the task list."""
        self.projects.append(project)


    def removeProject(self, project):
        """ Removes a project from the project list. """
        self.projects.remove(project)


    def moveProject(self, project, newDay):
        """ Moves a project from a project list to another
        project list """
        newDay.addProject(project)
        self.removeProject(project)


    def copyProject(self, project, newDay):
        """ Copies a project to another day's project list """
        newDay.addProject(project)


    def renameProject(self, project, newName):
        """ Renames a project """
        i = project.getTasks()
        self.addProject(newName, i)
        self.removeProject(project)


    def getProjects(self):
        """ Gets a list of a Day's project objects """
        list = []
        for i in self.projects:
            list.append(i)
        return list


    def getStrProjects(self):
        """ Gets a list of string representations of a Day's
        Project objects"""
        projectList = []
        
        for i in self.getProjects():
            projectList.append(str(i))
        return projectList
    

    def getProject(self, project):
        """ Gets a Project object from a string that matches the object's 
        output from the __str__ method """
        # string list
        strList = self.getStrProjects()
        # container list
        contList = self.getProjects()

        try:
            project = self.testString(project)
        except:
            raise KeyError("Must select an existing project")
        index = contList.index(project)
        return contList[index]
