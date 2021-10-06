import json
import pickle

writefileRoad = "web/config/datas.txt"
readfileRoad = "config/datas.txt"


class sendDataHelper:
    def __init__(self):
        self.datas = 0

    def writeToFile(self,datas):
        with open(writefileRoad, 'w') as filehandle:
            #filehandle.writelines("%s\n" % data for data in datas)
            json.dump(datas, filehandle)

    def readFromFile(self):
        # define empty list
        places = []

        # open file and read the content in a list
        with open(readfileRoad, 'r') as filehandle:
            # filecontents = filehandle.readlines()
            #
            # for line in filecontents:
            #     # remove linebreak which is the last character of the string
            #     current_place = line[:-1]
            #
            #     # add item to the list
            #     places.append(eval(current_place))
            places = json.load(filehandle)
        print(places)
        return places

