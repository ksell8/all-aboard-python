from typing import List

from pydantic import BaseModel
from datetime import date
from enum import Enum

class Contract (BaseModel):

    personal_data: str
    consent: bool

class RiskEvaluation (BaseModel):

    rating: float

class Parties (BaseModel):

    name: str
    last_name: str

class PrivacyPolicy (BaseModel):

    text: str # the content of the privacy policy
    update_date: date
    delivered_to: list
    complete: bool
    contract: Contract #Absent? -20points

class DataType (Enum):

    BASIC_PERSONAL = "BASIC_PERSONAL"
    SENSITIVE = "SENSITIVE"
    ANONYMIZED = "ANONYMIZED"

class RiskData (BaseModel):

    data_type: DataType
    amount: int
    protected: bool #Is there encryption? Anonymized?

