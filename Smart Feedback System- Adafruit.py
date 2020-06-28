#PIR and LED code using adafruit library and feeds
import board
import time
import digitalio
from Adafruit_IO import *

aio=Client( '[UserName]', '[Active Key]')
feeds_g=aio.feeds('GoodFeeds')
feeds_y=aio.feeds('AverageFeeds')
feeds_r=aio.feeds('PoorFeeds')

# Setup digital input for PIR sensors:
pir_g = digitalio.DigitalInOut(board.D14)
pir_g.direction = digitalio.Direction.INPUT
pir_y = digitalio.DigitalInOut(board.D18)
pir_y.direction = digitalio.Direction.INPUT
pir_r = digitalio.DigitalInOut(board.D24)
pir_r.direction = digitalio.Direction.INPUT

# Setup digital output for LEDs:
led_g = digitalio.DigitalInOut(board.D15)
led_g.direction = digitalio.Direction.OUTPUT
led_y = digitalio.DigitalInOut(board.D23)
led_y.direction = digitalio.Direction.OUTPUT
led_r = digitalio.DigitalInOut(board.D25)
led_r.direction = digitalio.Direction.OUTPUT


print ("Sensor initializing . . .")
time.sleep(2) #Give sensor time to startup
print ("Active")
print ("Press Ctrl+c to end program")


value=" depends !! "
try:
        while True:
                if pir_g.value == True: #If PIR pin goes high, motion is detect$
                        print ("Motion Detected! Green")
                        led_g.value = True #Turn on LED
                        time.sleep(2) #Keep LED on for 4 seconds
                        led_g.value = False #Turn off LED
                        time.sleep(0.2)
                        value="Good"
                        aio.send(feeds_g.key,value)
                        
                elif pir_y.value == True: #If PIR pin goes high, motion is detect$
                        print ("Motion Detected! Yellow")
                        led_y.value = True #Turn on LED
                        time.sleep(2) #Keep LED on for 4 seconds
                        led_y.value = False #Turn off LED
                        time.sleep(0.2)
                        value="Average"
                        aio.send(feeds_y.key,value)

                elif pir_r.value == True: #If PIR pin goes high, motion is detect$
                        print ("Motion Detected! Red")
                        led_r.value = True #Turn on LED
                        time.sleep(2) #Keep LED on for 4 seconds
                        led_r.value = False #Turn off LED
                        time.sleep(0.2)
                        value="Poor"
                        aio.send(feeds_g.key,value)


except KeyboardInterrupt: #Ctrl+c
        pass #Do nothing, continue to finally



finally:
        led_g.value = False  #Turn off LED
        led_y.value = False  #Turn off LED
        led_r.value = False  #Turn off LED
        print ("Program ended")

