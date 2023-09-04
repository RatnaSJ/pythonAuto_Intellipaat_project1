import logging


def configure_logger(log_file_path):
    logging.basicConfig(filename=log_file_path, level=logging.DEBUG, filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger('my_app')
    return logger
