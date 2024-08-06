import os
import logging
import ssl
import time
from dotenv import load_dotenv
from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder


# Load environment variables from .env file
current_dir = os.path.dirname(os.path.realpath(__file__))
env_file_path = os.path.join(current_dir, '..', '.env')

load_dotenv(dotenv_path=env_file_path)


AWS_IOT_CORE_ENDPOINT = os.getenv('AWS_IOT_CORE_ENDPOINT')
AWS_IOT_CORE_CLIENT_ID = os.getenv('AWS_IOT_CORE_CLIENT_ID')
AWS_IOT_CORE_CERT = os.getenv('AWS_IOT_CORE_CERT')
AWS_IOT_CORE_PRIVATE_KEY = os.getenv('AWS_IOT_CORE_PRIVATE_KEY')
AWS_IOT_CORE_ROOT_CA = os.getenv('AWS_IOT_CORE_ROOT_CA')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the AWS IoT SDK
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

# Create MQTT connection from environment
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=AWS_IOT_CORE_ENDPOINT,
    cert_filepath=AWS_IOT_CORE_CERT,
    pri_key_filepath=AWS_IOT_CORE_PRIVATE_KEY,
    ca_filepath=AWS_IOT_CORE_ROOT_CA,
    client_bootstrap=client_bootstrap,
    client_id=AWS_IOT_CORE_CLIENT_ID,
    tls_version=ssl.PROTOCOL_SSLv23,
    clean_session=False,
    keep_alive_secs=6
)

def connect():
    logger.info("Connecting to AWS IoT Core...")
    connect_future = mqtt_connection.connect()
    connect_future.result()
    logger.info("Connected to AWS IoT Core")


def disconnect():
    logger.info("Disconnecting from AWS IoT Core...")
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
    logger.info("Disconnected from AWS IoT Core")


def publish(topic, message):
    logger.info(f"Publishing message to topic {topic}: {message}")
    mqtt_connection.publish(
        topic=topic,
        payload=message,
        qos=mqtt.QoS.AT_LEAST_ONCE
    )

# Subscribe to a topic on AWS IoT Core
def subscribe(topic, callback):
    logger.info(f"Subscribing to topic {topic}")
    subscribe_future, packet_id = mqtt_connection.subscribe(
        topic=topic,
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=callback
    )
    subscribe_future.result()
    logger.info(f"Subscribed to topic {topic}")



connect()
time.sleep(10)
disconnect()
