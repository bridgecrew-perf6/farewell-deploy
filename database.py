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

#SQLALCHEMY_URL = \ 



#username = "farewell-db-user"  # DB username
#password = "farewell-db-password"  # DB password
#host = '34.175.70.254'  # Public IP address for your instance
#port = '8080'
#database = 'farewell-db'  # Name of database ('postgres' by default)

#db_url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
#    username, password, host, port, database)

#print(db_url)

#engine = sqlalchemy.create_engine(db_url)

engine = sqlalchemy.create_engine(

    # Equivalent URL:
    # postgresql+pg8000://<db_user>:<db_pass>@/<db_name>
    #                         ?unix_sock=<socket_path>/<cloud_sql_instance_name>/.s.PGSQL.5432
    # Note: Some drivers require the `unix_sock` query parameter to use a different key.
    # For example, 'psycopg2' uses the path set to `host` in order to connect successfully.
    sqlalchemy.engine.url.URL.create(
        drivername="postgresql+pg8000",
        username="farewell-db-user",  # e.g. "my-database-user"
        password="farewell-db-password",  # e.g. "my-database-password"
        database="farewell-db",  # e.g. "my-database-name"
        query={
            "unix_sock": "{}/{}/.s.PGSQL.5432".format(
                "/cloudsql",  # e.g. "/cloudsql"
                "farewell-353911:europe-southwest1:farewell-instance")  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
        }
    )
)




SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


