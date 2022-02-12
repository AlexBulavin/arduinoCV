__author__ = 'Alex Bulavin'

import qrcode

i = 0
qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 2,
    error_correction = qrcode.constants.ERROR_CORRECT_Q
)
#Параметр version может быть от 1 до 40, от 21х21 до 177х177 пикселей, не учитывая поля.

#Параметр box_size отвечает за количество пикселей в каждом квадрате QR-кода.

#Параметр border создает границу вокруг QR-кода.

#Параметр Error_correction служит для восстановления кода, если код повредился и плохо читаем.

#Каждый уровень указывает на процент данных для восстановления.
#ERROR_CORRECT_L = 7%
#ERROR_CORRECT_M = 15%
#ERROR_CORRECT_Q = 25%
#ERROR_CORRECT_H = 30%
while i <= 0:
    qr_data = i

    qr.add_data(qr_data)
    # img = qr.make_image(back_color=(47, 48, 70), fill_color=(255, 255, 255)).convert(
    #     'RGB')  # Задаём параметры для файла и конвертируем в RGB чтобы логотип был цветным
    img1 = qr.make_image()
    # pos = (
    #     (img.size[0] - logo.size[0]) // 2,
    #     (img.size[1] - logo.size[1]) // 2,
    # )
    # # img.paste(logo, pos)
    img1.save(f'QR_Rresources/{qr_data}.jpg', 'JPEG')  # Указываем папку в которую нужно сохранить файл
    qr.clear()
    i = i + 1
