__author__ = 'Alex Bulavin'

from cvzone.SerialModule import SerialObject
import cv2
import time
import serial

port = SerialObject("/dev/cu.usbserial-1430") #("Arduino MKR1000")
#serial.Serial(self.portNo, self.baudRate)
# com=serial.Serial('COM7',9600)
# com.write('on')

com = serial.Serial("/dev/cu.usbserial-1430", 115200)
#com.write('on')

#port.Serial()
max_diff_time = 0

img = cv2.imread("QR_Rresources/0.jpg")
cv2.imshow("Image", img)
cv2.waitKey(1)

while True:

    try:
        #res = port.getData()
        res = com.getData()
        print("port.getData() =", int(res))
        if res != None:
            start_time = int(round(time.time() * 1000))
            old_time = start_time
            print(res, "Start time = ", start_time)

            for i in range(299):

                img = cv2.imread(f"QR_Rresources/{i + 1}.jpg")
                cv2.imshow("Image", img)
                cv2.waitKey(0)  # Отображение х мс, то есть исчезает через x/1000 секунд
                if int(port.getData()) == i: #Если условие выполняется, меняем кадр
                    current_time = int(round(time.time() * 1000))
                    diff_time = current_time - old_time
                    sum_time = sum_time + diff_time
                    if diff_time > max_diff_time:
                        max_diff_time = diff_time
                    old_time = current_time
            print("Max time = ", max_diff_time)
        print("Average time = ", sum_time/300)

    except:
        pass