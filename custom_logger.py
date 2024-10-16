import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)8s | %(funcName)s | %(filename)s, %(lineno)d | %(message)s"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger
