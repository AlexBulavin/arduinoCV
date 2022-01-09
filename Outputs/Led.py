# from cvzone.SerialModule import SerialObject
# import cv2
#
# #Здесь arduino - просто переменная
# arduino = SerialObject() #Автоматически будет искать arduino на com порту. Если не найдёт, нужно указать вручную, взяв его из arduino IsADirectoryError
# #Например, SerialObject("/dev/cu.usbmodem14301") или SerialObject("Arduino MKR1000")
#
# imgLedOn = cv2.imread("../Resources/LedOn.jpg")
# imgLedOff = cv2.imread("../Resources/LedOff.jpg")
# pin13Off = cv2.imread("../Resources/Pin13Off.jpg")
# pin13On = cv2.imread("../Resources/Pin13On.jpg")
# potentiometer = cv2.imread("../Resources/Potentiometer.jpg")
#
# while True:
#     arduino.sendData([1])
#     cv2.imshow("Image1", imgLedOn)
#     cv2.imshow("Image2", pin13On)
#     cv2.waitKey(3000)
#     #sleep(3)
#     arduino.sendData([0])
#     cv2.imshow("Image1", imgLedOff)
#     cv2.imshow("Image2", pin13Off)
#     cv2.waitKey(1000)
#     #sleep(1)