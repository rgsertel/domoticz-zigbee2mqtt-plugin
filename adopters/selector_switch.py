import Domoticz
from adopters.adopter import Adopter

class SelectorSwitchAdopter(Adopter):
    SELECTOR_TYPE_BUTTONS = 0
    SELECTOR_TYPE_MENU = 1

    def __init__(self, devices):
        super().__init__(devices)
        self.level_names = ['Off']
        self.selector_style = self.SELECTOR_TYPE_MENU

    def get_level_value(self, level_name):
        level = 0
        for item in self.level_names:
            if (level_name == item):
                return level

            level += 10

        return 0

    def get_level_name(self, message):
        Domoticz.Log('Unable to get device level name, action is not implemented in adapter')

    def create_device(self, unit, device_id, device_name, device_data):
        selector_options = {
            "LevelActions": "",
            "LevelNames": '|'.join(self.level_names),
            "LevelOffHiddden": "false",
            "SelectorStyle": "1"
        }
        
        Domoticz.Debug('Creating selector switch for device with ieeeAddr ' + device_id)
        return Domoticz.Device(DeviceID=device_id, Name=device_name, Unit=unit, TypeName="Selector Switch", Options=selector_options).Create()

    def update_device(self, device, message):
        level_value = str(self.get_level_value(self.get_level_name(message)))
        signal_level = message.get_signal_level()
        battery_level = message.get_battery_level()

        if (battery_level == None):
            battery_level = device.BatteryLevel

        device.Update(nValue=1, sValue=level_value, SignalLevel=signal_level, BatteryLevel=battery_level)