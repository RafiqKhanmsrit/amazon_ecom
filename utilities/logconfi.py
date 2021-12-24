import logging


class Loggen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\B24\\PycharmProjects\\ecom\\Logfiles\\automation.log")
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger


