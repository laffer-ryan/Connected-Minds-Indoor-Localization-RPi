import unittest
from unittest.mock import patch, MagicMock
from src import iot_core_client

class TestIoTClient(unittest.TestCase):

    @patch('iot_core_client.mqtt_connection')
    @patch('iot_core_client.logger')
    def test_connect(self, mock_logger, mock_mqtt_connection):
        # Create a mock connect future
        mock_connect_future = MagicMock()
        mock_connect_future.result.return_value = None
        mock_mqtt_connection.connect.return_value = mock_connect_future

        # Run the connect function
        iot_core_client.connect()

        # Assert logger.info was called with expected messages
        mock_logger.info.assert_any_call("Connecting to AWS IoT Core...")
        mock_logger.info.assert_any_call("Connected to AWS IoT Core")

        # Assert mqtt_connection.connect() was called
        mock_mqtt_connection.connect.assert_called_once()

    @patch('iot_core_client.mqtt_connection')
    @patch('iot_core_client.logger')
    def test_disconnect(self, mock_logger, mock_mqtt_connection):
        # Create a mock disconnect future
        mock_disconnect_future = MagicMock()
        mock_disconnect_future.result.return_value = None
        mock_mqtt_connection.disconnect.return_value = mock_disconnect_future
        iot_core_client.connect()
        # Run the disconnect function
        iot_core_client.disconnect()

        # Assert logger.info was called with expected messages
        mock_logger.info.assert_any_call("Disconnecting from AWS IoT Core...")
        mock_logger.info.assert_any_call("Disconnected from AWS IoT Core")

        # Assert mqtt_connection.disconnect() was called
        mock_mqtt_connection.disconnect.assert_called_once()

    @patch('iot_core_client.mqtt_connection')
    @patch('iot_core_client.logger')
    def test_publish(self, mock_logger, mock_mqtt_connection):
        # Mock the publish method
        mock_publish = MagicMock()
        mock_mqtt_connection.publish = mock_publish

        # Run the publish function
        topic = 'test/topic'
        message = 'Test message'
        iot_core_client.publish(topic, message)

        # Assert logger.info was called with expected messages
        mock_logger.info.assert_any_call(f"Publishing message to topic {topic}: {message}")

        # Assert mqtt_connection.publish() was called with expected arguments
        mock_mqtt_connection.publish.assert_called_once_with(
            topic=topic,
            payload=message,
            qos=iot_core_client.mqtt.QoS.AT_LEAST_ONCE
        )

    @patch('iot_core_client.mqtt_connection')
    @patch('iot_core_client.logger')
    def test_subscribe(self, mock_logger, mock_mqtt_connection):
        # Mock the subscribe method
        mock_subscribe_future = MagicMock()
        mock_subscribe_future.result.return_value = None
        mock_mqtt_connection.subscribe.return_value = (mock_subscribe_future, 1)

        # Run the subscribe function
        topic = 'test/topic'
        callback = MagicMock()
        iot_core_client.subscribe(topic, callback)

        # Assert logger.info was called with expected messages
        mock_logger.info.assert_any_call(f"Subscribing to topic {topic}")
        mock_logger.info.assert_any_call(f"Subscribed to topic {topic}")

        # Assert mqtt_connection.subscribe() was called with expected arguments
        mock_mqtt_connection.subscribe.assert_called_once_with(
            topic=topic,
            qos=iot_core_client.mqtt.QoS.AT_LEAST_ONCE,
            callback=callback
        )

if __name__ == '__main__':
    unittest.main()
