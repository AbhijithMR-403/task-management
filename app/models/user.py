from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, DeclarativeBase
from datetime import datetime
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    # updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # tokens = relationship("Token", back_populates="user", cascade="all, delete-orphan")


# class Token(Base):
#     __tablename__ = "tokens"

#     id = Column(Integer, primary_key=True, index=True)
#     token = Column(String, unique=True, index=True, nullable=False)
#     created_at = Column(DateTime, default=datetime.now)
#     expires_at = Column(DateTime, nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"))

#     user = relationship("User", back_populates="tokens")
