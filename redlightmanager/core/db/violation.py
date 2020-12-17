from sqlalchemy import String, Integer, Date, DateTime, Column, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Violation(Base):
    __tablename__= 'violation'

    path = Column(String(100), nullable=False, primary_key=True)
    plate_number = Column(String(100), nullable=False)
    plate_number_ocr = Column(String(100))
    occurence_datetime = Column(DateTime, nullable=False)
    send_datetime = Column(DateTime)
    response_code = Column(Integer)
    response_token = Column(String(100))
    redlight_time = Column(Integer) # in milliseconds
    state = Column(String(20), ForeignKey('state.name'))
    violation_type = Column(String(20), ForeignKey('violation_type.name_en'))
    location = Column(String(100), ForeignKey('location.name_en'))
    camera_no = Column(Integer)

    __table_args__ = (UniqueConstraint('occurence_datetime',
                      'redlight_time'),)

    def __init__(self, path: str, plate_number: str,
                 occurence_datetime: str, send_datetime: str,
                 response_code: int, response_token: str,
                 redlight_time: int, state: str, violation_type: str,
                 location: str, camera_no: int):
        
        self.path = path
        self.plate_number = plate_number
        self.occurence_datetime = occurence_datetime
        self.send_datetime = send_datetime
        self.response_code = response_code
        self.response_token = response_token
        self.redlight_time = redlight_time
        self.state = state
        self.violation_type = violation_type
        self.location = location
        self.camera_no = camera_no
