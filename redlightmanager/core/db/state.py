# coding=utf-8

from sqlalchemy import Column, String, Integer
from .base import Base

class State(Base):
    __tablename__ = 'state'

    name = Column(String(20), primary_key=True, nullable=False)
    description = Column(String(100), nullable=False)

    def __init__(self, name: str, description: str):
        
        self.name = name
        self.description = description

