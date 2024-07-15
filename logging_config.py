import logging

def setup_logging():
	logging.basicConfig(
        level=logging.INFO,  # Установите уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()])