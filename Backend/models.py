from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    department = Column(String, nullable=False)
    role = Column(Enum("employee", "admin", name="user_role"), default="employee")
    joined_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    given_shoutouts = relationship("ShoutOut", foreign_keys="ShoutOut.giver_id", back_populates="giver")
    received_shoutouts = relationship("ShoutOut", foreign_keys="ShoutOut.receiver_id", back_populates="receiver")

class ShoutOut(Base):
    __tablename__ = "shoutouts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    giver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    giver_department = Column(String, nullable=False)  # Department of person giving shoutout
    receiver_department = Column(String, nullable=False)  # Department of person receiving shoutout
    category = Column(Enum("teamwork", "innovation", "leadership", "customer_service", "problem_solving", "mentorship", name="shoutout_category"), nullable=False)
    is_public = Column(Enum("public", "department_only", "private", name="visibility_level"), default="public")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    giver = relationship("User", foreign_keys=[giver_id], back_populates="given_shoutouts")
    receiver = relationship("User", foreign_keys=[receiver_id], back_populates="received_shoutouts")
