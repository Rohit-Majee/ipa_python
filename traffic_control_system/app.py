from signals.city_signal import CitySignal
from signals.highway_signal import HighwaySignal
from controllers.controller import SignalController
from app_logger import logger


logger.info(f"Traffic Stimulation Started...")

controller = SignalController()
no_vehicle = int(input("Enter number of vehicles: "))
Highway_signal = HighwaySignal(no_vehicle)
city_signal = CitySignal(no_vehicle)

controller.operate(Highway_signal)
controller.operate(city_signal)
    
logger.info(f"Traffic Stimulation completed")
