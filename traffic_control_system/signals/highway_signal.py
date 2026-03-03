from signals.base_signal import TrafficSignal
from app_logger import logger


from config import (
    HIGHWAY_SIGNAL_TRAFFIC_LIMIT ,
    HIGHWAY_LOW_GREEN_LIMIT ,
    HIGHWAY_HIGH_GREEN_LIMIT 
)

class HighwaySignal(TrafficSignal):

    def green_time(self):
        logger.info(f"Calculate green time for highway signal")
        if self.vehicle_count < HIGHWAY_SIGNAL_TRAFFIC_LIMIT:
            return HIGHWAY_LOW_GREEN_LIMIT
        else:
            return HIGHWAY_HIGH_GREEN_LIMIT
        

    def signal_type(self):
        return "Highway Signal" 