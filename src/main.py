import time
import logging
from sensors.mpu_6050 import get_mpu650_sensor_data, is_moving
from iot_core_client import connect, disconnect, publish, subscribe

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def message_callback(topic, payload, **kwargs):
    """Callback display when message received from IoT Core"""
    logger.info(f"Received message from topic {topic}: {payload}")

def main():
    try:
        connect()
        subscribe('test/topic', message_callback) # message topic needs to be changed based on defined topic in IoT Core
        while True:
            accel_data, _ = get_mpu650_sensor_data()
            if is_moving(accel_data):
                magnitude_thresh = is_moving(accel_data)[0]
                logger.info("Movement detected!")
                # Trigger the indoor localization algorithm here
                publish('test/topic', f"Movement detected! - {magnitude_thresh}")
            else:
                magnitude_thresh = is_moving(accel_data)[0]
                logger.info(f"No movement detected. - {magnitude_thresh}")
            time.sleep(2)
    except KeyboardInterrupt:
        logger.info("Program terminated")
    finally:
        disconnect()

if __name__ == "__main__":
    main()
