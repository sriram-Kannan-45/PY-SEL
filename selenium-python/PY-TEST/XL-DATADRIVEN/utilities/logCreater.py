import logging

def log_generator():

    logging.basicConfig(
        filename=r"D:\PY-SEL\selenium-python\PY-TEST\XL-DATADRIVEN\utilities\testLogReports.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True
    )

    return logging.getLogger()