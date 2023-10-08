"""Platform for start integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

def setup_platform(hass, config, add_devices.discovery_info=None):
  add_devices([ExampleSensor()])
class ExampleSensor(Entity):
  
  def name(self):
    return 'Temperature'
  
  def state(self):
    return 23
      
  def unit_of_measurement(self):
    return TEMP_CELSIUS
