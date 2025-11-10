import asyncio
import logging

logger = logging.getLogger(__name__)

class AioMqttPublisher:
    def __init__(self, client):
        self.client = client
        self._publish_queue = asyncio.Queue()

    async def publish_message(self, message):
        logger.info(f"Publishing MQTT message {message.topic}")
        try:
            await self.client.publish(
                message.topic,
                message.payload,
                qos=message.qos,
                retain=message.retain
            )
            logger.info(f"MQTT Published {message.topic} with payload {message.payload}")
        except Exception as e:
            logger.error("MQTT publish error", exc_info=True)

    async def start_producer_loop(self):
        while True:
            message = await self._publish_queue.get()
            await self.publish_message(message)
            self._publish_queue.task_done()

    def get_publish_queue(self):
        return self._publish_queue