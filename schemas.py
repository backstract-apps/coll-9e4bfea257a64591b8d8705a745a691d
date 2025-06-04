from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: Any
    name: str
    contact_details: str


class ReadUsers(BaseModel):
    id: Any
    name: str
    contact_details: str
    class Config:
        from_attributes = True


class AppointmentTypes(BaseModel):
    id: Any
    name: str
    duration: int


class ReadAppointmentTypes(BaseModel):
    id: Any
    name: str
    duration: int
    class Config:
        from_attributes = True


class Appointments(BaseModel):
    id: Any
    appointment_date_time: Any
    user_id: int
    appointment_type_id: int
    calendar_event_id: str


class ReadAppointments(BaseModel):
    id: Any
    appointment_date_time: Any
    user_id: int
    appointment_type_id: int
    calendar_event_id: str
    class Config:
        from_attributes = True




class PostAppointmentTypes(BaseModel):
    id: int
    name: str
    duration: int

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    id: int
    name: str
    contact_details: str

    class Config:
        from_attributes = True



class PostAppointments(BaseModel):
    id: int
    appointment_date_time: str
    user_id: int
    appointment_type_id: int
    calendar_event_id: str

    class Config:
        from_attributes = True

