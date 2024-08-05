# Connected-Minds-Indoor-Localization-RPi

## Project Description
This is a project uses Raspberry Pi's and Ultra Wideband technology with DWM anchors for indoor localization of store assets. The store assests can be tracked when being used by a customer to develop a better understanding of where shoppers congregate within a store and which locations can be better utilized.

This project aims to track customer movement and identify frequently visited aisles in a supermarket-like establishment. The primary method for data collection will involve using a Raspberry Pi system integrated into the shopping cart. 

Existing systems typically track items as they are added to the cart, but this approach primarily provides purchase history based on receipts, which limits the insights to purchase patterns rather than the physical location of items and their relation. Additionally, such methods often raise privacy concerns by tracking customers through their identification.


## Test Environment
Test whether gyroscope and accelerometer are attached properly.
Assuming you are located in the Connected_Minds directory run:
    python3 src/gyro_test/mpu_6050_test.py





## Hardware Requirements

| Item                        | Source              | Use                                                                                                                  |
|-----------------------------|---------------------|-----------------------------------------------------|
| 1x Raspberry Pi 4B+         | Provided            | Main device. Fitted inside the cart itself. Used as the dynamic positioning device (tag) to capture data between the (anchors) based on ToF (Time of flight). Fitted with following sensors: |
|                             |                     | - DWM1000 UWB 
| 3x Raspberry Pi 3B+         | Provided            | Used as IoT device to collect data and send to network        |
| 3x DWM1000 UWB sensors      | Purchased         | Ultra-wideband Broadband Sensor. Used for capturing main device position.          |
| 1x MPU 6050    | Provided            |   Sunfounder sensor that includes accelerometer, gyroscope and temperature     |
| 1x Time sensor              | Provided            | Used to timestamp signal data sent between the devices.      |
| 1x Breadboard 830-point     | Provided            | Sensor connection              |




### Configuring Thing with IoT Core

You can set your IAM credentials as environment variables by using the preconfigured names. For Unix systems, you can do the following:

```
export AWS_ACCESS_KEY_ID=<your aws access key id string>
export AWS_SECRET_ACCESS_KEY=<your aws secret access key string>
export AWS_SESSION_TOKEN=<your aws session token string>
```

This will define the PATH variables for a device registered as an IoT Thing