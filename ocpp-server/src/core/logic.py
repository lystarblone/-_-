import logging

logger = logging.getLogger("Logic")

def process_boot_notification(station_id, vendor, model):
    logger.info(f"Booted station {station_id}: {vendor}, {model}")

def process_authorize(station_id, id_tag):
    logger.info(f"Authorize request: {id_tag} on station {station_id}")
    return id_tag == "VALID"

def process_start_transaction(station_id, connector_id, id_tag):
    logger.info(f"StartTransaction: {station_id} connector {connector_id} id_tag {id_tag}")
    return hash((station_id, connector_id, id_tag))

def process_meter_values(station_id, connector_id, meter_value):
    logger.info(f"MeterValues: {station_id} connector {connector_id} value {meter_value}")

def process_status_notification(station_id, connector_id, status, error_code=None):
    msg = f"StatusNotification: {station_id} connector {connector_id} status {status}"
    if error_code:
        msg += f" error: {error_code}"
    logger.info(msg)