import Domoticz
from devices.device import Device

class KwhSensor(Device):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="kWh").Create()

    def get_numeric_value(self, value, device):
        return int(value)

    def get_string_value(self, value, device):
        return str(value)

    