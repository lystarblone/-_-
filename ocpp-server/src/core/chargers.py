from ocpp.v16 import ChargePoint as Cp
from ocpp.routing import on
from ocpp.v16.enums import RegistrationStatus, AuthorizationStatus
from datetime import datetime
import logging

from src.core import logic

logger = logging.getLogger("Charger")

class ChargePoint(Cp):
    async def send_boot_notification(self):
        payload = {
            "chargePointVendor": "TestVendor",
            "chargePointModel": "TestModel"
        }
        return await self.call("BootNotification", payload)

    @on("BootNotification")
    async def on_boot_notification(self, charge_point_vendor, charge_point_model, **kwargs):
        logger.info(f"BootNotification {charge_point_vendor} {charge_point_model}")
        logic.process_boot_notification(self.id, charge_point_vendor, charge_point_model)
        return {
            "currentTime": datetime.utcnow().isoformat() + "Z",
            "interval": 20,
            "status": RegistrationStatus.accepted
        }

    @on("Authorize")
    async def on_authorize(self, id_tag, **kwargs):
        result = logic.process_authorize(self.id, id_tag)
        if result:
            return {"idTagInfo": {"status": AuthorizationStatus.accepted}}
        else:
            return {"idTagInfo": {"status": AuthorizationStatus.blocked}}

    @on("StartTransaction")
    async def on_start_transaction(self, connector_id, id_tag, **kwargs):
        txn_id = logic.process_start_transaction(self.id, connector_id, id_tag)
        return {"transactionId": txn_id, "idTagInfo": {"status": AuthorizationStatus.accepted}}

    @on("MeterValues")
    async def on_meter_values(self, connector_id, meter_value, **kwargs):
        logic.process_meter_values(self.id, connector_id, meter_value)
        return {}

    @on("StatusNotification")
    async def on_status_notification(self, connector_id, status, error_code=None, **kwargs):
        logic.process_status_notification(self.id, connector_id, status, error_code)
        return {}