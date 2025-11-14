# Car Telemetry

Комплекс программ для получения телеметрии автомобиля

Файл ***get_car_data.py*** используется для получения списка доступных команд для управления и информации об устройстве

## Список доступных команд управления указанным устройством:

  - getbalance: Запросить баланс SIM-карты
  - hijack: Управление режимом Антиограбление
  - out: Выполнить программу гибкой логики
  - update_position: Запрос координат
  - valet: Управление сервисным режимом
  - general_out_1_on: Включение блокировки двигателя
  - general_out_1_off: Выключение блокировки двигателя
  - general_out_2_on: Включение универсального выхода №2
  - general_out_2_off: Выключение универсального выхода №2

Телеметрия и состояние указанного устройства:

## Основная информация о устройстве
```json
{
  "alias": "Название устройства",
  "type": 3,
  "telephone": "+7XXXXXXXXXX",
  "status": 2,
  "sn": "Серийный номер",
  "typename": "Тип устройства",
  "device_id": 864107076219516,
  "activity_ts": 1762854936,
  "firmware_version": "X.XX.X",
  "functions": ["функция1", "функция2", "..."],
  "battery_type": "volt",
  "reg_date": 1738804610
}
```
Позиционирование (GPS)
```json
{
  "position": {
    "dir": 0,
    "s": 0,
    "sat_qty": 0,
    "ts": 1762853821,
    "x": 30.292718,
    "y": 59.966442,
    "r": 89,
    "is_move": false
  }
}
```
Общие параметры состояния
```json
{
  "common": {
    "gps_lvl": null,
    "gsm_lvl": 31,
    "ctemp": 31,
    "etemp": null,
    "mayak_temp": null,
    "ts": 1762854936,
    "reg_date": 1738804610,
    "heater_liquid_temp": null,
    "heater_air_temp": null,
    "motohours_reset_ts": null,
    "battery": 13.756,
    "battery_type": "volt"
  }
}
```
Баланс SIM-карт
```json
{
  "balance": [
    {
      "key": "active",
      "value": 0,
      "state": 1,
      "operator": "Оператор",
      "currency": "₽",
      "url_payment": "https://...",
      "slot": 1,
      "number": "+7XXXXXXXXXX",
      "ts": 1763117139
    },
    {
      "key": "standby",
      "value": 0,
      "state": 1,
      "operator": "Оператор",
      "currency": "₽",
      "url_payment": "",
      "slot": 2,
      "number": "",
      "ts": 1762854936
    }
  ]
}
```
OBD (диагностика)
```json
{
  "obd": {
    "ts": 1762854936,
    "fuel_litres": null,
    "fuel_percent": null,
    "fuel_ts": null,
    "dist_to_empty": null,
    "fuel_reserve_ts": null,
    "mileage": null,
    "mileage_ts": null
  }
}
```
Состояние устройства
```json
{
  "state": {
    "alarm": false,
    "arm": false,
    "door": false,
    "hbrake": false,
    "ign": false,
    "pbrake": true,
    "run": false,
    "trunk": false,
    "valet": false,
    "webasto": false,
    "r_start": false,
    "dvr": false,
    "superuser": false,
    "relay": false,
    "general_out_1": false,
    "general_out_2": false,
    "general_out_3": null,
    "parking_pay_city": true,
    "parking_pay_auto_stop": true,
    "parking_pay_auto_extend": true,
    "ts": 1762854936
  }
}
```
Состояние сигнализации
```json
{
  "alarm_state": {
    "add_h": false,
    "add_l": false,
    "door": false,
    "hbrake": false,
    "hijack": false,
    "hood": false,
    "run": false,
    "ign": false,
    "pbrake": false,
    "shock_h": false,
    "shock_l": false,
    "tilt": false,
    "trunk": false,
    "ts": 1762854936
  }
}
```
Электрический статус:
```json
{
  "electric_status": {
    "battery_percents": null,
    "battery_wt": null,
    "charging": null
  }
}
```
