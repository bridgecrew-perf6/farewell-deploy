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


#SQLALCHEMY_DABASE_URL = "postgresql://postgres:1234!@localhost/SolomonJuliusDatabase"

#engine  = create_engine(
#    SQLALCHEMY_DABASE_URL)

# Remember - storing secrets in plaintext is potentially unsafe. Consider using
# something like https://cloud.google.com/secret-manager/docs/overview to help keep
# secrets secret.
db_user = "farewell-user"
db_pass = "{mJHC52&'f85:3e#"
db_name = "farewell-db"
db_socket_dir = "/cloudsql"
instance_connection_name = "farewell-353911:europe-southwest1:farewell-instance"

engine = create_engine(

    # Equivalent URL:
    # postgresql+pg8000://<db_user>:<db_pass>@/<db_name>
    #                         ?unix_sock=<socket_path>/<cloud_sql_instance_name>/.s.PGSQL.5432
    # Note: Some drivers require the `unix_sock` query parameter to use a different key.
    # For example, 'psycopg2' uses the path set to `host` in order to connect successfully.
    sqlalchemy.engine.url.URL.create(
        drivername="postgresql+pg8000",
        username=db_user,  # e.g. "my-database-user"
        password=db_pass,  # e.g. "my-database-password"
        database=db_name,  # e.g. "my-database-name"
        query={
            "unix_sock": "{}/{}/.s.PGSQL.5432".format(
                db_socket_dir,  # e.g. "/cloudsql"
                instance_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
        }
    )
)

#engine = create_engine(SQLALCHEMY_DABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


