# History Services integration

This integration povides easy way to export history data of any sensor using services

## Services
- Export
- Device tracker export

### Export

Id: 'history_services.export'  
Returns all the historical data of selected entity within given time interval

**Configuration Options:**

| Field | Description | Required | Default | Details |
|---|---|---|---|---|
| `entity_id` | Any entity | Yes | - | - |
| `last_hours` | Data from last X hours | Yes | `24` | Min: `1`, Max: `120` |
| `start` | Beginning of the interval | No | - | Datetime object |
| `end` | Ending of the interval | No | - | Datetime object |

### Device tracker export

Id: 'history_services.export_device_tracker'  
Returns historical data of selected entity of the 'device_tracker' domain in the KML file format  
Saves output into file with default location: 'www/history/device_tracker.kml'

**Configuration Options:**

| Field | Description | Required | Default | Details / Example |
|---|---|---|---|---|
| `entity_id` | Device tracker entity | Yes | - | - |
| `last_hours` | Data from last X hours | Yes | `24` | Min: `1`, Max: `120` |
| `start` | Beginning of the interval | No | - | Datetime object |
| `end` | Ending of the interval | No | - | Datetime object |
| `max_gap` | Max gap [s]: A period which is not counted as a break | Yes | `300` | Min: `0`, Max: `3600` |
| `min_radius` | Min radius [m]: A radius in which a group of coords will not be considered a valid path | Yes | `100` | Min: `0`, Max: `1000` |
| `attributes` | Additional attributes to include | No | - | e.g. `timestamp distance length course speed` |
| `directory` | Directory part of save location of the tracking data | No | - | e.g. `www/history/` |
| `filename` | File name part of save location of the tracking data | No | - | e.g. `device_tracker` |

## Installation

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=davidrapan&repository=ha-history&category=integration)

### HACS (Manually)
- Follow the link [here](https://hacs.xyz/docs/faq/custom_repositories/)
- Add custom repository: https://github.com/davidrapan/ha-history
- Select type of the category: integration
- Find newly added History Services, open it and then click on the DOWNLOAD button

### Manually
- Copy the contents of 'custom_components/history_services' directory into the Home Assistant with exactly the same hirearchy withing the '/config' directory
