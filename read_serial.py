import serial
import re
import pyrebase
import time
import yaml

class ST_Connection(object):
    
    def __init__(self, config_path):
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.port = '/dev/ttyACM0'
        self.ser.open()
        with open(config_path) as f:
            config = yaml.load(f)
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def read_data(self):
        channel = None
        address = None
        innum = None
        outnum = None
        while True:
            res = self.ser.readline().decode("utf-8")
            #print(res)
            z0 = re.match(r".*?Published Address is= (\S+).*", res)
            z1 = re.match(r".*?peer_addr=\[(\d+)\].*", res)
            z2 = re.match(r".*?Innum: (\d+), Outnum: (\d+).*", res)
            #print (z0, z1, z2)
            if z0:
                channel = z0.groups()[0]
            if z1: 
                address = z1.groups()[0] 
            if z2:
                innum = z2.groups()[0]
                outnum = z2.groups()[1]
                if channel and address:
                    self.update(channel, address, int(innum), int(outnum))


    def update(self, channel, address, innum, outnum):
        print("updating with {}".format(innum-outnum))
        self.db.child("building").update({"location1":innum-outnum})
        print("done")


if __name__ == "__main__":
    conn = ST_Connection("config.yaml")
    conn.read_data()


