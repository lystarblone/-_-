from enum import Enum

class CpStatus(Enum):
    AVAILABLE = "Available"
    UNAVAILABLE = "Unavailable"
    IN_USE = "InUse"
    ERROR = "Error"
    OTHER = "Other"
    UNKNOWN = "Unknown"

class CmdTypes(Enum):
    POWER = "POWER"
    VOLTAGE = "VOLTAGE"
    CURRENT = "CURRENT"

class EventTypes(Enum):
    BOOT_NOTIFICATION = "BootNotification"
    AUTHORIZATION = "Authorization"
    START_TRANSACTION = "StartTransaction"
    STOP_TRANSACTION = "StopTransaction"
    METER_VALUES = "MeterValues"
    DISCONNECT = "Disconnect"
    HEARTBEAT = "Heartbeat"
    STATUS_NOTIFICATION = "StatusNotification"
    OTHER = "Other"

class MqttTopics(Enum):
    PANEL_STATION_IDENTIFIER = "/panel/station/{id}/IDENTIFIER"
    PANEL_STATION_LIMITS_CURRENT = "/panel/station/{id}/limits/CURRENT"
    SAFETY_INPUT_ENDSTOP = "/safety/input/{id}/ENDSTOP"
    SAFETY_INPUT_EMERGENCY = "/safety/input/{id}/EMERGENCY"
    SAFETY_INPUT_FLOODING = "/safety/input/{id}/FLOODING"
    SAFETY_INPUT_FIRE = "/safety/input/{id}/FIRE"
    CHARGE_POINT_DATA = "/chargepoint/data"

class MqttQos(Enum):
    AT_MOST_ONCE = 0
    AT_LEAST_ONCE = 1
    EXACTLY_ONCE = 2