from smbus2 import SMBus
from mlx90614 import MLX90614
def checktemp():
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)
    temp=sensor.get_object_1()
    return temp
a=checktemp()
print(a)