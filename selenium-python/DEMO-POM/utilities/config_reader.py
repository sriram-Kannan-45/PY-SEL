from configparser import ConfigParser
import os

def get_config(category, key):

    config = ConfigParser()

    base_path = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(base_path, "configure", "config.ini")

    print("Config Path:", config_path)
    print("File Exists:", os.path.exists(config_path))

    config.read(config_path)

    print("Sections:", config.sections())

    return config.get(category, key)