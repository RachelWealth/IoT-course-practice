import serial
import logging
import datetime

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
now = datetime.datetime.now()


class Serial:
    def __init__(self):
        logging.INFO("Serial initial")
        self.port = 'COM3'
        self.bandrate = 9600
        self.timex = 1000
        logging.INFO("prot:"+self.port+"/bandrate:"+self.bandrate+"/timex:"+self.timex)

    def openSerial(self):
        """
        open serial
        :return: flag->value:true or false
        """
        logging.INFO(now.strftime("%Y-%m-%d %H:%M:%S") + "open Serial")

        logging.INFO(now.strftime("%Y-%m-%d %H:%M:%S") + "open successful")


    def closSerial(self):

        """
        close serial
        :return:flag->value:true or false
        """
        logging.INFO(now.strftime("%Y-%m-%d %H:%M:%S") + "close Serial")

        logging.INFO(now.strftime("%Y-%m-%d %H:%M:%S") + "Serial successful")

    def readSerial(self):
        """
        read the data read from serial
        :return: data->value type:string
        """



