import asyncio
import logging
import configparser
from src.service.service import MqttService
from src.infra.mqtt.client import AioMqttClient
from src.infra.mqtt.publisher import AioMqttPublisher
from src.infra.mqtt.subscriber import AioMqttSubscriber
from src.domain.entities.mqtt import MqttClient

logging.basicConfig(level=logging.INFO)

async def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    mqtt_host = config['mqtt']['host']
    mqtt_port = int(config['mqtt']['port'])
    mqtt_id = config['mqtt'].get('client_id', 'ocpp-server')

    mqtt_client = MqttClient(hostname=mqtt_host, port=mqtt_port, client_id=mqtt_id)
    aioclient = AioMqttClient(mqtt_client)
    publisher = AioMqttPublisher(aioclient)
    subscriber = AioMqttSubscriber(aioclient)

    service = MqttService(aioclient, publisher, subscriber)
    await service.start()

if __name__ == "__main__":
    asyncio.run(main())