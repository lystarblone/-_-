from src.core.logic import process_meter_values

def test_meter_process(caplog):
    caplog.set_level("INFO", logger="Logic")
    process_meter_values('STATIONTEST', '1', {"value": 42})
    assert "MeterValues" in caplog.text