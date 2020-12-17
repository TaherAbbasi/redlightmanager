import configparser

config = configparser.ConfigParser()
config.read('config.ini')

db_name = config['REDLIGHT']['dbname'] # database name
username = config['REDLIGHT']['dbuser'] # username
password = config['REDLIGHT']['dbpassword'] # password


__all__ = ['db_name', 'username', 'password']