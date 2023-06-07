from machine import UART,Pin, SoftI2C,PWM
from pn532 import Pn532
import ssd1306
import time
def clear(self):
    oled.fill(0)
    oled.show()
    
p2 = PWM(Pin(2))
p2.freq(50)

i2c = SoftI2C(scl=Pin(18),sda=Pin(19))

# 宽度高度
oled_width = 128
oled_height = 64

# 创建oled屏幕对象
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.text('Welcome To Use', 10, 20)
oled.show()
time.sleep(1)
oled.text('By anopy', 30, 30)
oled.show()
time.sleep(3)

# oled预填充设定，0为纯黑，1为纯白
oled.fill(0)

# 应用填充
oled.show()

oled.text('Waiting Card...',13,30)
oled.show()

from machine import freq
from pn532 import Pn532
u1 = UART(1,115200,rx=13,tx=12)
a = Pn532(u1)
uid = a.find_card(0)
uid_str = str(uid)
uid_str = uid_str[3:8]
ad_list = [uid_str,"Z\x05"]
while True:
    clear(0)
    oled.text('Waiting Card...',15,30)
    oled.show()
    uid = a.find_card(0)
    uid_str = str(uid)
    u = uid_str[5:8]
    if u == 'x05':
        p2.duty_u16(4915)
        clear(0)
        oled.text('Unlocked!',30,30)
        oled.show()
        time.sleep(5)
        p2.duty_u16(1638) # 舵机复位
        time.sleep(1)
        clear(0)
    else:
        clear(0)
        oled.text('Failed!',30,20)
        oled.show()
        oled.text('Try again!',20,30)
        oled.show()
        time.sleep(3)
