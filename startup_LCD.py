import subprocess
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

lcd = Adafruit_CharLCDPlate(busnum = 1)
lcd.backlight(lcd.OFF)


# Very Linux Specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]

lcd.clear()
lcd.backlight(lcd.BLUE)
lcd.message("My IP is: \n" + ipaddr)
sleep(2)
lcd.backlight(lcd.GREEN)
sleep(2)
lcd.backlight(lcd.TEAL)
sleep(2)
lcd.backlight(lcd.VIOLET)
sleep(2)
lcd.backlight(lcd.YELLOW)
exit()
