import Domoticz
from devices.device import Device

class HumiditySensor(Device):
    def create_device(self, unit, device_name, options, message):
        return Domoticz.Device(Name=device_name, Unit=unit, TypeName="Humidity", Options=options).Create()

    def get_numeric_value(self, value, device):
        return int(value)

    def get_string_value(self, value, device):
        return '0'

    