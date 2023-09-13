"""
This program is intended to be used as a weekly
scheduler that will manage a list of tasks. Each
task can be assigned to a day in the week.

Additionally, the program will provide a list of
completed tasks for each day and can toggle
a task as repeatable each week.
"""

import os
from week import Week
from project import Project
from day import Day
from file import File

# tuple of the days of the week
DAYSOFWEEK = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Master')

PROMPT = " > "
INDEX1 = ""
INDEX2 = "\t"
INDEX3 = "\t\t"
INDEX4 = "\t\t\t"
TASKINDENT = "    "

MINWIDTH = 5

QUIT = 'Q'
ADDPROJ = 'AP'
DPROJJ = 'DP'
ADD = 'A'
DELETE = 'D'
MOVE = 'M'
TOGGLE = 'T'

# menus
MAINMENU = ("Enter 'q' or nothing to quit the program.")
DAYMENU = ("Enter 'ap' to add a project, 'dp' to delete a project, 'a' to add a task, "
           "'d' to delete a task,'r' to rename a task, 'm' to move a task,  or 't' to "
           "toggle a task.")
UNKNOWN = ("Program didn't find file to read; to avoid data being replaced "
           "when the program creates a new file, immediately exit the program.")
REPLACE = ("Data has been replaced.")
CONTINUE = ("Press 'Enter' to continue.")
VALIDOPTION = ("That wasn't valid input. Please one of the above column headers.")
SELECTDAY = ("Select a day from the above list.")
VALIDTASK = ("Sorry, that wasn't a valid task.")
NONE = ("none")
TASKTEXT = "Enter a task."
PROJECTTEXT = "Enter a project."

# Week-related functions

def createWeek(days):
    """ Creates a list full of Day objects (initalized from a list of days)
    and initializes a Week object with them """
    items = []
    for item in days:
        items.append(Day(item))
    return Week(items)


def getDays(week):
    """ Get the week's tasks """
    list = []
    for day in week.getDays():
        list.append(day)
    return list


# Day-related functions

def sortDay(day):
    list = []
    for project in day.getProjects():
        list.append(f"| {str(project)}")
        for task in project.getTasks():
            if "-" in task:
                list.append(task)
            else:
                list.append(TASKINDENT+task)
    return list


# Project-related functions

def addProject(day):
    """ Adds a project to a day """
    i = input(INDEX3+PROMPT)
    if i.upper() != QUIT and not i.isspace():
        day.addProject(Project(i))


def removeProject(day):
    """ Removes a project from a day """
    i = input(INDEX3+PROMPT)
    if i.upper() != QUIT and not i.isspace():
        day.removeProject(getProjectObjFromStr(i, day))


def getProjectObjFromStr(project, day):
    """ Gets a Project object from a string that matches the object's 
    output from the __str__ method """
    # string list
    strList = getStrProjectList(day)
    # container list
    contList = day.getProjects()

    for string in strList:
        if string.lower().strip() == project:
            index = strList.index(string)
            return contList[index]
        else:
            raise KeyError("Check getProjectObjFromStr")


def getStrProjectList(day):
    """ Gets a list of string representations of Project objects"""
    projectList = []
    
    for item in day.getProjects():
        projectList.append(str(item))
    return projectList


# Task-related functions

def addTask(project):
    print(INDEX3, TASKTEXT)
    i = input(INDEX3+PROMPT)
    while i.upper() != QUIT and not i.isspace():
        project.addTask(i)
        print(INDEX3, TASKTEXT)
        i = input(INDEX3+PROMPT)


def removeTask(project):
    print(INDEX3, TASKTEXT)
    i = input(INDEX3+PROMPT)
    while i.upper() != QUIT and not i.isspace():
        project.removeTask(i)
        print(INDEX3, TASKTEXT)
        i = input(INDEX3+PROMPT)


def moveTask(day, schedule):
    print(INDEX3, TASKTEXT)
    i = input(INDEX3+PROMPT)
    while i.upper() != QUIT and not i.isspace():
        j = input(INDEX3+PROMPT).title().strip()
        if j.upper() != QUIT and not j.isspace():
            j = schedule.getDay(j)
            day.moveTask(i, j)
        print(INDEX3, TASKTEXT)
        i = input(INDEX3+PROMPT)


def toggleTask(project):
    print(INDEX3, TASKTEXT)
    i = input(INDEX3+PROMPT)
    while i != 'q' and not i.isspace():
        project.toggleTask(i)
        print(INDEX3, TASKTEXT)
        i = input(INDEX3+PROMPT)


# Display-related functions

def getColumnWidth(week):
    """ Returns the width of the longest item plus CONST """
    list = []
    for day in week:
        for project in day.getProjects():
            list.append(str(project))
            for item in project.getTasks():
                list.append(item)
    # min width is added for some whitespace between columns
    return max(len(i) for i in list) + MINWIDTH


def getLongestList(week):
    """ Returns the length of the longest task list"""
    list = []
    for item in week:
        list.append(sortDay(item))
    return max(len(i) for i in list)


def displayWeek(week):
    """ Displays the tasks for each day in a separate column that extends
    through the longest task list 
    
    The column's width is generated to fit the longest task with some padding
    each time """
    try:
        width = getColumnWidth(week)
    except:
        width = MINWIDTH
    maxRow = getLongestList(week)

    for i in DAYSOFWEEK:
        print(f"{i:{width}}", end="")

    print()

    for row in range(0, maxRow):
        for day in week:
            dayList = sortDay(day)
            try:
                if "|" in dayList[row]:
                    print(f"{dayList[row]:{width}}", end="")
                elif "-" in dayList[row]:
                    print(f"{dayList[row]:{width}}", end="")
                else:
                    print(f"{dayList[row]:{width}}", end="")
            except:
                print(f"{'':{width}}", end="")
        print()


def main():
    try:
        schedule = File.readFile()
    except:
        print(UNKNOWN)
        print(CONTINUE)
        input()
        schedule = createWeek(DAYSOFWEEK)
        print(REPLACE)
    print()
    print(MAINMENU)
    print()
    displayWeek(getDays(schedule))
    print()
    print(SELECTDAY)
    dayInput = input(INDEX1+PROMPT).title().strip()

    while dayInput.upper() != QUIT and not dayInput.isspace():

        while dayInput not in DAYSOFWEEK:
            print(VALIDOPTION)
            dayInput = input(INDEX1+PROMPT).title().strip()

        day = schedule.getDay(dayInput)
        i = "none"

        while i != 'q' and not i.isspace():
            print(INDEX2, DAYMENU)
            i = input(INDEX2+PROMPT)

            if i.upper() == ADDPROJ:
                addProject(day)
            elif i.upper() == DPROJJ:
                removeProject(day)
            elif i.upper() == ADD:
                print(INDEX3, PROJECTTEXT)
                j = input(INDEX3+PROMPT)
                k = getProjectObjFromStr(j, day)
                addTask(k)
            elif i.upper() == DELETE:
                print(INDEX3, PROJECTTEXT)
                j = input(INDEX3+PROMPT)
                k = getProjectObjFromStr(j, day)
                removeTask(k)
            elif i.upper() == MOVE:
                print(INDEX3, PROJECTTEXT)
                j = input(INDEX3+PROMPT)
                k = getProjectObjFromStr(j, day)
                moveTask(day, schedule)
            elif i.upper() == TOGGLE:
                print(INDEX3, PROJECTTEXT)
                j = input(INDEX3+PROMPT)
                k = getProjectObjFromStr(j, day)
                toggleTask(k)
            else:
                print(f"{i} isn't a valid option.")  
        
        File.saveFile(schedule)
        print()
        os.system("cls")
        displayWeek(getDays(schedule))
        print()
        dayInput = input(INDEX1+PROMPT).title().strip()


if __name__ == '__main__':
    main()
