import os, pickle

class File:
    # reads the file and grabs the 'week' object from previous sessions
    def readFile():
        with open("weeklySchedule.txt", "rb") as f:
            info = pickle.load(f)
        return info

    # saves the 'week' object to the file
    def saveFile(week):
        with open("weeklySchedule.txt", "wb") as f:
            pickle.dump(week, f)

    def clearFile():
        os.remove("weeklySchedule.txt")

    # renames the file for archival purposes
    def archiveFile():
        file = open("weeklySchedule.txt", "r").read()
        weekDate = input("Week-dates: > ")
        weekName = f"Week {weekDate}"
        newFile = open(f"{weekName}", 'w')
        newFile.write(pickle.dump(file))
        file.close()
        newFile.close()
    
    def loadArchivedFile():
        pass