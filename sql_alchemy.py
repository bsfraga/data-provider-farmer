from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os

engine = create_engine(f'mariadb://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}/{os.environ["DATA_PROVIDER_DB_NAME"]}')


session = Session(engine)

