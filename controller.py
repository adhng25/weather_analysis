# Hong Anh Nguyen
#controller.py

# Import the Dataset class
from THW2 import Dataset

# mostHumid find the most humid day in dataset
# parameters:
      # data: dataset
# return number of the most humid day
def mostHumid(data):
    # set up an empty list
    list = []
    for day in range(1,366):
        # add humidity of each day in a year to list
        list.append(data.getHumidityOn(day))
    # assign max to the first value in list
    max = list[0]
    # initialize value for j
    j = 0
    # initialize value for humidDay
    humidDay = 1
    for i in list:
        # keep track of j
        j += 1
        # check if values in list larger than max
        if (i > max):
            # assign max to i
            max = i
            # assign humidDay to the index of i in list
            humidDay = j
    return humidDay

# tempDiffer find the day that contained largest temperature difference
# parameters:
      # data1: dataset
      # data2: dataset
# return number of the the day contained largest temperature difference
def tempDiffer(data1, data2):
    # set up empty list1
    list1 = []
    # set up empty list2
    list2 = []
    # set up an empty list
    list = []
    for day in range(1,366):
        # add temperature of each day in a year to list1
        list1.append(data1.getTempOn(day))
        # add temperature of each day in a year to list2
        list2.append(data2.getTempOn(day))
    for i in range(0,365):
        # add difference between temperature of each day in a year to list
        list.append(abs(list1[i]-list2[i]))
    # assign max to the first value in list
    max = list[0]
    # initialize value for j
    j = 0
    # initialize value for tempdifferDay
    tempdifferDay = 1
    for i in list:
        # keep track of j
        j += 1
        # check if values in list larger than max
        if (i > max):
            # assign max to i
            max = i
            # assign tempdifferDay to the index of i in list
            tempdifferDay = j
    return tempdifferDay

# wind7Day find highest average wind speed for any 7-day period
# parameters:
      # data: dataset
# return the highest average wind speed for a 7-day period
def wind7Day(data):
    # set up an empty list
    list = []
    for day in range(1,360):
        # add average windspeed for any 7-day period to list
        list.append(data.meanWindSpeed(day,7))
    # assign max to the first value in list
    max = list[0]
    for i in list:
        # check if values in list larger than max
        if (i > max):
            # assign max to i
            max = i
    return max


def main():
    data2006 = Dataset("Open_2006_daily.txt")
    data2018 = Dataset("Open_2018_daily.txt")
    print("Average temperature, 2006: ", data2006.meanTemp(1,365))
    print("Average temperature, 2018: ", data2018.meanTemp(1,365))
    print("Average humidity, 2006: ", data2006.meanHumidity(1,365))
    print("Average humidity, 2018: ", data2018.meanHumidity(1,365))
    print("Average wind speed, 2006: ", data2006.meanWindSpeed(1,365))
    print("Average wind speed, 2018: ", data2018.meanWindSpeed(1,365))
    print("Most humid day in 2006: ", mostHumid(data2006))
    print("Most humid day in 2018: ", mostHumid(data2018))
    print("Day contained largest temperature difference: ", tempDiffer(data2006, data2018))
    print("Highest average wind speed, 2006: ", wind7Day(data2006))
    print("Highest average wind speed, 2018: ", wind7Day(data2018))
main()
