# Hong Anh Nguyen
# THW2.py

# A Dataset class do analysis of dataset containing daily weather entries
class Dataset:

# Constructor: contain required name of souce file and optional name of set
    def __init__(self, file, set = None):
        self.fileName = file
        self.setName = set
        self.data = {}
        self.insertData(file)

# Method:
# insertData pass data from file into Object’s data attribute.
# parameters:
      # fileName: string
# return none
    def insertData(self, fileName):
        # open fileName
        reader = open(fileName, "r")
        # read fileName
        lines = reader.readlines()
        # initialize value for day
        day = 0
        for r in lines:
            # keep track of day
            day += 1
            # divide each row into individual values
            self.data[day] = r.split(",")
        # close fileName
        reader.close()

# getTempOn collect temperature of a particular day
# parameters:
      # day: integer
# return air temperature on that day to 2 decimal places
    def getTempOn(self, day):
        return round(float(self.data[day][0]),2)

# getHumidityOn collect humidity of a particular day
# parameters:
      # day: integer
# return humidity on that day to 2 decimal places
    def getHumidityOn(self, day):
        return round(float(self.data[day][1]),2)

# getWindOn collect wind speed of a particular day
# parameters:
      # day: integer
# return wind speed on that day to 2 decimal places
    def getWindOn(self, day):
        return round(float(self.data[day][2]),2)

# meanTemp find average temperature during a period of time
# parameters:
      # day: integer
      # num: integer
# return average temperature for a number of days beginning on a specific day
# to 2 decimal places
    def meanTemp(self, day, num):
        # set up an empty list
        list = []
        # initialize value for sum
        sum = 0
        for i in range(num):
            # assign track to the beginning day
            track = day
            # set track to each day in the period
            track += i
            # add temperature of each day to list
            list.append(self.data[track][0])
        for j in range(len(list)):
            # add up temperature of each day
            sum += float(list[j])
        # find the average temperature during the period
        average = sum/len(list)
        return round(average,2)

# meanHumidity find average humidity during a period of time
# parameters:
      # day: integer
      # num: integer
# return average humidity for a number of days beginning on a specific day
# to 2 decimal places
    def meanHumidity(self, day, num):
        # set up an empty list
        list = []
        # initialize value for sum
        sum = 0
        for i in range(num):
            # assign track to the beginning day
            track = day
            # set track to each day in the period
            track += i
            # add humidity of each day to list
            list.append(self.data[track][1])
        for j in range(len(list)):
            # add up humidity of each day
            sum += float(list[j])
        # find the average humidity during the period
        average = sum/len(list)
        return round(average,2)

# meanWindSpeed find average windspeed during a period of time
# parameters:
      # day: integer
      # num: integer
# return average windspeed for a number of days beginning on a specific day
# to 2 decimal places
    def meanWindSpeed(self, day, num):
        # set up an empty list
        list = []
        # initialize value for sum
        sum = 0
        for i in range(num):
            # assign track to the beginning day
            track = day
            # set track to each day in the period
            track += i
            # add windspeed of each day to list
            list.append(self.data[track][2])
        for j in range(len(list)):
            # add up windspeed of each day
            sum += float(list[j])
        # find the average windspeed during the period
        average = sum/len(list)
        return round(average,2)
