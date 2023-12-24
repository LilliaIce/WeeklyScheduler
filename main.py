"""
This program is intended to be used as a weekly
scheduler that will manage a list of tasks. Each
task can be assigned to a day in the week.

Additionally, the program will provide a list of
completed tasks for each day and can toggle
a task as repeatable each week.
"""

import os
from file import File
from week import Week
from project import Project
from day import Day

# tuple of the days of the week
DAYSOFWEEK = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Master')

PROMPT = " > "
INDEX1 = ""
INDEX2 = "\t"
INDEX3 = "\t\t"
INDEX4 = "\t\t\t"
TASKINDENT = "  "

MINWIDTH = 8
NONE = "none"

# constant user-options
QUIT = 'Q'
ADDPROJ = 'AP'
DELETEPROJ = 'DP'
MOVEPROJ = 'MP'
ADD = 'A'
DELETE = 'D'
MOVE = 'M'
TOGGLE = 'T'

# menus
MAINMENU = ("Enter 'q' or nothing to quit the program.")
SELECTDAY = ("Select a day from the above list.")
SELECTOPTION = ("Enter 'ap' to add a project, 'dp' to delete a project, 'a' to add a task, "
           "'d' to delete a task,'r' to rename a task, 'm' to move a task,  or 't' to "
           "toggle a task.")
UNKNOWN = ("Program didn't find file to read; to avoid data being replaced "
           "when the program creates a new file, immediately exit the program.")
REPLACE = ("Data has been replaced.")
CONTINUE = ("Press 'Enter' to continue.")

VALIDOPTION = ("Sorry, that wasn't a valid day.")
VALIDTASK = ("Sorry, that wasn't a valid task.")
VALIDPROJECT = ("Sorry, that wasn't a valid project.")

DAYTEXT = ("Enter a day.")
TASKTEXT = ("Enter a task.")
PROJECTTEXT = ("Enter a project.")

# Week-related functions

def createWeek(days):
    """ Creates a list full of Day objects (initalized from a list of days)
    and initializes a Week object with them """
    items = []
    for i in days:
        items.append(Day(i))
    return Week(items)


def getDays(week):
    """ Get the week's tasks """
    list = []
    for day in week.getDays():
        list.append(day)
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
        try:
            day.removeProject(day.getProject(i))
        except:
            print(VALIDPROJECT)


def moveProject(day, schedule):
    print(INDEX3, PROJECTTEXT)
    j = input(INDEX3+PROMPT)

    if j.upper() != QUIT and not j.isspace():
        j = day.getProject(j)
        print(INDEX3, "GET NEW DAY")
        i = input(INDEX3+PROMPT).title().strip()

        if i.upper() != QUIT and not i.isspace():
            i = schedule.getDay(i)
            day.moveProject(j, i)


# Task-related functions

def addTask(day):
    print(INDEX3, PROJECTTEXT)
    j = input(INDEX3+PROMPT)
    try:
        project = day.getProject(j)
    except:
        print(VALIDPROJECT)
    print(INDEX4, TASKTEXT)
    i = input(INDEX4+PROMPT)
    
    while i.upper() != QUIT and not i.isspace():
        try:
            project.addTask(i)
        except:
            print(VALIDTASK)
        print(INDEX4, TASKTEXT)
        i = input(INDEX4+PROMPT)


def removeTask(day):
    print(INDEX3, PROJECTTEXT)
    j = input(INDEX3+PROMPT)
    project = day.getProject(j)
    print(INDEX3, TASKTEXT)
    i = input(INDEX3+PROMPT)

    while i.upper() != QUIT and not i.isspace():
        try:
            project.removeTask(i)
        except:
            print(VALIDTASK)
        print(INDEX3, TASKTEXT)
        i = input(INDEX3+PROMPT)


def moveTask(day, schedule):
    print(INDEX3, PROJECTTEXT)
    j = input(INDEX3+PROMPT)
    project = day.getProject(j)
    print(INDEX3, TASKTEXT)
    i = input(INDEX3+PROMPT)

    while i.upper() != QUIT and not i.isspace():
        print(INDEX3, "GET NEW DAY")
        newDay = input(INDEX3+PROMPT).title().strip()

        if newDay.upper() != QUIT and not i.isspace():
            newDay = schedule.getDay(newDay)
            print(INDEX3, PROJECTTEXT)
            newProject = input(INDEX3+PROMPT).title().strip()

            if newProject.upper() != QUIT and not newProject.isspace():
                newProject = newDay.getProject(j)
                project.moveTask(i, newProject)

        print(INDEX3, TASKTEXT)
        i = input(INDEX3+PROMPT)


def toggleTask(day):
    print(INDEX3, PROJECTTEXT)
    j = input(INDEX3+PROMPT)
    project = day.getProject(j)
    print(INDEX3, TASKTEXT)
    i = input(INDEX3+PROMPT)
    while i != 'q' and not i.isspace():
        try:
            project.toggleTask(i)
        except:
            print(VALIDTASK)
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
        list.append(arrangeDayDisplay(item))
    return max(len(i) for i in list)


def arrangeDayDisplay(day):
    list = []
    for project in day.getProjects():
        list.append(f"| {str(project)}")
        try:
            for task in project.getTasks():
                if "-" in task:
                    list.append(TASKINDENT+task)
                else:
                    list.append(TASKINDENT+TASKINDENT+task)
        except:
            print("")
    return list


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
            dayList = arrangeDayDisplay(day)
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
            print(INDEX1, SELECTDAY)
            dayInput = input(INDEX1+PROMPT).title().strip()

        day = schedule.getDay(dayInput)
        i = "none"

        while i != 'q' and not i.isspace():
            print(INDEX2, SELECTOPTION)
            i = input(INDEX2+PROMPT)

            if i.upper() == ADDPROJ:
                addProject(day)
            elif i.upper() == DELETEPROJ:
                removeProject(day)
            elif i.upper() == MOVEPROJ:
                moveProject(day, schedule)
            elif i.upper() == ADD:
                addTask(day)
            elif i.upper() == DELETE:
                removeTask(day)
            elif i.upper() == MOVE:
                moveTask(day, schedule)
            elif i.upper() == TOGGLE:
                toggleTask(day)
            else:
                print(f"{i} isn't a valid option.")  
        
        File.saveFile(schedule)
        print()
        os.system("cls")
        displayWeek(getDays(schedule))
        print()
        print(INDEX1, SELECTDAY)
        dayInput = input(INDEX1+PROMPT).title().strip()


if __name__ == '__main__':
    main()
