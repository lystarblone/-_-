print("SERVER FILE RUNNED!!!", __file__)

import asyncio
import websockets
from datetime import datetime

from ocpp.routing import on
from ocpp.v16 import ChargePoint as Cp
from ocpp.v16.call_result import BootNotification
from ocpp.v16.enums import RegistrationStatus


class TestChargePoint(Cp):
    @on("BootNotification")
    async def on_boot_notification(self, charge_point_vendor, charge_point_model, **kwargs):
        print(f"BootNotification от {self.id}: {charge_point_vendor} {charge_point_model}")
        return BootNotification(
            status=RegistrationStatus.accepted,
            current_time=datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
            interval=300,
        )


async def on_connect(websocket, path):
    print(f"Accepted client: {path}")
    cp_id = path.strip("/")
    if not cp_id:
        await websocket.close(1008, "Empty ID")
        return

    cp = TestChargePoint(cp_id, websocket)
    try:
        await cp.start()
    except Exception as e:
        import traceback
        print("SERVER EXCEPTION:", e)
        traceback.print_exc()


async def main():
    print("OCPP Test Server → ws://localhost:9000 (websockets 10.0 + ocpp 2.0.0)")
    async with websockets.serve(
        on_connect,
        "localhost",
        9000,
        subprotocols=["ocpp1.6"],
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())