import asyncio
import logging
import json
from src.domain.repositories import MqttSubscriberRepo
from src.domain.entities.mqtt import MqttTopic
from src.infra.mqtt.client import AioMqttClient

logger = logging.getLogger(__name__)

class AioMqttSubscriber(MqttSubscriberRepo):
    def __init__(self, aioclient: AioMqttClient):
        self.aioclient = aioclient
        self._subscribe_queue = asyncio.Queue()

    async def subscribe_to_topic(self, topic: MqttTopic) -> None:
        logger.info(f"Subscribing to {topic.name}")
        async with self.aioclient.get_client() as client:
            await client.subscribe(topic.name, topic.qos)

    async def unsubscribe_from_topic(self, topic: MqttTopic) -> None:
        logger.info(f"Unsubscribing from {topic.name}")
        async with self.aioclient.get_client() as client:
            await client.unsubscribe(topic.name)

    async def start_consumer_loop(self) -> None:
        async with self.aioclient.get_client() as client:
            async for message in client.messages:
                try:
                    decoded_payload = json.loads(message.payload.decode())
                    await self._subscribe_queue.put({
                        "topic": str(message.topic),
                        "payload": decoded_payload
                    })
                    logger.info(f"MQTT received on {message.topic}")
                except Exception as e:
                    logger.error("MQTT consumer error", exc_info=True)

    async def stop_consumer_loop(self) -> None:
        self._subscribe_queue.join()
        self._subscribe_queue.task_done()
    
    def get_subscribe_queue(self) -> asyncio.Queue:
        return self._subscribe_queue