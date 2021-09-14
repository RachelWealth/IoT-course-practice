import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
class Serial:
    def __init__(self):
        logging.INFO("The completion of the initial static interface")
        self.port = 'COM3'
        self.bandrate = 9600
        self.timex = 1000
        logging.INFO("prot:"+self.port+"/bandrate:"+self.bandrate+"/timex:"+self.timex)