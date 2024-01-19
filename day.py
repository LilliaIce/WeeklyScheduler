"""Module with the Day class"""

class Day:
    def __init__(self, name):
        """ When a Day object is created, creates a projects list. """
        self.projects = []
        self.name = name


    def __str__(self):
        """ Names the Day object """
        return self.name


    def testString(self, project):
        """Tests if a valid project name
        
        If the project name already exists, the string is invalid"""
        val = True
        projects = self.getStrProjects()
        for i in projects:
            if project.lower().strip() == i.lower().strip():
                val = False
        return val


    def addProject(self, project):
        """Adds a project to the projects list."""
        if project.name.isspace():
            raise NameError("Project can't be whitespace")
        elif project == False:
            raise NameError("Project can't be empty")
        elif project in self.projects:
            raise NameError("Project can't be in the projects list")
        self.projects.append(project)


    def removeProject(self, project):
        """ Removes a project from the project list. """
        self.projects.remove(project)


    def moveProject(self, project, newDay):
        """ Moves a project from a project list to another
        project list """
        if str(project) in newDay.getStrProjects():
            newProject = newDay.getProject(str(project))
            for task in project.getTasks():
                project.moveTask(task, newProject)
        else:
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

        if project in strList:
            index = strList.index(project)
            return contList[index]
        raise NameError("Project must be in the projects list")