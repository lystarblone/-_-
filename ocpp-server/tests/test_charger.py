import pytest
import websockets
import json

@pytest.mark.asyncio
async def test_boot_notification():
    ws_url = "ws://localhost:9000/CHARGERTEST"
    async with websockets.connect(ws_url, subprotocols=["ocpp1.6"]) as ws:
        call_id = "123456"
        call_msg = [
            2,
            call_id,
            "BootNotification",
            {
                "chargePointVendor": "Test",
                "chargePointModel": "TestModel"
            }
        ]
        await ws.send(json.dumps(call_msg))
        response = await ws.recv()
        print("BootNotification response:", response)
        assert "Accepted" in response