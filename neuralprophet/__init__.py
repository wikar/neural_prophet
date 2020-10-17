import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('logs.log', 'w+')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.INFO)
# Create formatters and add it to handlers
c_format = logging.Formatter('%(levelname)s - %(name)s - %(funcName)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s  - %(funcName)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
# Add handlers to the logger
log.addHandler(c_handler)
log.addHandler(f_handler)

from neural_prophet import NeuralProphet
