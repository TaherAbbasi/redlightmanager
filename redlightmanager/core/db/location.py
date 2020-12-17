# coding=utf-8

from sqlalchemy import Column, String, Integer
from .base import Base

class Location(Base):
    __tablename__ = 'location'

    name_en = Column(String(50), primary_key=True, nullable=False)
    name_fa = Column(String(50), nullable=False)
    police_code = Column(Integer, nullable=False)
    device_id = Column(Integer)
    extra_id = Column(Integer)

    def __init__(self, name_fa: str, name_en: str, police_code: int,
                 device_id: int, basir_id: int):
        
        self.name_fa = name_fa
        self.name_en = name_en
        self.police_code = police_code
        self.device_id = device_id
        self.basir_id = basir_id
