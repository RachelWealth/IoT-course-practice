import logging
from Serial import Serial
"""
just an example of how to use Serial.py file
"""
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def example():
    ser = Serial()  # get Serial object
    port = ser.getSerial()  # get serial insert on your computer
    if port == -1:
        print("cannot get the serial")
        return 1
    else:
        print("get serial successful")

    if port.isOpenSerial():         # judge whether the serial open successfully
        print("serial open successful")
    else:
        print("serial open failed")
        return 2

    data = port.readSerial()
    if data == 1:
        print("yi fu")
    elif data == 2:
        print("tu shu")
    elif data == 3:
        print("tiao liao")
    elif data == 0:
        print("no data")
    elif data == -1:
        print("data cannot be recognized")

    port.close()


if __name__ == '__main__':
    example()
    logging.info("serialTest begin")
