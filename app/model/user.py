

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db.database_config import Base

class User(Base):
    __tablename__ = "users"
    # 
    id=Column(Integer,autoincrement=True, primary_key=True, nullable=False, index=True)
    uuid=Column(String,index=True, nullable=False)
    username=Column(String, default="anynomous")
    email=Column(String)
    password=Column(String)
    is_deleted=Column(Boolean, default=False)
    is_verified=Column(Boolean, default=True)
    created_date=Column(DateTime)
    profile=Column(String, default="user.com")
    updated_date=Column(DateTime, default=None)

    # create a constructor
    def __init__(self, uuid, username, email, password, is_deleted, is_verified, created_date, profile=None, updated_date=None):
        self.uuid = uuid
        self.username = username
        self.email = email
        self.password = password
        self.is_deleted = is_deleted
        self.is_verified = is_verified
        self.created_date = created_date
        self.profile = profile
        self.updated_date = updated_date
    