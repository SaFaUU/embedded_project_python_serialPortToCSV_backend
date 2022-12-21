import datetime
import serial.tools.list_ports
from csv import writer

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

# val = input("Select Port: COM")

# for x in range(0, len(portsList)):
#     if portsList[x].startswith("COM" + str(val)):
#         portVar = "COM" + str(val)
#         print(portVar)
portVar = 'COM10'

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        with open('../embedded-project/src/data.csv', 'a', newline='') as f_object:
            currentTime = datetime.datetime.now().strftime("%H:%M:%S")
            writer_object = writer(f_object)
            sendList = packet.decode('utf').rstrip('\n').split(',')
            sendList.append(currentTime)
            print(sendList)
            writer_object.writerow(sendList)

            f_object.close()
