import os
from cvzone.SerialModule import SerialObject
import cv2
import time
import serial.tools.list_ports as sp

os.system('clear')  # для Unix/Linux/Mac
# Получить список доступных портов
ports = list(sp.comports())
# Вывести информацию о каждом порту
for port in ports:
    print(f"Port: {port.device}, Description: {port.description}")

port = SerialObject("/dev/cu.usbserial-120")  # Заменил ser на port
port.ser.flushInput()
port.ser.flushOutput()

max_diff_time = 0
sum_time = 0
img = cv2.imread("QR_Rresources/0.jpg")
cv2.imshow("Image", img)
cv2.waitKey(1)
counter = 0
items_in_test = 300
time.sleep(3)

while True:
    try:
        print("Test", counter)
        data_raw = port.ser.readline()
        print("Data from port:", data_raw)
        counter = counter + 1

        if data_raw:
            start_time = int(round(time.time() * 1000))
            old_time = start_time
            print("Start time =", start_time)

            for i in range(items_in_test):
                img = cv2.imread(f"QR_Rresources/{i + 1}.jpg")
                cv2.imshow("Image", img)
                cv2.waitKey(0)  # cv2.waitKey(х) Отображение х мс, то есть исчезает через x/1000 секунд

                data_raw = port.ser.readline()
                print("Data from port inside loop:", data_raw)

                current_time = int(round(time.time() * 1000))
                diff_time = current_time - old_time
                sum_time = sum_time + diff_time
                if diff_time > max_diff_time:
                    max_diff_time = diff_time
                old_time = current_time
                print("Max time =", max_diff_time, "миллисекунд на фрейм")
                print("Average time =", sum_time / (items_in_test + 1), "миллисекунд на фрейм")

    except Exception as e:
        print("Error:", e)
    cv2.destroyAllWindows()

