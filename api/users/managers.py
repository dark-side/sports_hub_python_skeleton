"""User manager."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.models import User
from api.users.security import get_password_hash


class UserManager:
    """User manager."""

    def __init__(self, session: AsyncSession):
        """Initialize user manager."""
        self.session = session

    async def create_user(
        self,
        email: str,
        password: str,
        password_confirmation: str,
        commit: bool = False,
    ) -> User:
        """Create a new user."""
        if password != password_confirmation:
            raise ValueError("Passwords do not match")

        # Check if user already exists
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        if result.scalar_one_or_none():
            raise ValueError("User with this email already exists")

        user = User(
            email=email,
            password_hash=get_password_hash(password),
        )
        self.session.add(user)

        if commit:
            await self.session.commit()
            await self.session.refresh(user)

        return user

    async def get_user_by_email(self, email: str) -> User | None:
        """Get user by email."""
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def list_users(self) -> list[User]:
        """List all users."""
        result = await self.session.execute(select(User))
        return list(result.scalars().all())

    async def get_user_by_id(self, user_id: int) -> User | None:
        """Get user by ID."""
        result = await self.session.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()
