import aiomqtt
import asyncio
import logging
from src.domain.repositories import MqttPublisherRepo
from src.domain.entities.mqtt import MqttMessage
from src.infra.mqtt.client import AioMqttClient

logger = logging.getLogger(__name__)

class AioMqttPublisher(MqttPublisherRepo):
    def __init__(self, aioclient: AioMqttClient):
        self.aioclient = aioclient
        self._publish_queue = asyncio.Queue()

    async def publish_message(self, message: MqttMessage) -> None:
        logger.info(f"Publishing MQTT message {message.topic}")
        try:
            await self.aioclient.get_client().publish(
                message.topic,
                message.payload,
                message.qos,
                message.retain
            )
        except Exception as e:
            logger.error("MQTT publish error", exc_info=True)
        logger.info(f"MQTT Published {message.topic} with payload {message.payload}")
    
    async def start_producer_loop(self) -> None:
        while True:
            message = await self._publish_queue.get()
            await self.publish_message(message)
            self._publish_queue.task_done()

    async def stop_producer_loop(self) -> None:
        self._publish_queue.join()
        self._publish_queue.task_done()
    
    def get_publish_queue(self) -> asyncio.Queue:
        return self._publish_queue