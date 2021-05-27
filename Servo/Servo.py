import machine
i2c = machine.I2C(-1, scl = machine.Pin('X5'),sda=machine.Pin('X4'))
import pca9685
pca = pca9685.PCA9685(i2c)
pca.duty(1,4095)


//pca9685
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 60	
pca.channels[0].duty_cycle = 0x7fff

//servo
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50
servo7 = servo.Servo(pca.channels[7])
for i in range(180):
servo7.angle = i
for i in range(180):
servo7.angle = 180 - i
pca.deinit()