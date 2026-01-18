"""
Pydantic models for validating Spanish sentences with subjects, verbs, and objects.
"""

from enum import Enum
from pydantic import BaseModel, field_validator
from typing import Optional


# Enum es una clase especial en la que definen todos los valores posibles
class VerbEnding(str, Enum):
    """Spanish infinitive verb endings."""
    AR = "ar"
    ER = "er"
    IR = "ir"


class SpanishVerb(BaseModel):
    """Model for validating a Spanish infinitive verb."""

    infinitive: str

    @field_validator("infinitive")
    @classmethod
    def must_be_infinitive(cls, v: str) -> str:
        v = v.lower().strip()
        valid_endings = [ending.value for ending in VerbEnding]
        if not any(v.endswith(ending) for ending in valid_endings):
            raise ValueError(f"Verb '{v}' must end in -ar, -er, or -ir")
        return v

    @property
    def ending(self) -> VerbEnding:
        """Return the verb ending as an enum."""
        for ending in VerbEnding:
            if self.infinitive.endswith(ending.value):
                return ending
        raise ValueError("Invalid verb ending")


class DirectObject(BaseModel):
    """
    Direct object - answers 'what?' or 'whom?' (el objeto directo)
    Example: "Yo como [una manzana]" - I eat [an apple]
    """
    value: str

    @field_validator("value")
    @classmethod
    def not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Direct object cannot be empty")
        return v


class IndirectObject(BaseModel):
    """
    Indirect object - answers 'to whom?' or 'for whom?' (el objeto indirecto)
    Example: "Yo doy una manzana [a mi madre]" - I give an apple [to my mother]
    """
    value: str

    @field_validator("value")
    @classmethod
    def not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Indirect object cannot be empty")
        return v


class SpanishSentence(BaseModel):
    """
    Model for a Spanish sentence with subject, verb, and optional objects.

    Components:
        - subject: Who performs the action (required)
        - verb: The action in infinitive form (required)
        - direct_object: What/whom receives the action (optional)
        - indirect_object: To/for whom the action is done (optional)
    """

    subject: str
    verb: SpanishVerb
    direct_object: Optional[DirectObject] = None
    indirect_object: Optional[IndirectObject] = None

    @field_validator("subject")
    @classmethod
    def subject_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Subject cannot be empty")
        return v

    def to_sentence(self) -> str:
        """Construct the sentence as a string."""
        parts = [self.subject, self.verb.infinitive]
        if self.direct_object:
            parts.append(self.direct_object.value)
        if self.indirect_object:
            parts.append(self.indirect_object.value)
        return " ".join(parts)
