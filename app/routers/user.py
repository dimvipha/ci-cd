from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database_config import get_session
from app.db.schema.user import CreatUser, UpdateUser
from app.db.crud.user import get_all_users, create_user, update_user, delete_user,get_user_by_uuid
from app.db.schema.base import BaseReponse
from datetime import datetime


user_router = APIRouter()

@user_router.get("/api/v1/users")
async def get_users(db:AsyncSession=Depends(get_session)):
    return BaseReponse(
        status_code=200,
        timestamp= datetime.now(),
        data=await get_all_users(db),
        message="Get all Users"
    )

@user_router.post("/api/v1/users")
async def add_user(user_data:CreatUser, db:AsyncSession=Depends(get_session)):
    return BaseReponse(
        status_code=200,
        timestamp= datetime.now(),
        data=await create_user(user_data, db),
        message="Created user successfully"
    )
    

@user_router.put("/api/v1/users/{user_uuid}")
async def update_user_by_uuid(user_uuid: str,update_user_data: UpdateUser, db:AsyncSession=Depends(get_session)):
    return BaseReponse(
        status_code=200,
        timestamp= datetime.now(),
        data=await update_user(user_uuid,update_user_data, db),
        message="Updated user successfully"
    )

@user_router.delete("/api/v1/users/{user_uuid}")
async def delete_user_by_uuid(user_uuid: str, db:AsyncSession=Depends(get_session)):
    return BaseReponse(
        status_code=200,
        timestamp= datetime.now(),
        data=await delete_user(user_uuid, db),
        message="Deleted user successfully"
    ) 

@user_router.get("/api/v1/users/{user_uuid}")

async def get_a_user(user_uuid: str, db:AsyncSession=Depends(get_session)):
    return BaseReponse(
        status_code=200,
        timestamp= datetime.now(),
        data=await get_user_by_uuid(user_uuid, db),
        message="Get user by UUID"
    )