from src.model.user_model import UserModel
from src.controller.user_controller import UserController
from src.view.user_view import UserView

user_model = UserModel()
user_controller = UserController(user_model)

user_view = UserView(user_controller)
user_view.create_user()
