from app.model.user import User
from app.db.schema.user import ResponseUser
def to_user_response(user:User):
    return ResponseUser(
        uuid=user.uuid,
        username=user.username,
        email=user.email,
        created_date=user.created_date,
        updated_date=user.updated_date,
        is_deleted=user.is_deleted,
        is_verified=user.is_verified,
        profile=user.profile,
    )