import serial
import logging
import datetime

from PyQt5.QtCore import QTimer

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
now = datetime.datetime.now()


class Serial:
    def __init__(self):
        logging.info("Serial initial")
        print("Serial initial")
        self.__port = 'COM3'
        self.__bandrate = 11520  # bandrate
        self.__timex = 2  # timeout
        self.__data = ""  # data from serial

        logging.info("prot:" + self.__port + "/bandrate:" + str(self.__bandrate) + "/timex:" + str(self.__timex))
        print("prot:" + self.__port + "/bandrate:" + str(self.__bandrate) + "/timex:" + str(self.__timex))

    def getSerial(self):
        """
        return the serial
        :return: serial
        """
        try:
            self.__ser = serial.Serial(
                self.__port,
                self.__bandrate,
                timeout=self.__timex,
                parity=serial.PARITY_ODD,  # 校验位
                stopbits=serial.STOPBITS_TWO,  # 停止位
                bytesize=serial.SEVENBITS  # 数据位
            )
            self.__ser.flushInput()
            logging.info("initial successful")
            return self.__ser
        except:
            logging.info("initial failed")
            return -1

    def isOpenSerial(self):
        """
        clear all the data in serial and open it
        :return: flag->value:true or false
        """
        logging.info("open Serial")
        if self.__ser.isOpen():
            flag = 1
            logging.info("open successful")
        else:
            flag = 0
            logging.error("open failed")
        return flag

    def closSerial(self):
        """
        close serial
        :return:flag->value:true or false
        """
        logging.info("close Serial")
        try:
            self.__ser.close()
            logging.info("close successful")
        except:
            logging.error("close failed")
        finally:
            logging.info("close finish")

    def readSerial(self):
        """
        read the data read from serial
        :return: flag->value: number
        recieving data from serial successful returns [1-?]
        data not exist in defalut setting returns -1
        no data returns 0

        value of self.data:
        1. "yi fu"
        2."tu shu"
        3."tiao liao"
        4.b''
        WARNING: the number of its value may be extended in the furture, please take care of your data structure and code scalability
        """
        flag = 0
        try:
            if self.__ser.inWaiting():
                self.__data = self.__ser.readline()
                if self.__data == 'xiao jie':
                    flag = 1
                elif self.__data == 'yi fu':
                    flag = 2
                elif self.__data == 'tu shu':
                    flag = 3
                elif self.__data == 'tiao liao':
                    flag = 4
                else:
                    print(self.__data)
                    flag = -1
                logging.info("data from serial:" + str(flag))
            else:
                flag = 0
                logging.info("no data")
        except IOError:
            flag = -2
        finally:
            return flag


def voiceManager():
    ser = Serial()  # get Serial object
    port = ser.getSerial()  # get serial insert on your computer
    if port == -1:
        print("cannot get the serial")
    else:
        print("get serial successful")

    if ser.isOpenSerial():  # judge whether the serial open successfully
        print("serial open successful")
    else:
        print("serial open failed")

    data = ser.readSerial()
    if data == 2:
        print("yi fu")
    elif data == 3:
        print("tu shu")
    elif data == 4:
        print("tiao liao")
    elif data == 1:
        print("xiao jie")
    elif data == 0:
        print("no data")
    elif data == -1:
        print("data cannot be recognized")


if '__name__' == '__main__':
    _timer = QTimer()
    _timer.timeout.connect(voiceManager)
    _timer.start(1000)  # plot after 1s delay
    #
    # b"'hAfh\x1d\x16\x19\x12"
    # command = -1
    # command = 0
    # b'&MGIQnIL\x19\x16\x1d\x16'
