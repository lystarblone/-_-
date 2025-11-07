import asyncio
import logging
from src.infra.mqtt.client import AioMqttClient
from src.infra.mqtt.publisher import AioMqttPublisher
from src.infra.mqtt.subscriber import AioMqttSubscriber
from src.domain.enums import MqttTopics

logger = logging.getLogger("Service")
STATION_COUNT = 10

class MqttService:
    def __init__(self, aioclient: AioMqttClient, publisher: AioMqttPublisher, subscriber: AioMqttSubscriber):
        self.aioclient = aioclient
        self.publisher = publisher
        self.subscriber = subscriber

    async def start(self):
        logger.info("Starting MQTT service")
        await self.aioclient.connect()
        await self._subscribe_to_station_topics()
        await self.publisher.start_producer_loop()
        await self.subscriber.start_consumer_loop()

    async def stop(self):
        logger.info("Stopping MQTT service")
        await self.publisher.stop_producer_loop()
        await self.subscriber.stop_consumer_loop()
        await self.aioclient.disconnect()

    async def _subscribe_to_station_topics(self):
        logger.info(f"Subscribing to topics for {STATION_COUNT} stations")
        for station_id in range(STATION_COUNT):
            await self.subscriber.subscribe_to_topic(
                MqttTopics.PANEL_STATION_IDENTIFIER.format(id=station_id))
            await self.subscriber.subscribe_to_topic(
                MqttTopics.PANEL_STATION_LIMITS_CURRENT.format(id=station_id))
            await self.subscriber.subscribe_to_topic(
                MqttTopics.SAFETY_INPUT_ENDSTOP.format(id=station_id))
            await self.subscriber.subscribe_to_topic(
                MqttTopics.SAFETY_INPUT_EMERGENCY.format(id=station_id))
            await self.subscriber.subscribe_to_topic(
                MqttTopics.SAFETY_INPUT_FLOODING.format(id=station_id))
            await self.subscriber.subscribe_to_topic(
                MqttTopics.SAFETY_INPUT_FIRE.format(id=station_id))