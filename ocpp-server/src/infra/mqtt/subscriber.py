import asyncio
import logging
import json

logger = logging.getLogger(__name__)

class AioMqttSubscriber:
    def __init__(self, client):
        self.client = client
        self._subscribe_queue = asyncio.Queue()

    async def subscribe_to_topic(self, topic: str, qos: int = 0):
        logger.info(f"Subscribing to topic {topic}")
        await self.client.subscribe(topic, qos=qos)

    async def unsubscribe_from_topic(self, topic: str, qos: int = 0):
        logger.info(f"Unsubscribing from topic {topic}")
        await self.client.unsubscribe(topic, qos=qos)

    async def start_consumer_loop(self):
        async for message in self.client.messages:
            try:
                decoded_payload = json.loads(message.payload.decode())
                await self._subscribe_queue.put({
                    "topic": str(message.topic),
                    "payload": decoded_payload
                })
                logger.info(f"MQTT received on {message.topic}")
            except Exception as e:
                logger.error("MQTT consumer error", exc_info=True)

    def get_subscribe_queue(self):
        return self._subscribe_queue