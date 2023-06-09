from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

router.include_router(fastapi_users.get_auth_router(auth_backend),
                      prefix='/auth/jwt',
                      tags=['auth'],)
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate),
                      prefix='/auth',
                      tags=['auth'],)
router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate),
                      prefix='/users',
                      tags=['users'],)


@router.delete(
    # Путь и тег полностью копируют параметры эндпоинта по умолчанию.
    '/users/{id}',
    tags=['users'],
    # Параметр, который показывает, что метод устарел.
    deprecated=True)
def delete_user(id: str):
    """Не используйте удаление, деактивируйте пользователей."""
    raise HTTPException(status_code=405,
                        # 405 ошибка - метод не разрешен.

                        detail="Удаление пользователей запрещено!")
