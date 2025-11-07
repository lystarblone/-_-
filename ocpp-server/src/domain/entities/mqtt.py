from dataclasses import dataclass
from typing import Optional
import aiomqtt
from src.domain.enums import MqttTopics, MqttQos

@dataclass
class MqttClient:
    hostname: str
    port: int
    client_id: str
    client: aiomqtt.Client | None = None

@dataclass
class MqttTopic:
    name: MqttTopics
    qos: Optional[MqttQos] = MqttQos.AT_MOST_ONCE
    
@dataclass
class MqttMessage:
    topic: MqttTopics
    payload: str | bytes
    qos: Optional[MqttQos] = MqttQos.AT_MOST_ONCE
    retain: Optional[bool] = False