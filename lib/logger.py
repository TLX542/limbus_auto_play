import logging
import os

# Global logger instance
logger = None


def setup_logging(debug_enabled, script_dir):
    """Setup logging configuration based on debug settings"""
    global logger
    
    log_file = os.path.join(script_dir, 'log.txt')
    
    # Create logger
    logger = logging.getLogger('winrate_debug')
    logger.setLevel(logging.DEBUG if debug_enabled else logging.INFO)
    
    # Clear existing handlers
    logger.handlers.clear()
    
    if debug_enabled:
        # File handler for debug logs
        file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        
        # Add session separator
        logger.info("=" * 50)
        logger.info("NEW DEBUG SESSION STARTED")
        logger.info("=" * 50)
    
    return logger


def debug_log(message):
    """Log debug message if debug logging is enabled"""
    if logger:
        logger.debug(message)


def info_log(message):
    """Log info message if logging is enabled"""
    if logger:
        logger.info(message)