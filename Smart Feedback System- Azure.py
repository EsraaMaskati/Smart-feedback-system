from base64 import b64encode, b64decode
from hashlib import sha256
from urllib import quote_plus, urlencode
from hmac import HMAC
import requests
import json
import os
import time
import RPi.GPIO as GPIO



# Azure IoT Hub
URI = '[your_iot_hub].azure-devices.net'
KEY = '[iothubowner Primary Key]'
IOT_DEVICE_ID = 'ID of the registered IoT device within IoT Hub'
POLICY = 'iothubowner'


# Helpfull connection functions
def generate_sas_token():
    expiry=3600
    ttl = time.time() + expiry
    sign_key = "%s\n%d" % ((quote_plus(URI)), int(ttl))
    signature = b64encode(HMAC(b64decode(KEY), sign_key, sha256).digest())
    rawtoken = {
        'sr' :  URI,
        'sig': signature,
        'se' : str(int(ttl))
    }
    rawtoken['skn'] = POLICY
    return 'SharedAccessSignature ' + urlencode(rawtoken)



def send_message(token, message):
    url = 'https://{0}/devices/{1}/messages/events?api-version=2016-11-14'.format(URI, IOT_DEVICE_ID)
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = json.dumps(message)
    print (data)
    response = requests.post(url, data=data, headers=headers)

y = ''
g=''
r=''
def read_y(pir_y):
    if GPIO.input(pir_y) == True: #If PIR pin goes high, motion is detect$
        y = 'Average'
        print ("Motion Detected! yellow")
        GPIO.output(led_y, True) #Turn on LED
        time.sleep(2) #Keep LED on for 4 seconds
        GPIO.output(led_y, False) #Turn off LED
        time.sleep(0.2)
    return y

def read_g(pir_g):
    if GPIO.input(pir_g) == True: #If PIR pin goes high, motion is detect$
        g = 'Good'
        print ("Motion Detected! Green")
        GPIO.output(led_g, True) #Turn on LED
        time.sleep(2) #Keep LED on for 4 seconds
        GPIO.output(led_g, False) #Turn off LED
        time.sleep(0.2)
    return g

def read_r(pir_r):
    if GPIO.input(pir_r) == True: #If PIR pin goes high, motion is detect$
        r = 'Poor'
        print ("Motion Detected! Red")
        GPIO.output(led_r, True) #Turn on LED
        time.sleep(2) #Keep LED on for 4 seconds
        GPIO.output(led_r, False) #Turn off LED
        time.sleep(0.2)
    return r


if __name__ == '__main__':

    
    # 1.  Hardware settings
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD) #Set GPIO to pin numbering

    pir_g = 8 #Assign pin 8 to PIR
    led_g = 10 #Assign pin 10 to LED

    pir_y= 12
    led_y=16

    pir_r=18
    led_r=22

    GPIO.setup(pir_r, GPIO.IN) #Setup GPIO pin PIR as input
    GPIO.setup(led_r, GPIO.OUT) #Setup GPIO pin for LED as output

    GPIO.setup(pir_y, GPIO.IN)
    GPIO.setup(led_y, GPIO.OUT)

    GPIO.setup(pir_g, GPIO.IN)
    GPIO.setup(led_g, GPIO.OUT)

    

    

    # 2. Program initializing
    print ("Sensor initializing . . .")
    time.sleep(2) #Give sensor time to startup
    print ("Active")
    print ("Press Ctrl+c to end program")


    # 3. Generate SAS Token
    token = generate_sas_token()

    try:
        while True:
            yellow=read_y(pir_y)
            green=read_g(pir_g)
            red=read_r(pir_r)
             if (len(yellow)> 0):
                message_y = { "Yellow ": yellow }
                send_message(token, message_g)               
             elif (len(green)> 0):
                message_g = { "Green ": green }
                send_message(token, message_g)
             elif (len(red)> 0):
                message_r = { "Red ": red }
                send_message(token, message_r)
            time.sleep(1)
            
    except KeyboardInterrupt: #Ctrl+c
        pass #Do nothing, continue to finally
    
    finally:
        GPIO.output(led_r, False) #Turn off LED in case left on
        GPIO.output(led_y, False) #Turn off LED
        GPIO.output(led_g, False) #Turn off LED
        GPIO.cleanup() #reset all GPIO
        print ("Program ended")
     
