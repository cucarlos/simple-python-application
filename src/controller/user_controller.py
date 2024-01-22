from src.model.user_model import UserModel, UserEntity

class UserController():
    def __init__(self, user_model: UserModel) -> None:
        self._user_model = user_model
    
    def create_user(self, email: str, password: str) -> UserEntity:
        user_entity = UserEntity(email, password)
        return self._user_model.save_user(user_entity)