from pyax12.connection import Connection
from serial_port_handler import Search_for_the_serial_port as port_in_use
import time





class Dynamixel():
    def __init__(self):
        # Dynamixel serial port
        dynamixel_serial_port = port_in_use()
        self.baud_rate = 1000000
        self.timeout = 20
        # Connect to the serial port
        self.serial_connection = Connection(
            port=dynamixel_serial_port,
             baudrate=self.baud_rate, 
             timeout=self.timeout,
             waiting_time=0.02, rpi_gpio=False)
        
        print('Connected to the serial port')
        scan_results = self.scan()
        
    

    def scan(self):
        # Ping the dynamixel unit(s)
        print('Scanning for connected Dynamixel units...')
        
        self.control_table = []
        connected_baudrates = []
        ids_available = self.serial_connection.scan()
        ids = []
        for dynamixel_id in ids_available:
            ids.append(dynamixel_id)
            
            # self.gotodegree(dynamixel_id, position=102)
            # time.sleep(1.5)
            # current = self.currentposition(dynamixel_id)
            try:
                self.serial_connection.pretty_print_control_table(dynamixel_id=dynamixel_id)
                connected_baudrates.append(self.serial_connection.get_baud_rate(dynamixel_id))
            except:
                pass

        self.connected_ids = [('id: %s'%id,'baudrate: %s'%baudr) for id,baudr in zip(ids, connected_baudrates)]
        print('Connected Dynamixel Units: {}'.format(self.connected_ids)) 
        return self.connected_ids


    def gotodegree(self, dynamixel_id, position, speed=100, degrees=True):
        current = self.currentposition(dynamixel_id, degrees=degrees)
        self.control_table = self.serial_connection.get_control_table_tuple(dynamixel_id)
        
        for d in self.control_table:
            if d[0] == 'cw_angle_limit':
                min_position = float(d[1][:4])
            if d[0] == 'ccw_angle_limit':    
                max_position = float(d[1][:3])


        
        if min_position < position+current < max_position:
            goal_position = position+current
        elif position+current < min_position:
            goal_position = position-current
        else:
            goal_position = position-current
        print('Moving to position: ', goal_position)
        # Go to the specified position in degrees
        self.serial_connection.goto(dynamixel_id, goal_position, speed=speed, degrees=degrees)

        print('Waiting for movement to finish...')
        while True:
            time.sleep(0.1)
            if self.is_moving_status(dynamixel_id=dynamixel_id):
                break
            else: pass




    def currentposition(self, dynamixel_id, degrees=True):
        # Get the current position
        current_position = self.serial_connection.get_present_position(dynamixel_id, degrees=degrees)
        print('Current position: ', current_position,'\n')
        return current_position

    def is_moving_status(self, dynamixel_id):
        is_moving = self.serial_connection.get_control_table_tuple(dynamixel_id)[-3][1]
        if is_moving == 'no':
                print( 'Movement finished. Stopping...')
                return True
        else:
            print('Still moving...')
            return False
    


if __name__ == '__main__':
  
    Dynamixel()

    

