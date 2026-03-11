from __future__ import annotations

import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

#from homeassistant.config_entries import ConfigEntry

from .services.export import async_register_service as async_register_export_service
from .services.device_tracker import async_register_service as async_register_device_tracker_service

from .const import *

CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    _LOGGER.debug(f'async_setup({config})')
    # If a user has it in config but NOT yet in UI, they might need config entry creation or just legacy support.
    # To keep both working without conflicts, we just register services if they aren't already.
    # The recommended approach for integrations moving to config flow is to let the config flow handle it all,
    # but we can preserve yaml backward compataibliltiy like this.
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = True
        await async_register_export_service(hass)
        await async_register_device_tracker_service(hass)
    return True

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool:
    _LOGGER.debug(f'async_setup_entry({entry.as_dict()})')
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = True
        await async_register_export_service(hass)
        await async_register_device_tracker_service(hass)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool:
    _LOGGER.debug(f'async_unload_entry({entry.as_dict()})')
    # Services in HA are automatically unloaded/removed if no other entities or entries require them,
    # but we can explicitly remove them if needed. For now, returning True unloads the entry cleanly.
    if DOMAIN in hass.data:
        hass.data.pop(DOMAIN)
        hass.services.async_remove(DOMAIN, EXPORT_SERVICE_NAME)
        hass.services.async_remove(DOMAIN, EXPORT_DEVICE_TRACKER_SERVICE_NAME)
    return True