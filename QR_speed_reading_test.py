__author__ = 'Alex Bulavin'

from cvzone.SerialModule import SerialObject
import cv2
import time
import serial

#ser = serial.Serial('/dev/cu.usbserial-1430', 2000000, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser = serial.Serial('/dev/cu.usbserial-1430', timeout=None, baudrate=115200, xonxoff=False, rtscts=False, dsrdtr=False)
ser.flushInput()
ser.flushOutput()

#port = SerialObject("/dev/cu.usbserial-1431") #("Arduino MKR1000")

max_diff_time = 0
sum_time = 0
img = cv2.imread("QR_Rresources/0.jpg")
cv2.imshow("Image", img)
cv2.waitKey(1)
counter = 0
items_in_test = 300

try:

    counter = counter + 1
    print("Test", counter)
    #res = port.getData()
    #print("port.getData() =", res)
    data_raw = ser.readline()
    print("data_raw = ", data_raw)

    #if res != None:
    if data_raw != None:
        start_time = int(round(time.time() * 1000))
        old_time = start_time
        print(data_raw, type(data_raw), "Start time = ", start_time)

        for i in range(items_in_test):
            img = cv2.imread(f"QR_Rresources/{i + 1}.jpg")
            cv2.imshow("Image", img)
            cv2.waitKey(1)  # Отображение х мс, то есть исчезает через x/1000 секунд
            data_raw = ser.readline()
            #res = port.getData()
            print("Код ", i+1, " из", items_in_test)
            if data_raw != None:
                print("data_raw = ", data_raw)
            #if res != None: #Если условие выполняется, меняем кадр
                current_time = int(round(time.time() * 1000))
                diff_time = current_time - old_time
                sum_time = sum_time + diff_time
                if diff_time > max_diff_time:
                    max_diff_time = diff_time
                old_time = current_time
        print("Максимальное время = ", max_diff_time, " миллисекунд на фрейм")
        print("Среднее время = ", sum_time/(items_in_test+1), " миллисекунд на фрейм")

except:
    pass