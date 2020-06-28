# Smart-feedback-system
This project replaces traditional buttons in Feedback machines with smart sensors.the python codes catchs readings from PIRs (passive infrared sensors) and Raspberry Pi and send each reading as a feedback:
- In [Smart Feedback System- Azure.py](https://github.com/EsraaMaskati/Smart-feedback-system/blob/master/Smart%20Feedback%20System-%20Azure.py) file: to Azure cloud IoT hub, then visualize it by Power BI.
- In [Smart Feedback System- Adafruit.py](https://github.com/EsraaMaskati/Smart-feedback-system/blob/master/Smart%20Feedback%20System-%20Adafruit.py) file: to io.adafruit and disply viualizes in the dashboard.

## [Smart Feedback System- Azure.py](https://github.com/EsraaMaskati/Smart-feedback-system/blob/master/Smart%20Feedback%20System-%20Azure.py) file notes :
Replace the what is bewteen '[]' according to your Azure account as stated below:
```
# Azure IoT Hub
URI = '[your_iot_hub].azure-devices.net'
KEY = '[iothubowner Primary Key]'
IOT_DEVICE_ID = 'ID of the registered IoT device within IoT Hub'
POLICY = 'iothubowner'
```

## [Smart Feedback System- Adafruit.py](https://github.com/EsraaMaskati/Smart-feedback-system/blob/master/Smart%20Feedback%20System-%20Adafruit.py) file notes :
Replace the 'Client' arguments with your IO.adafruit 'Username' and 'Active Key' recpectivly:

```
aio=Client( '[UserName]', '[Active Key]')

```
