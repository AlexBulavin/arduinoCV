__author__ = 'Alex Bulavin'

# import cv2
# import serial
# import os
# import time
#
# ser = serial.Serial("/dev/cu.usbserial-120", baudrate=115200, timeout=1)
#
# image_folder = "QR_Rresources"
# image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".jpg")])
#
# # Формируем буфер изображений в оперативной памяти
# image_buffer = [cv2.imread(os.path.join(image_folder, file)) for file in image_files]
#
# current_image_index = 0
# # Определите желаемые координаты для размещения окна и текста
# window_x, window_y = 600, 1300
# text_x, text_y = 500, 990
# # Создайте окно с изображением и переместите его на указанные координаты
# cv2.namedWindow("Current Image", cv2.WINDOW_NORMAL)
# cv2.moveWindow("Current Image", window_x, window_y)
#
# img = image_buffer[current_image_index]
# cv2.imshow("Current Image", img)
# cv2.waitKey(1)
# time.sleep(5)  # Пауза для начального ожидания
#
# start_recognition_time = None
# counter = 0
# max_diff_time = 0
# min_diff_time = float('inf')
# sum_diff_time = 0
#
# try:
#     while True:
#         data = ser.readline().decode().strip()
#         print(f"Полученные данные: {data}")
#
#         if data.isdigit():
#             counter += 1
#             recognized_value = int(data)
#
#             current_file_number = int(os.path.splitext(image_files[current_image_index])[0])
#             print("Line 51 recognized_value = ", recognized_value, "\ncurrent_file_number = ", current_file_number)
#
#             if recognized_value == current_file_number:
#                 print(f"Распознавание успешно для изображения {current_image_index}: {recognized_value}")
#
#                 if start_recognition_time is None:
#                     start_recognition_time = time.time()
#
#                 current_time = time.time()
#                 diff_time = current_time - start_recognition_time
#                 sum_diff_time += diff_time
#
#                 if diff_time > max_diff_time:
#                     max_diff_time = diff_time
#
#                 if diff_time < min_diff_time:
#                     min_diff_time = diff_time
#
#                 print(f"Время для изображения {current_image_index}: {diff_time:.4f} секунд")
#
#                 start_recognition_time = time.time()
#
#                 current_image_index += 1
#                 if current_image_index < len(image_files):
#                     print("current_image_index = ", current_image_index)
#                     print("Пытаемся загрузить следующий имидж: ",
#                           f"QR_Rresources/{current_image_index}.jpg")
#                     # Добавляем текст с текущими координатами в шапку контейнера
#                     cv2.putText(img, f"Coordinates: ({window_x}, {window_y})",
#                                 (text_x, text_y),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),
#                                 2, cv2.LINE_AA)
#
#                     img = image_buffer[current_image_index]
#                     img_name = f"QR_Rresources/{current_image_index}.jpg"
#                     cv2.imshow(img_name, img)
#                     cv2.waitKey(1)  # Добавляем ожидание для корректного отображения
#                 else:
#                     print("Все изображения распознаны. Завершение.")
#                     break
#             else:
#                 print(f"Распознавание не удалось. Ожидалось {current_file_number}, получено {recognized_value}")
#
# except KeyboardInterrupt:
#     pass
#
# finally:
#     ser.close()
#
# if counter > 0:
#     avg_diff_time = sum_diff_time / counter
#     print(f"Среднее время распознавания: {avg_diff_time:.4f} секунд")
#     print(f"Максимальное время распознавания: {max_diff_time:.4f} секунд")
#     print(f"Минимальное время распознавания: {min_diff_time:.4f} секунд")
#
# cv2.destroyAllWindows()
import cv2
import serial
import os
import time

ser = serial.Serial("/dev/cu.usbserial-120", baudrate=115200, timeout=1)

image_folder = "QR_Rresources"
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".jpg")])

# Формируем буфер изображений в оперативной памяти
image_buffer = [cv2.imread(os.path.join(image_folder, file)) for file in image_files]

current_image_index = 0
# Определите желаемые координаты для размещения окна и текста
window_x, window_y = 600, 1300
text_x, text_y = 500, 990
# Создайте окно с изображением и переместите его на указанные координаты
cv2.namedWindow("Current Image", cv2.WINDOW_NORMAL)
cv2.moveWindow("Current Image", window_x, window_y)

img = image_buffer[current_image_index]
cv2.imshow("Current Image", img)
cv2.waitKey(1)
time.sleep(5)  # Пауза для начального ожидания

start_recognition_time = None
counter = 0
max_diff_time = 0
min_diff_time = float('inf')
sum_diff_time = 0

try:
    while True:
        data = ser.readline().decode().strip()
        print(f"Полученные данные: {data}")

        if data.isdigit():
            counter += 1
            recognized_value = int(data)

            current_file_number = int(os.path.splitext(image_files[current_image_index])[0])
            print("Line 51 recognized_value = ", recognized_value, "\ncurrent_file_number = ", current_file_number)

            if recognized_value == current_file_number:
                print(f"Распознавание успешно для изображения {current_image_index}: {recognized_value}")

                if start_recognition_time is None:
                    start_recognition_time = time.time()

                current_time = time.time()
                diff_time = current_time - start_recognition_time
                sum_diff_time += diff_time

                if diff_time > max_diff_time:
                    max_diff_time = diff_time

                if diff_time < min_diff_time:
                    min_diff_time = diff_time

                print(f"Время для изображения {current_image_index}: {diff_time:.4f} секунд")

                start_recognition_time = time.time()

                current_image_index += 1
                if current_image_index < len(image_files):
                    print("current_image_index = ", current_image_index)
                    print("Пытаемся загрузить следующий имидж: ",
                          f"QR_Rresources/{current_image_index}.jpg")
                    # Добавляем текст с текущими координатами в шапку контейнера
                    cv2.putText(img, f"Coordinates: ({window_x}, {window_y})",
                                (text_x, text_y),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),
                                2, cv2.LINE_AA)

                    img = image_buffer[current_image_index]

                    # Внутри цикла, перед отображением нового изображения
                    img_name = f"QR_Rresources/{current_image_index}.jpg"
                    cv2.setWindowTitle("Current Image", img_name)
                    cv2.imshow("Current Image", img)
                    cv2.waitKey(1)
                    cv2.waitKey(1)  # Добавляем ожидание для корректного отображения
                else:
                    print("Все изображения распознаны. Завершение.")
                    break
            else:
                print(f"Распознавание не удалось. Ожидалось {current_file_number}, получено {recognized_value}")

except KeyboardInterrupt:
    pass

finally:
    ser.close()

if counter > 0:
    avg_diff_time = sum_diff_time / counter
    print(f"Среднее время распознавания: {avg_diff_time:.4f} секунд")
    print(f"Максимальное время распознавания: {max_diff_time:.4f} секунд")
    print(f"Минимальное время распознавания: {min_diff_time:.4f} секунд")

cv2.destroyAllWindows()
