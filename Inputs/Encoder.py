from cvzone.SerialModule import SerialObject
import cv2
import numpy as np

arduino1 = SerialObject() #("Arduino MKR1000")

imgLedOn = cv2.imread("../Resources/LedOn.jpg")
imgLedOff = cv2.imread("../Resources/LedOff.jpg")
pin13Off = cv2.imread("../Resources/Pin13Off.jpg")
pin13On = cv2.imread("../Resources/Pin13On.jpg")

while True:

    result = arduino1.getData()
    potentiometer = cv2.imread("../Resources/Potentiometer.jpg")
    print(result[0], result[1])
    try:
        val = str(int((int(result[1]) + 100)/2))
        valButton = result[0]

        if int(val) < 10:
            cv2.putText(potentiometer, val.zfill(1), (300, 280), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
            #Здесь: putText(картинка на которую нужно поместить текст, количество знаков в тексте, (начальная координата X, начальная координата Y), cv2.название шрифта, масштаб, (R, G, B), толщина)
        elif int(val) >= 10 & int(val) < 100:
            cv2.putText(potentiometer, val.zfill(2), (283, 280), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
        elif int(val) == 100:
            cv2.putText(potentiometer, val.zfill(3), (266, 280), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

        if val != '0':
            # -100 to +100
            # -90 to 270
            val = np.interp(int(val), [0, 100], [-90, 270])
            cv2.ellipse(potentiometer, (320, 265), (131, 131), 0, -90, val, (255, 180, 0), 27)
            #Вписать элипс (потому, что он позволяет строить арки) в имидж с центром 320х265, осями 131, 131, нулевой угол 0 сместить на -90 град (начать сверху)
            #преобразованными данными val, цветом (255, 180, 0), толщиной 27

    except:
        pass

    cv2.imshow("Image", potentiometer)
    cv2.waitKey(1)

    if  int(valButton) == 0:

        cv2.imshow("Image1", imgLedOff)
        cv2.imshow("Image2", pin13Off)
        cv2.waitKey(1)

    elif int(valButton) == 1:
        cv2.imshow("Image1", imgLedOn)
        cv2.imshow("Image2", pin13On)
        cv2.waitKey(1)
