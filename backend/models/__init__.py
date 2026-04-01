"""Models module - database models."""
# from sqlalchemy import Column, Integer, String, Boolean, DateTime
# from sqlalchemy.orm import DeclarativeBase
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String(255), unique=True, index=True, nullable=False)
#     username = Column(String(50), unique=True, index=True, nullable=False)
#     hashed_password = Column(String(255), nullable=False)
#     is_active = Column(Boolean, default=True)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)