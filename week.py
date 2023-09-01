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
        self.list = []
        for i in self.daysInWeek:
             self.list.append(str(i))
        return self.daysInWeek[self.list.index(day)]