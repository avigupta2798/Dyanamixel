import  bluetooth,time
import Adafruit_BBIO.GPIO as GPIO
search_time=10
led_pin="P8_7"
addr = None
print("Welcome")
if (addr==None):
    try:
        input("To continue, press Enter")
    except SyntaxError:
        pass
    print("Searching for bluetooth device:")
    nearby_devices=bluetooth.discover_devices(duration=search_time,flush_cache=True,lookup_names=True)
    if(len(nearby_devices)>0):
        print("found%ddevices: "%len(nearby_devices))
    else:
        print("No devices found")
        exit(0)
    i=0;
    for addr,name in nearby_devices:
        print("%s.%s-%s"%(i,addr,name))
        i+=1
    device_num=input("please enter the serial no. :")
    addr,name=nearby_devices[device_num][0],nearby_devices[device_num][1]
print("script wil now scan the  device %s."%(addr))
GPIO.setup(led_pin,GPIO.OUT)
while True:
    state = bluetooth.lookup_name(addr,timeout=20)
    services=bluetooth.find_service(address=addr)
    if(state==None and services==[]):
        print("no device detected")
        GPIO.output(led_pin,GPIO.LOW)
    else:
        print("device detected")
        GPIO.output(led_pin,GPIO.HIGH)
    time.sleep(2)