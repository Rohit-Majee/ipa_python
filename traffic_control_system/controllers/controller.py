from app_logger import logger

class SignalController:

    def operate(self, signal):
        logger.info(f"Signal Controller started for {signal.signal_type()}")
        time = signal.green_time()
        logger.info(f"Signal Type: {signal.signal_type()}, Green Time: {time} seconds")
        logger.info(f"Signal controller operation completed")


    
