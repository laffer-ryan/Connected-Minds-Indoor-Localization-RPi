# Connected-Minds-Indoor-Localization-RPi

## Project Description
This is a project uses Raspberry Pi's and Ultra Wideband technology with DWM anchors for indoor localization of store assets. The store assests can be tracked when being used by a customer to develop a better understanding of where shoppers congregate within a store and which locations can be better utilized.

This project aims to track customer movement and identify frequently visited aisles in a supermarket-like establishment. The primary method for data collection will involve using a Raspberry Pi system integrated into the shopping cart. 

Existing systems typically track items as they are added to the cart, but this approach primarily provides purchase history based on receipts, which limits the insights to purchase patterns rather than the physical location of items and their relation. Additionally, such methods often raise privacy concerns by tracking customers through their identification.


## Hardware Requirements

| Item                        | Source              | Use                                                                                                                  |
|-----------------------------|---------------------|-----------------------------------------------------|
| 1x Raspberry Pi 4B+         | Provided            | Main device. Fitted inside the cart itself. Used as the dynamic positioning device (tag) to capture data between the (anchors) based on ToF (Time of flight). Fitted with following sensors: |
|                             |                     | - DWM1000 UWB 
| 2x Raspberry Pi 3B+         | Provided            | Used as one of the static beacons (anchor) to broadcast location data to the receiver. Fitted with following sensors:|sensor                                                                                                |
| 1x Raspberry Pi Zero        | Purchased - Ryan    |                                                                                                                      |
| 1x Arduino      | Purchased - Cameron |               |
| 3x DWM1000 UWB sensors      | Purchased         | Ultra-wideband Broadband Sensor. Used for capturing main device position.                       |
| 1x Proximity sensor       | Provided            |                        |
| 1x Tracking sensor          | Provided            |                |
| 1x IR obstacle sensor       | Provided            | Used to identify/avoid immediate obstacles.                    |
| 1x Ultrasonic distance sensor| Provided           |            |
| 1x Time sensor              | Provided            | Used to timestamp signal data sent between the devices.        |
| 1x Breadboard 830-point     | Provided            |               |

