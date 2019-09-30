import configparser

config = configparser.ConfigParser()
config.read('../pyproject.toml')
__version__ = config['tool.poetry']['version'][1:-1]
