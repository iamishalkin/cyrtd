import configparser

config = configparser.ConfigParser()
__version__ = config['tool.poetry']['version'][1:-1]
