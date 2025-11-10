import aiomqtt
import logging

logger = logging.getLogger(__name__)

class AioMqttClient:
    def __init__(self, hostname, port, client_id):
        self.hostname = hostname
        self.port = port
        self.client_id = client_id

    async def context(self):
        logger.info(f"Connecting to MQTT broker {self.hostname}:{self.port}")
        async with aiomqtt.Client(
            hostname=self.hostname,
            port=self.port,
            identifier=self.client_id,
        ) as client:
            yield client
        logger.info(f"Disconnected from MQTT broker {self.hostname}:{self.port}")