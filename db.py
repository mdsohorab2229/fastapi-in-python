from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



# DATABASE_URL="mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL="mysql+pymysql://root:@localhost:3307/sms"


engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit =False, autoflush=False, bind=engine)
base = declarative_base()


# def get_connection():
#     db = session_local
#     try:
#         yield db
#     finally:
#         db.close    