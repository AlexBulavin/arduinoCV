### Необходимо освободить серийный порт от Arduino IDE Serial monitor
Для этого просто выключить монитор серийного порта в Arduino IDE и перезапустить ESP
После чего запустить скрипт на Python

Настроить правильный порт и прописать его в этой строке:
ser = serial.Serial("/dev/cu.usbserial-120", baudrate=115200, timeout=1)

Чтобы узнать какие порты имеются на компе, нужно выполнить вот такой код:
### Импортировать нужную библиотеку
import serial.tools.list_ports as sp
#### Получить список доступных портов
ports = list(sp.comports())
#### Вывести информацию о каждом порту
for port in ports:
    print(f"Port: {port.device}, Description: {port.description}")

### Полный листинг кода:
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

# ГЛАВНОЕ!!!
## Перед запуском скрипта serial_port_reader.py или его аналога ВСЕГДА перезапускаем ESP32-CAM путём отключения от компа и повторного включения!!!
## ИНАЧЕ НЕ РАБОТАЕТ!!!