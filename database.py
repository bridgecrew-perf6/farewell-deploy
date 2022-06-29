from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os 
import cloudinary
import cloudinary.uploader
import cloudinary.api
import sqlalchemy

cloudinary.config( 
  cloud_name = "dxhdxbedp", 
  api_key = "552497812426217", 
  api_secret = "HTsyA53RosfW3btxsZF_qKS1hQU",
)

#Pw: {mJHC52&'f85:3e#
#userpw: -rf.l<[9ti|Cx6)i

#SQLALCHEMY_DABASE_URL = "sqlite:///./solomon.db"


username = "farewell-user"  # DB username
password = "-rf.l<[9ti|Cx6)i"  # DB password
host = '34.175.70.254'  # Public IP address for your instance
port = '8080'
database = 'farewell-db'  # Name of database ('postgres' by default)

db_url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
    username, password, host, port, database)

engine = sqlalchemy.create_engine(db_url)

#engine = create_engine(SQLALCHEMY_DABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


