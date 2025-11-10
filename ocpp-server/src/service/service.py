import asyncio
import logging
from src.infra.mqtt.publisher import AioMqttPublisher
from src.infra.mqtt.subscriber import AioMqttSubscriber
from src.domain.enums import MqttTopics

logger = logging.getLogger("Service")
STATION_COUNT = 10

class MqttService:
    def __init__(self, client, publisher: AioMqttPublisher, subscriber: AioMqttSubscriber):
        self.client = client
        self.publisher = publisher
        self.subscriber = subscriber

    async def start(self):
        logger.info("Starting MQTT service")
        await self._subscribe_to_station_topics()
        await asyncio.gather(
            self.publisher.start_producer_loop(),
            self.subscriber.start_consumer_loop()
        )

    async def _subscribe_to_station_topics(self):
        logger.info(f"Subscribing to topics for {STATION_COUNT} stations")
        for station_id in range(STATION_COUNT):
            await self.subscriber.subscribe_to_topic(
                MqttTopics.PANEL_STATION_IDENTIFIER.value.format(id=station_id))
            await self.subscriber.subscribe_to_topic(
                MqttTopics.PANEL_STATION_LIMITS_CURRENT.value.format(id=station_id))
            await self.subscriber.subscribe_to_topic(
                MqttTopics.SAFETY_INPUT_ENDSTOP.value.format(id=station_id))
            await self.subscriber.subscribe_to_topic(
                MqttTopics.SAFETY_INPUT_EMERGENCY.value.format(id=station_id))
            await self.subscriber.subscribe_to_topic(
                MqttTopics.SAFETY_INPUT_FLOODING.value.format(id=station_id))
            await self.subscriber.subscribe_to_topic(
                MqttTopics.SAFETY_INPUT_FIRE.value.format(id=station_id))