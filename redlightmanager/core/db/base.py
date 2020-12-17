from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser
import os

config = configparser.ConfigParser()
config_file_path = os.path.abspath(r'redlightmanager\configs\config.ini')

config.read(config_file_path)
dbname = config['REDLIGHT']['dbname'] # database name
username = config['REDLIGHT']['dbuser'] # username
password = config['REDLIGHT']['dbpassword'] # password
host = config['REDLIGHT']['host'] # password
port = config['REDLIGHT']['port'] # password
db_url = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{dbname}'

engine = create_engine(db_url)
                       
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()