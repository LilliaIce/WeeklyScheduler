class Week():
    def __init__(self, days):
        """When a week object is created, populates the days list with
        the days of the week."""
        self.daysInWeek = []
        for item in days:
                self.daysInWeek.append(item)


    def getDays(self):
        """Gets a list of the days in the Week object."""
        return self.daysInWeek


    def getDay(self, day):
        """Gets a day from the daysInWeek list."""
        list = []
        for i in self.daysInWeek:
             list.append(str(i))
        return self.daysInWeek[list.index(day)]