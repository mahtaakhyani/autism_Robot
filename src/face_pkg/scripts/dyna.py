#!/usr/bin/env python3
from dynamixel_sdk import *
import math
import time

class motors():
    def __init__(self):
        # Control table address
        self.ADDR_MX_TORQUE_ENABLE      = 24               # Control table address is different in Dynamixel model
        self.ADDR_MX_MOVE_SPEED         = 32
        self.ADDR_MX_CW_ANGLE_LIMIT     = 6
        self.ADDR_MX_CCW_ANGLE_LIMIT    = 8 
        self.ADDR_MX_PRESENT_POSITION   = 36
        self.ADDR_MX_GOAL_POSITION      = 30
        self.ADDR_MX_TORQUE_LIMIT       = 34

        # Data Byte Length
        self.LEN_MX_MOVE_SPEED          = 2

        # Protocol version
        self.PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel

        # Default setting
        self.DXL1_ID                     = 1    #foot                
        self.DXL2_ID                     = 16   #foot                 
        self.DXL3_ID                     = 28   #foot

        self.DXL4_ID                     = 3    #head up_down  toque 350   (posiotion 445 - 600)
        self.DXL5_ID                     = 18   #head left_right  toque 200   (posiotion 780 - 220)
        
        self.DXL6_ID                     = 13    #right hand  toque 200   (posiotion 10 - 1020)
        self.DXL7_ID                     = 14   #left hand  toque 200   (posiotion 10 - 1020)

        self.BAUDRATE                    = 1000000             # Dynamixel default baudrate : 57600
        self.DEVICENAME                  = '/dev/ttyUSB0'    # Check which port is being used on your controller
                                                        # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

        self.TORQUE_ENABLE               = 1                 # Value for enabling the torque
        self.TORQUE_DISABLE              = 0                 # Value for disabling the torque
        self.DXL_MINIMUM_POSITION_VALUE  = 100           # Dynamixel will rotate between this value
        self.DXL_MAXIMUM_POSITION_VALUE  = 1023            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
        self.DXL_MOVING_STATUS_THRESHOLD = 20                # Dynamixel moving status threshold
        # Initialize PortHandler instance
        # Set the port path
        # Get methods and members of PortHandlerLinux or PortHandlerWindows
        self.portHandler = PortHandler(self.DEVICENAME)

        # Initialize PacketHandler instance
        # Set the protocol version
        # Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
        self.packetHandler = PacketHandler(self.PROTOCOL_VERSION)

        # Initialize GroupSyncWrite instance
        self.groupSyncWrite = GroupSyncWrite(self.portHandler, self.packetHandler, self.ADDR_MX_MOVE_SPEED, self.LEN_MX_MOVE_SPEED)

        # Open port
        self.portHandler.openPort()


        # Set port baudrate
        self.portHandler.setBaudRate(self.BAUDRATE)

        self.set_wheel_mode(self.DXL1_ID)
        self.set_wheel_mode(self.DXL2_ID)
        self.set_wheel_mode(self.DXL3_ID)

        self.set_joint_mode(self.DXL4_ID)
        self.set_joint_mode(self.DXL5_ID)
        
        self.set_joint_mode(self.DXL6_ID)
        self.set_joint_mode(self.DXL7_ID)

        
        self.enable_torque(self.DXL1_ID)
        self.enable_torque(self.DXL2_ID)
        self.enable_torque(self.DXL3_ID)

        self.set_torque_limit(self.DXL4_ID, 300)
        self.enable_torque(self.DXL4_ID)
        self.packetHandler.write2ByteTxRx(self.portHandler, self.DXL4_ID, self.ADDR_MX_GOAL_POSITION, 530)
        
        self.set_torque_limit(self.DXL5_ID, 400)
        self.enable_torque(self.DXL5_ID)
        self.packetHandler.write2ByteTxRx(self.portHandler, self.DXL5_ID, self.ADDR_MX_GOAL_POSITION, 500)

        
        self.set_torque_limit(self.DXL6_ID, 200)
        self.enable_torque(self.DXL6_ID)
        self.packetHandler.write2ByteTxRx(self.portHandler, self.DXL6_ID, self.ADDR_MX_GOAL_POSITION, 200)
        
        self.set_torque_limit(self.DXL7_ID, 200)
        self.enable_torque(self.DXL7_ID)
        self.packetHandler.write2ByteTxRx(self.portHandler, self.DXL7_ID, self.ADDR_MX_GOAL_POSITION, 874)


        zero = self.prepare_packet(0)
        self.groupSyncWrite.addParam(self.DXL3_ID, zero)
        self.groupSyncWrite.addParam(self.DXL2_ID, zero)
        self.groupSyncWrite.addParam(self.DXL1_ID, zero)
        self.groupSyncWrite.txPacket()
        self.groupSyncWrite.clearParam()

        # self.head(600, 0)   #PAAK SHAVAD!!!!



    def set_wheel_mode(self, ID):
        self.packetHandler.write2ByteTxRx(self.portHandler, ID, self.ADDR_MX_CW_ANGLE_LIMIT, 0)
        self.packetHandler.write2ByteTxRx(self.portHandler, ID, self.ADDR_MX_CCW_ANGLE_LIMIT, 0)

    def set_joint_mode(self, ID):
        self.packetHandler.write2ByteTxRx(self.portHandler, ID, self.ADDR_MX_CW_ANGLE_LIMIT, 0)
        self.packetHandler.write2ByteTxRx(self.portHandler, ID, self.ADDR_MX_CCW_ANGLE_LIMIT, 1023)

    def set_torque_limit(self, ID, torque):
        self.packetHandler.write2ByteTxRx(self.portHandler, ID, self.ADDR_MX_TORQUE_LIMIT, torque)

    def enable_torque(self, ID):
        self.packetHandler.write1ByteTxRx(self.portHandler, ID, self.ADDR_MX_TORQUE_ENABLE, self.TORQUE_ENABLE)

    def disable_torque(self, ID):
        self.packetHandler.write1ByteTxRx(self.portHandler, ID, self.ADDR_MX_TORQUE_ENABLE, self.TORQUE_DISABLE)

    def prepare_packet(self, speed):
        return [DXL_LOBYTE(int(speed)), DXL_HIBYTE(int(speed))]

    def map(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def constrain(self, value, min, max):
        if value >= max:    return max
        elif value <= min:  return min
        else:               return value

    def map_dyna(self, value):
        if value >= 0:  return value + 1024
        elif value < 0: return -1 * value

    def stop_motors(self):
        self.disable_torque(self.DXL1_ID)
        self.disable_torque(self.DXL2_ID)
        self.disable_torque(self.DXL3_ID)


    def head(self, pos, dir):
        # dir is pan or tilt
        # pos is the position
        if dir == 0: 
            pos = self.constrain(pos, 445, 600)
            self.packetHandler.write2ByteTxRx(self.portHandler, self.DXL4_ID, self.ADDR_MX_GOAL_POSITION, pos)
        elif dir == 1:
            pos = self.constrain(pos, 220, 780)
            self.packetHandler.write2ByteTxRx(self.portHandler, self.DXL5_ID, self.ADDR_MX_GOAL_POSITION, pos)


        # dxl_present_position, junk, junk = self.packetHandler.read2ByteTxRx(self.portHandler, self.DXL4_ID, self.ADDR_MX_PRESENT_POSITION)


    def hand(self,pos,dir):

        if dir == 0:
            pos = self.constrain(pos, 10, 1020)
            self.packetHandler.write2ByteTxRx(self.portHandler, self.DXL6_ID, self.ADDR_MX_GOAL_POSITION, pos)
        elif dir == 1:
            pos = self.constrain(pos, 10, 1020)
            self.packetHandler.write2ByteTxRx(self.portHandler, self.DXL7_ID, self.ADDR_MX_GOAL_POSITION, pos)



    def move(self, speed, theta, yaw):

        Vx = speed * math.cos(theta * math.pi / 180)
        Vy = speed * math.sin(theta * math.pi / 180)

        A = -Vx
        B = 0.5 * Vx - 0.866 * Vy
        C = 0.5 * Vx + 0.866 * Vy
        


        A = self.constrain(A + yaw, -500, 500)
        B = self.constrain(B + yaw, -500, 500)
        C = self.constrain(C + yaw, -500, 500)

        A = self.map(A, -500, 500, -1023, 1023)
        B = self.map(B, -500, 500, -1023, 1023)
        C = self.map(C, -500, 500, -1023, 1023)

        A = self.map_dyna(A)
        B = self.map_dyna(B)
        C = self.map_dyna(C)
        
        A = self.prepare_packet(A)
        B = self.prepare_packet(B)
        C = self.prepare_packet(C)

        self.groupSyncWrite.addParam(self.DXL3_ID, A)
        self.groupSyncWrite.addParam(self.DXL2_ID, B)
        self.groupSyncWrite.addParam(self.DXL1_ID, C)

        self.groupSyncWrite.txPacket()


        self.groupSyncWrite.clearParam()



        

        

    

    
if __name__ == "__main__":
    motors()
