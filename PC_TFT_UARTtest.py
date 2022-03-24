# pip install pyserial

import time
from datetime import datetime
import serial

def send_data(start_p,end_p,steps):
    a=start_p
    while  a!=end_p+steps  :
        msg='S,'+(str(a)+',')*12
        if a<50 :
            msg=msg+'0,0,0,'
        elif a<80 :
            msg=msg+'1,1,1,'
        else :
            msg=msg+'2,2,2,'
        msg=msg+(datetime.now().strftime('%S')) + ','
        msg=msg+(datetime.now().strftime('%f')[:-3]) + ',E'
        print(msg)
        ser.write(bytes( msg, encoding='ascii'))
        a=a+steps
        time.sleep(intervalA/1000)

    
intervalA=190
a=0
ser =  serial.Serial('COM4', 115200, timeout=0.1)  
# 'COM4':according to your environment
time.sleep(6)

send_data(1,50,1)
send_data(49,30,-1)
send_data(31,100,1)
send_data(99,0,-1)
ser.close()