import pytest
from unittest.mock import AsyncMock
from src.infra.mqtt.publisher import AioMqttPublisher
from src.domain.entities.mqtt import MqttTopics, MqttQos

class DummyMessage:
    def __init__(self, topic, payload, qos, retain):
        self.topic = topic
        self.payload = payload
        self.qos = qos
        self.retain = retain

@pytest.mark.asyncio
async def test_publish():
    mock_aiomqtt_client = AsyncMock()
    publisher = AioMqttPublisher(mock_aiomqtt_client)

    message = DummyMessage(
        topic=MqttTopics.CHARGE_POINT_DATA.value,
        payload='test_payload',
        qos=MqttQos.AT_MOST_ONCE.value,
        retain=False
    )
    await publisher.publish_message(message)
    mock_aiomqtt_client.publish.assert_awaited_once_with(
        MqttTopics.CHARGE_POINT_DATA.value, 'test_payload',
        qos=MqttQos.AT_MOST_ONCE.value, retain=False
    )