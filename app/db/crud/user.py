from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.model.user import User
from app.db.schema.user import CreatUser, UpdateUser, ResponseUser
import uuid
from datetime import datetime
from fastapi import HTTPException
from typing import List
from app.db.mapper.user_mapper import to_user_response


async def get_all_users(session:AsyncSession):
    query = select(User).where(User.is_deleted==False).order_by(User.created_date.desc())
    result = await session.execute(query)
    users = result.scalars().all()
    response = []
#   map user to user_response
    for user in users:
        response.append(to_user_response(user))
        # ========================================
    return response

async def create_user(create_user:CreatUser,session:AsyncSession):
    user = User(
        uuid=str(uuid.uuid4()),
        username=create_user.username,
        email=create_user.email,
        password=create_user.password,
        is_deleted=False,
        is_verified=True,
        created_date=datetime.now(),
        updated_date=None,
        profile="google.com"
    )
    # save
    session.add(user)
    await session.commit()
    return to_user_response(user)

async def update_user(user_uuid: str, update_user_data: UpdateUser, session:AsyncSession):
    query = select(User).where(User.uuid==user_uuid).where(User.is_deleted == False)
    result = await session.execute(query)
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # 
    update_dict = update_user_data.model_dump(exclude_defaults=True)
    update_dict["updated_date"] = datetime.now()
    # start updating
    perform_update= (
        update(User)
        .where(User.uuid==user_uuid)
        .values(**update_dict)
        .returning(User)
    )
    re = await session.execute(perform_update)
    await session.commit()
    session.refresh(user)
    
    return to_user_response(user)


async def delete_user(user_uuid: str, session:AsyncSession):
    query = select(User).where(User.uuid==user_uuid).where(User.is_deleted == False)
    print(user_uuid)
    result = await session.execute(query)
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_deleted = True
    await session.commit()
    return user_uuid

async def get_user_by_uuid(uuid:str, session:AsyncSession):
    query = select(User).where(User.uuid==uuid).where(User.is_deleted == False)
    result = await session.execute(query)
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return to_user_response(user)