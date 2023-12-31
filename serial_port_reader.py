__author__ = 'Alex Bulavin'
import serial

# Укажите правильный путь к вашему серийному порту и настройки (скорость передачи, таймаут и т. д.)
ser = serial.Serial("/dev/cu.usbserial-120", baudrate=115200, timeout=1)

try:
    while True:
        data = ser.readline().decode().strip()
        print(f"Received data: {data}")
except KeyboardInterrupt:
    # Завершение программы по нажатию Ctrl+C
    pass
finally:
    ser.close()
