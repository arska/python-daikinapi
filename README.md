# Daikin Airconditioner/Air source heat pump data/control through Wi-Fi API

[![Python package](https://github.com/arska/python-daikinapi/actions/workflows/main.yml/badge.svg)](https://github.com/arska/python-daikinapi/actions/workflows/main.yml)
[![PyPI version](https://badge.fury.io/py/daikinapi.svg)](https://badge.fury.io/py/daikinapi)

## Compatibility

Tested with Daikin BRP069B41 Wi-Fi Interface and Daikin Emura FTXG-LS indoor unit

Should be compatible with (https://www.daikin.eu/en_us/product-group/control-systems/daikin-online-controller/connectable-units.html):
* BRP069A41/BRP069B41
  * FTXM-M
  * CTXM-M
  * ATXM-M
  * FTXTM-M
  * BRP069A45
  * FTXG-LS
  * FTXG-LW
  * FTXJ-MW (built-in)
  * FTXJ-MS (built-in)
* BRP069A42/BRP069B42
  * FTXZ-N
  * FTXS35-42-50K
  * FTXS60-71G
  * FTX50-60-71GV
  * FTXLS-K3
  * FTXLS-K3
  * FVXS-F
  * FLXS-B
  * FLXS-B9
  * ATXS35-50K
  * FVXM-F
* BRP069A43/BRP069B43
  * CTXS15-35K
  * FTXS20-25K
  * FTX20-25-35J3
  * FTXL-JV
  * ATXS20-25K
  * ATX-J3
  * ATXL-JV

Based on exisiting reverse-engineering work:
* https://github.com/ael-code/daikin-control
* https://github.com/ael-code/daikin-aricon-pylib/
* https://github.com/ael-code/daikin-control/wiki/API-System

## Usage

see example.py for runnable example

```python
from daikinapi import Daikin

API = Daikin("192.168.1.3")
print(API)
print(API.target_temperature)
```

produces:
```
Daikin(host=192.168.1.3,name=mydevice,mac=D0C5D304A0B1)
21.0
```

