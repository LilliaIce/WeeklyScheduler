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

# list of the days of the week
DAYSOFWEEK = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Master')

# prompt for main menu
MAINP = " > "
# prompt for day menu
DAYP = "\t > "
# prompt for options
OPTIONP = "\t\t > "

# menus
MAINMENU = ("Enter 'q' or nothing to quit the program.")
DAYMENU = ("Enter 'a' to add a task, 'd' to delete a task, 'r' to "
            "rename a task, 'm' to move a task,  or 't' to toggle a task.")


def addTask(day):
    i = input(OPTIONP)
    while i != 'q' and not i.isspace():
        day.addTask(i)
        i = input(OPTIONP)


def removeTask(day):
    i = input(OPTIONP)
    while i != 'q' and not i.isspace():
        try:
            day.removeTask(i)
        except:
            print("Sorry, that wasn't a valid task.")
        i = input(OPTIONP)


def moveTask(day, schedule):
    i = input(OPTIONP)
    while i != 'q' and not i.isspace():
        j = input(OPTIONP).title().strip()
        if j != 'Q' and not j.isspace():
            j = schedule.getDay(j)
            day.moveTask(i, j)
        i = input(OPTIONP)


def toggleTask(day):
    i = input(OPTIONP)
    while i != 'q' and not i.isspace():
        try:
            day.toggleTask(i)
        except:
            pass
        i = input(OPTIONP)


def createWeek(days):
    """Creates a list full of Day objects (initalized from a list of days)
    and initializes a Week object with them"""
    items = []
    for item in days:
        items.append(Day(item))
    return Week(items)


def addProject():
    i = input(OPTIONP)
    if i != 'q' and not i.isspace():
        day.addProject(i)


def removeProject():
    pass


def getWeekTasks(schedule):
    """"""
    list = []
    for item in schedule.getDays():
        list.append(item)
    return list


def getColumnWidth(week):
    """ Returns the width of the longest item plus CONST"""
    list = []
    CONST = 5
    for day in week:
        for item in day.getTasks():
            list.append(item)
    return max(len(i) for i in list) + CONST


def getLongestList(tasks):
    """ Returns the length of the longest task list"""
    return max(len(i.getTasks()) for i in tasks)


def displayWeek(week):
    """ Displays the tasks for each day in a separate column that extends
    through the longest task list 
    
    The column's width is generated to fit the longest task with some padding
    each time """
    width = getColumnWidth(week)
    maxRow = getLongestList(week)

    for i in DAYSOFWEEK:
        print(f"{i:{width}}", end="")
    print()

    for row in range(0, maxRow):
        for day in week:
            try:
                print(f"{day.getTasks()[row]:{width}}", end="")
            except:
                print(f"{'':{width}}", end="")
        print()


def displayDay(day):
    """ Displays a day's tasks """
    width = getColumnWidth(day)
    maxRow = getLongestList(day)

    print(day)

    for row in range(0, maxRow):
        print(f"{day.getTasks()[row]:{width}}", end="")
    print()


def displayTasks():
    pass


def dayLoop(schedule, dayInput):
        ADD = 'A'
        DELETE = 'D'
        RENAME = 'R'
        MOVE = 'M'
        TOGGLE = 'T'

        day = schedule.getDay(dayInput)
        i = "none"
        while i != 'q' and not i.isspace():
            # gets the user's input for the day menu
            print(DAYMENU)
            i = input(DAYP)

            if i.upper() == ADD:
                addTask(day)
            elif i.upper() == DELETE:
                removeTask(day)
            elif i.upper() == RENAME:
                pass
            elif i.upper() == MOVE:
                moveTask(day, schedule)
            elif i.upper() == TOGGLE:
                toggleTask(day)
            else:
                # if input doesn't correspond to any of the available
                # options, user will be prompted for a new input
                print()
                print(f"{i} isn't a valid option.")
            File.saveFile(schedule)


def startup():
    """ Function will read file if able to; if unable to, function will 
    print line to warn user """
    try:
        schedule = File.readFile()
    except:
        print("Program didn't find file to read; to avoid data being ",
              "replaced when the program creates a new file, ",
              "immediately exit the program.")
        print("Press 'Enter' to continue.")
        input()
        schedule = createWeek(DAYSOFWEEK)
        print("Data has been replaced.")
    return schedule


def main():
    schedule = startup()
    print()
    print(MAINMENU)

    print()
    displayWeek(getWeekTasks(schedule))
    print()

    dayInput = "none"
    while dayInput != 'q' and not dayInput.isspace():
        # prompts the user to select a day
        print("Please select a day from the following list.")
        print(*schedule.getDays(), sep = ", ")
        print()

        dayInput = input(DAYP).title().strip()

        while dayInput not in DAYSOFWEEK:
            print("That's not a day of the week. Please choose a day from Monday to Friday " +
                  "or the 'master' list.")
            dayInput = input(MAINP).title().strip()

        dayLoop(schedule, dayInput)
        print()
        os.system("cls")
        displayWeek(getWeekTasks(schedule))
        print()

if __name__ == '__main__':
    main()
