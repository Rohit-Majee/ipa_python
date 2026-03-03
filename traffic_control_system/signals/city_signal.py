from signals.base_signal import TrafficSignal
from app_logger import logger


from config import (
    CITY_SIGNAL_TRAFFIC_LIMIT ,
    CITY_LOW_GREEN_LIMIT,
    CITY_HIGH_GREEN_LIMIT
)

class CitySignal(TrafficSignal):

    def green_time(self):
        logger.info(f"Calculate green time for highway signal")
        if self.vehicle_count < CITY_SIGNAL_TRAFFIC_LIMIT:
            return CITY_LOW_GREEN_LIMIT
        else:
            return CITY_HIGH_GREEN_LIMIT
        

    def signal_type(self):
        return "City Signal" 