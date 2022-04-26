import logging
import os.path

logger = logging.getLogger('chat.client')

formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(module)-8s - %(message)s ")

log_store = 'log-storage'
if not os.path.exists(log_store):
    os.mkdir(log_store)
filename = os.path.join(log_store, 'chat.client.log')

log_file = logging.FileHandler(filename, encoding='utf-8')
log_file.setLevel(logging.DEBUG)
log_file.setFormatter(formatter)

logger.addHandler(log_file)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Test...')
