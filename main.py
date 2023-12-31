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
from menu import Menu
from day import Day
from file import File

# list of the days of the week
DAYSOFWEEK = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Master')

def addTask(day):
    i = input(Menu.OPTIONP)
    while i != 'q' and not i.isspace():
        day.addTask(i)
        i = input(Menu.OPTIONP)


def removeTask(day):
    i = input(Menu.OPTIONP)
    while i != 'q' and not i.isspace():
        try:
            day.removeTask(i)
        except:
            pass
        i = input(Menu.OPTIONP)


def moveTask(day, schedule):
    i = input(Menu.OPTIONP)
    while i != 'q' and not i.isspace():
        j = input(Menu.OPTIONP).title().strip()
        if j != 'Q' and not j.isspace():
            j = schedule.getDay(j)
            day.moveTask(i, j)
        i = input(Menu.OPTIONP)


def toggleTask(day):
    i = input(Menu.OPTIONP)
    while i != 'q' and not i.isspace():
        try:
            day.toggleTask(i)
        except:
            pass
        i = input(Menu.OPTIONP)


def createWeek(days):
    """Creates a list full of Day objects (initalized from a list of days)
    and initializes a Week object with them"""
    items = []
    for item in days:
        items.append(Day(item))
    return Week(items)


def displayTasks(tasks):
    """Displays the tasks for each in a separate column that extends
    over the longest task list"""
    for item in DAYSOFWEEK:
        print(f"{item:30}", end="")
    print()
    longest = max([len(i.getTasks()) for i in tasks])
    for position in range(0, longest):
        for i in tasks:
            try:
                print(f"{i.getTasks()[position]:30}", end="")
            except:
                print(f"{'':30}", end="")
        print()


def getWeeksTasks(schedule):
    """"""
    list = []
    for item in schedule.getDays():
        list.append(item)
    return list


def main():
    # will read file if able to; if not able, will print line to
    # warn user
    kill = input("Press any key to start: ")
    if kill == 'd':
        File.clearFile()
    try:
        schedule = File.readFile()
    except:
        print("Program didn't find file to read; to avoid data being ",
              "replaced when the program creates a new file, ",
              "immediately exit the program.")
        print("Press 'Enter' to continue.")
        input("")
        schedule = createWeek(DAYSOFWEEK)
        print("Data has been replaced.")
    print()
    print(Menu.MAINMENU)

    print()
    displayTasks(getWeeksTasks(schedule))
    print()

    dayInput = "none"
    while dayInput != 'q' and not dayInput.isspace():
        # prompts the user to select a day
        print("Please select a day from the following list.")
        print(*schedule.getDays(), sep = ", ")
        print()

        dayInput = input("Please select the day. > ").title().strip()

        while dayInput not in DAYSOFWEEK:
            print("That input wasn't valid. Please select from the following options.")
            dayInput = input(" > ").title().strip()

        day = schedule.getDay(dayInput)

        i = "none"
        while i != 'q' and not i.isspace():
            # gets the user's input for the day menu
            print(Menu.DAYMENU)
            i = input(Menu.DAYP)

            if i == 'a':
                # add tasks
                addTask(day)
            elif i == 'd':
                # remove tasks
                try:
                    removeTask(day)
                except NameError:
                    print("That wasn't a valid option.")
            elif i == 'r':
                # rename tasks
                pass
            elif i == 'm':
                # move tasks to another day
                moveTask(day, schedule)
            
            elif i == 't':
                # toggle tasks
                toggleTask(day)
            else:
                # if input doesn't correspond to any of the available
                # options, user will be prompted for a new input
                print()
                print(f"{i} isn't a valid option.")
            # when the user finishes with the above options, the program
            # will save to the file and display the main menu again
            File.saveFile(schedule)
        print()
        os.system("cls")
        displayTasks(getWeeksTasks(schedule))
        print()


if __name__ == '__main__':
    main()
