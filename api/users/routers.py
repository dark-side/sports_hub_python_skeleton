"""User routers."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from api.users import schemas
from api.users.dependencies import get_user_manager
from api.users.manager import UserManager

registration_router = APIRouter()

router = APIRouter()


@registration_router.post("/registrations", response_model=schemas.UserRegistrationResponse)
async def create_user(
    payload: schemas.UserRegistrationRequest,
    user_manager: Annotated[UserManager, Depends(get_user_manager)],
):
    """Create a new user."""
    try:
        user = await user_manager.create_user(
            payload.registration.email,
            payload.registration.password,
            payload.registration.password_confirmation,
            commit=True,
        )
    except ValueError as e:
        raise HTTPException(status_code=409, detail=[{"msg": str(e)}]) from e

    r = schemas.UserRegistrationResponse.model_validate(
        user, from_attributes=True
    )
    return r


@router.get("", response_model=list[schemas.UserResponse])
async def list_users(
    user_manager: Annotated[UserManager, Depends(get_user_manager)],
):
    """List all users."""
    users = await user_manager.list_users()
    return [schemas.UserResponse.model_validate(user, from_attributes=True) for user in users]


@router.get("/{user_id}", response_model=schemas.UserResponse)
async def get_user(
    user_id: int,
    user_manager: Annotated[UserManager, Depends(get_user_manager)],
):
    """Get user by ID."""
    user = await user_manager.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return schemas.UserResponse.model_validate(user, from_attributes=True)
