from fastapi import APIRouter, Body, HTTPException, status
from passlib.context import CryptContext

from converter.auth.auth_handler import signJWT
from converter.models.model import UserLoginSchema, UserSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users = []

router = APIRouter()


# helpers


def check_user(data):
    """
    Checks if a an email address is being used
    """
    for user in users:
        if user.email == data.email:
            return True
    return False


def get_user(data: UserLoginSchema):
    """
    Returns a user from the users list
    """
    for user in users:
        if user.email == data.email:
            return user
    return False


def verify_password(plain_password, hashed_password):
    """
    Verifies a users password with the hashed password in storage.
    """
    return pwd_context.verify(plain_password, hashed_password)


# route handlers


@router.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    """
    creates a user and authenticates a user (in memory)
    """
    if check_user(user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User with email already exists",
        )
    user.password = pwd_context.encrypt(user.password)
    users.append(user)
    return signJWT(user.email)


@router.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    """
    Validates a users login credentials
    """
    if check_user(user):
        data = get_user(user)
        if verify_password(user.password, data.password):
            return signJWT(user.email)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect username or password",
        )
