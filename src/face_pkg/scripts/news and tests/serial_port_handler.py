import serial
import serial.tools.list_ports
import argparse
import time



baudrate=1000000
timeout=100

def Search_for_the_serial_port():
    global serial_port_in_use

    if args.__getattribute__('port'):
        serial_port_in_use = args.__getattribute__('port')
        print('serial_port_in_use set to ',serial_port_in_use)
        return serial_port_in_use

    available_ports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
    
    for port in available_ports:
        if "USB" in port[1]:
            print('Hmm...%s port is connected.\n'%port[0])

            try:
                test_serial = serial.Serial(
                    port='COM2',
                    baudrate=1000000, 
                    timeout=20)

                test_serial.close()
                test_serial.open()
                time_last = time.time()
                test_serial.close()


                if time.time()-time_last > 10:
                    print('Oh sh** timeout')
                    break
                serial_port_in_use = test_serial.port
            except:
                print('Nope.Not working.\n\n')
    if not serial_port_in_use:
        print('[WARN] No USB Serial is connected!\n [HINT] If you know the port, re-run and set it manually using --port, or enter it below(i.e., COM1, /dev/ttyUSB0):')

        manual_port = input('')
        serial_port_in_use = [manual_port if ('COM' in manual_port or '/dev/' in manual_port) else print('Invalid Input')][0]
        test_serial.close()
        
    if serial_port_in_use: 
        print('serial_port_in_use set to ',serial_port_in_use) 
    else: 
        print('serial_port_in_use set to default "/dev/ttyUSB0"')
        serial_port_in_use="/dev/ttyUSB0", exit()
    return serial_port_in_use
        


if __name__ == "__main__":
    port_in_use = Search_for_the_serial_port()
else:
    error = 'This script is not meant to be imported.'