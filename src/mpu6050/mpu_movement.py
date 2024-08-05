import time
import math
import logging

from mpu6050 import mpu6050
mpu = mpu6050(0x68)

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# File handler
file_handler = logging.FileHandler('movement_detection.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(file_handler)


# Functionality
def calculate_magnitude(data: dict):
    """
    Calculate the magnitude of the 3D acceleration vector based on Euclidean Distance.

    data: Dictionary of x,y,z data from accelerometer
    """
    return math.sqrt(data['x']**2 + data['y']**2 + data['z']**2)


def is_moving(accel_data: dict, threshold=10):
    """
    Determine if the sensor is moving based on the magnitude of the acceleration vector. Compare it to a defined threshold
    
    accel_data: x, y, and z data from the accelerometer
    threshold: set the minimum value for the accelerometer to consider movement
    """
    magnitude = calculate_magnitude(accel_data)

    ratio = f'Magnitude: {magnitude} - Threshold: {threshold}'
    return ratio, magnitude > threshold

# This may not be required. If the cart is moving and then stops with a second then it sholdn't be considered moving and does not require a location.
def debounce(movement_detected, buffer_size=5):
    """
    Debouncing function filters out noise an ensures smooth movement sensing. 
    Debounce uses the average movement vector removing outliers to ensure movement 
    """
    buffer = [False] * buffer_size
    index = 0
    while True:
        buffer[index] = movement_detected()
        index = (index + 1) % buffer_size
        if all(buffer):
            return True
        time.sleep(0.2)
    return False




# Main thread
def main():
    try:
        while True:
            accel_data = mpu.get_accel_data()
            gyro_data = mpu.get_gyro_data()

            logger.debug(f"Accel Data: {accel_data}")
            logger.debug(f"Gyro Data: {gyro_data}")

            if is_moving(accel_data)[1]:
                magnitude_thresh = is_moving(accel_data)[0]
                logger.info(f"Movement detected! - {magnitude_thresh}")
                # Trigger the indoor localization algorithm here
            else:
                magnitude_thresh = is_moving(accel_data)[0]

                logger.info(f"No movement detected. - {magnitude_thresh}")

            time.sleep(1) # Minimum time period between checking for changes in accel. Not required for production.
    except KeyboardInterrupt:
        logger.info("Program terminated")

if __name__ == "__main__":
    main()