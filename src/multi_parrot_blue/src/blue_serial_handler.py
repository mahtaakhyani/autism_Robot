#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import serial
import serial.tools.list_ports
from multi_parrot_blue.srv import *
import time

parrot_serial = "COM8"
arduino_serial = None
baudrates = 9600


def Search_for_parrot_serial_port():
    global parrot_serial
    available_ports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
    for port in available_ports:
        test_serial = serial.Serial(
            port = port[0],
            baudrate = baudrates,
            timeout = 10
        )
        test_serial.close()
        test_serial.open()
        time_last = time.time()
        
        while True:

            text = test_serial.readline()#.decode('utf-8')
            if text.find('parrot') != -1:
                parrot_serial = test_serial
                print('!!!blue parrot port found on port %s!!!'%port[0])
                break
            else:pass


            if time.time()-time_last > 10:
                print('!!!! this port is not arduino or parrot %s  !!!!'%port[0])
                break


def handle_parrot_connection(req):
    parrot_serial.write(req.command)
    # print(req)
    # return ParrotResponse(parrot_serial.readline().decode('utf-8'))
    return parrot_serial.readline()



def handel_connections():
    rospy.init_node('blue_serial_handler', log_level=rospy.DEBUG)
    parrot_service = rospy.Service('blue_serial_handler/blueparrot', BlueParrot, handle_parrot_connection)
    rospy.spin()

if __name__ == "__main__":
    Search_for_parrot_serial_port()
    print("start the service")
    handel_connections()
