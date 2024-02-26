"""Module for defining the Complaint class."""

from pydantic import BaseModel
from datetime import datetime

class Complaint(BaseModel):
    """Abstract base class for the complaint object."""
    # primary information
    id: int
    description: str
    country: str

    # metadata
    date_received: datetime
    date_occurred: datetime
    owned_by: str


def region_from_country(country: str, tracer: dict) -> str:
    """Return the region from the country."""
    if country in tracer:
        return tracer[country]
    

class ParentRecord(Complaint):
    """A subclass to represent the parent record object."""
    def __init__(self, id, description, country, date_received, date_occurred, owned_by):
        self.parent_id = id
        self.event_description = description
        self.country_of_origin = country
        self.region = self.region_from_country(country)
        self.receipt_date = date_received
        self.event_date = date_occurred
        self.assigned_to = owned_by

        #super().__init__(id, description, country, date_received, date_occurred, owned_by)