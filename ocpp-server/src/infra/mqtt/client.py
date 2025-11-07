import aiomqtt
import asyncio
from src.domain.repositories import MqttConnectionRepo
from src.domain.entities.mqtt import MqttClient
import logging

logger = logging.getLogger(__name__)

class AioMqttClient(MqttConnectionRepo):
    def __init__(self, aioclient: MqttClient):
        self.aioclient = aioclient

    def __str__(self):
        return f"AioMqttClient({self.aioclient.hostname}:{self.aioclient.port})"

    async def connect(self) -> None:
        logger.info(f"Connecting to MQTT broker {str(self.aioclient)}")
        await self.aioclient.client.connect(
            self.aioclient.hostname, 
            self.aioclient.port, 
            self.aioclient.client_id
        )
        await self.aioclient.client.__aenter__()

    async def disconnect(self) -> None:
        logger.info(f"Disconnecting from MQTT broker {str(self.aioclient)}")
        await self.aioclient.client.disconnect()
        await self.aioclient.client.__aexit__(None, None, None)

    async def is_connected(self) -> bool:
        if self.aioclient.client is None:
            logger.error("MQTT client not connected")
            return False
        return True

    def get_client(self) -> aiomqtt.Client:
        if not self.aioclient.client:
            logger.error("MQTT client not connected")
            raise RuntimeError("MQTT client not connected")
        return self.aioclient.client