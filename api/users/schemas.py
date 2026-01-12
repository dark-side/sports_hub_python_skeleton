"""User schemas."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, field_validator


class UserRegistration(BaseModel):
    """User registration DTO."""

    email: EmailStr
    password: str
    password_confirmation: str

    @field_validator("password_confirmation")
    @classmethod
    def passwords_match(cls, v: str, info) -> str:
        """Validate that passwords match."""
        if "password" in info.data and v != info.data["password"]:
            raise ValueError("Passwords do not match")
        return v


class UserRegistrationRequest(BaseModel):
    """User registration response DTO."""

    registration: UserRegistration


class UserRegistrationResponse(BaseModel):
    """User registration response DTO."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    created_at: datetime
    updated_at: datetime


class UserResponse(BaseModel):
    """User response DTO."""
    
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    email: EmailStr
    created_at: datetime
    updated_at: datetime
