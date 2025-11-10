import asyncio
import logging
import configparser

from src.infra.mqtt.client import AioMqttClient
from src.infra.mqtt.publisher import AioMqttPublisher
from src.infra.mqtt.subscriber import AioMqttSubscriber
from src.service.service import MqttService

logging.basicConfig(level=logging.INFO)

async def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    mqtt_host = config['mqtt']['host']
    mqtt_port = int(config['mqtt']['port'])
    mqtt_id = config['mqtt'].get('client_id', 'ocpp-server')

    aioclient = AioMqttClient(mqtt_host, mqtt_port, mqtt_id)

    async for client in aioclient.context():
        publisher = AioMqttPublisher(client)
        subscriber = AioMqttSubscriber(client)
        service = MqttService(client, publisher, subscriber)
        await service.start()

if __name__ == "__main__":
    asyncio.run(main())