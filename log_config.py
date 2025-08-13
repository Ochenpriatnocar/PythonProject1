import logging
from config import ROOT_DIR

def setup_loger(name, log_file):
    """ Функция логирования других функций"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(filename=f"{ROOT_DIR}/logs/{log_file}", mode="w", encoding="utf-8")
    file_formate = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(lineno)d: %(message)s')
    file_handler.setFormatter(file_formate)
    logger.addHandler(file_handler)
    return logger