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

db_user = os.environ["DB_USER"]
db_pass = os.environ["DB_PASS"]
db_name = os.environ["DB_NAME"]
db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
instance_connection_name = os.environ["INSTANCE_CONNECTION_NAME"]
db_url = f"postgresql+pg8000://{db_user}:{db_pass}@/{db_name}?unix_sock={db_socket_dir}/{instance_connection_name}/.s.PGSQL.5432"

#username = "farewell-db-user"  # DB username
#password = "farewell-db-password"  # DB password
#host = '34.175.70.254'  # Public IP address for your instance
#port = '8080'
#database = 'farewell-db'  # Name of database ('postgres' by default)

#db_url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
#    username, password, host, port, database)


engine = sqlalchemy.create_engine(db_url)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


